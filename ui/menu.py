from skraping.spotify.get_song_links import get_song_links
from skraping.spotify.get_stream_data import get_stream_data


def menu():
    choice = ""

    while choice != "0":
        print(
            """
        
-------- MENY --------
1. Updatera sånglänkar
2. Hämta data (kräver att excelfilen med länkar redan finns)
3. Båda efter varandra

0. Avsluta
"""
        )
        choice = input("Välj: ")
        if choice == "1":
            get_song_links()
        if choice == "2":
            get_stream_data()
        if choice == "3":
            get_song_links()
            get_stream_data()
