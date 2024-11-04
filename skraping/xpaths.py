# Gemensamma
class XPATH:
    cookie_button = "//button[@id='onetrust-accept-btn-handler']"


# Spellistan
class PlayListXPATH(XPATH):
    list_title = "//span[@data-testid='entityTitle']"
    list_of_songs = "//div[@class='contentSpacing']/div/div[2]/div[2]/div"
    list_item_number = "/div/div"
    list_item_link = "//a"


# Låt
class SongXPATH(XPATH):
    info_base = "//div[@id='main']//main//div/div[3]/div[3]/div"
    artist = info_base + "/div/span/a"
    song_title = info_base + "/span/a"
    streams = "//span[@data-testid='playcount']"
