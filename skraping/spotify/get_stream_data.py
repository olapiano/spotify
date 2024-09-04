from datetime import datetime
import pandas as pd
from settings import Settings
from skraping.scraping_utilities import ScrapingUtilities
from skraping.xpaths import SongXPATH


def get_stream_data():
    # Hämta xpaths
    xpath = SongXPATH

    # Läs in länkarna från excelfil till en DataFrame
    df = pd.read_excel(
        Settings.xlsx_playlist_links_file_name,
        sheet_name=Settings.xlsx_playlist_links_sheet_name,
    ).dropna()

    # Hämta skrapverktyg, initiera driver, ladda in sida etc
    su = ScrapingUtilities(
        web_driver=Settings.web_driver,
        website=df[Settings.xlsx_playlist_links_title].loc[df.index[0]],
        timeout_large=Settings.timeout_large,
        timeout_small=Settings.timeout_small,
        page_load_strategy=Settings.page_load_strategy,
    )

    # Clicka bort cookieknappen
    su.click_element(xpath.cookie_button)

    # Listan där data om låtarna sparas
    the_list = []

    # Loopa en länk i taget i listan
    for link in df[Settings.xlsx_playlist_links_title]:
        # Ladda in låten
        su.load_page(link)

        # Hämta webbelementen med data om låten
        artist_element = su.get_element(xpath.artist)
        song_title_element = su.get_element(xpath.song_title)
        streams_element = su.get_element(xpath.streams)

        # Hämta texten från webbelementen
        artist = su.get_text_from_element(artist_element)
        song_title = su.get_text_from_element(song_title_element)
        streams = int(su.get_text_from_element(streams_element).replace(" ", ""))

        # Lägg till datan i listan
        the_list.append({"Song": song_title, "Artist": artist, "Streams": streams})

    # Intiera en DataFrame som sedan kan skapa en excelfil
    df2 = pd.DataFrame(the_list)
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")

    print("Summa: ", df2["Streams"].sum())

    df3 = pd.DataFrame([df2["Streams"].sum()], columns=["Total sum"])

    with pd.ExcelWriter(Settings.xlsx_stream_data_file_name) as writer:
        df2.to_excel(writer, sheet_name=f"Song data {date}")
        df3.to_excel(writer, sheet_name=f"Total {date}")

    print("Excelfil skapades med lyssningsdata")
