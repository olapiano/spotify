from skraping.chrome_driver import ChromeDriver


class Settings:
    # Spellistans HREF
    href_to_playlist = "https://open.spotify.com/playlist/37i9dQZF1DX49poIUZYXp7"

    # Namn på excelfilerna
    xlsx_stream_data_file_name = "stream_data.xlsx"
    xlsx_playlist_links_file_name = "playlist_links.xlsx"
    xlsx_playlist_links_sheet_name = "Links"
    xlsx_playlist_links_title = "Links"

    # Maxtid i sekunder att vänta varje gång ett element ska läsas in eller klickas på
    # Öka om uppkopplingen för långsam
    timeout_large = 10
    timeout_small = 1

    # Driver (typ koppling till) den webbläsare som ska användas
    # Just nu finns bara en till Chrome
    web_driver = ChromeDriver

    # 'normal' (vänta tills hela sidan laddats in, kan göra att allt fastnar)
    # 'eager' (grundsidan är inladdad men kanske inte alla bilder mm)
    # 'none' (kör på direkt)
    page_load_strategy = "eager"
