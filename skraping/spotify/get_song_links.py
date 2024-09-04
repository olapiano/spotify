import time
import pandas as pd
from selenium.common import StaleElementReferenceException
from skraping.scraping_utilities import ScrapingUtilities
from skraping.xpaths import PlayListXPATH
from selenium.webdriver import ActionChains
from settings import Settings


def get_song_links():
    # Hämta xpaths
    xpath = PlayListXPATH

    # Hämta skrapverktyg, initiera driver, ladda in sida etc
    su = ScrapingUtilities(
        web_driver=Settings.web_driver,
        website=Settings.href_to_playlist,
        timeout_large=Settings.timeout_large,
        timeout_small=Settings.timeout_small,
        page_load_strategy=Settings.page_load_strategy,
    )

    # Clicka bort cookieknappen
    su.click_element(xpath.cookie_button)

    # Spara spellistans namn
    title_element = su.get_element(xpath.list_title)
    title = su.get_text_from_element(title_element)

    list_of_songs = []
    list_of_song_links = []
    previous_last_song_number = "1"

    while True:
        # Alla tillgängliga sånger
        songs = su.get_elements(xpath.list_of_songs)

        last_song_index = len(songs)
        last_song_number_element = su.get_element_with_index(xpath.list_of_songs, last_song_index,
                                                             xpath.list_item_number)
        last_song_number = su.get_text_from_element(last_song_number_element)

        for song in songs:
            if song not in list_of_songs:
                list_of_songs.append(song)

        for index, song in enumerate(songs):
            link_element = su.get_element_with_index(xpath.list_of_songs, index + 1, xpath.list_item_link)
            link = su.get_href_from_element(link_element)
            if link not in list_of_song_links:
                list_of_song_links.append(link)

        for x in range(1, 6):
            try:
                ActionChains(su.get_driver()).scroll_to_element(songs[-1]).perform()
                break
            except StaleElementReferenceException:
                print("StaleElementReferenceException i försök nr ", x)

        time.sleep(Settings.timeout_small)

        if last_song_number == previous_last_song_number:
            break

        previous_last_song_number = last_song_number

    df = pd.DataFrame(list_of_song_links)
    df.columns = [Settings.xlsx_playlist_links_title]
    df.to_excel(
        Settings.xlsx_playlist_links_file_name,
        engine="xlsxwriter",
        sheet_name=Settings.xlsx_playlist_links_sheet_name,
        index=False)

    print(f"Excelfil skapades/uppdaterades med länkar till låtar från spellistan: {title}")
