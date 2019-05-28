from notipy_me import Notipy
from time import sleep

def test_notipy_me():
    mail = input("Please insert the test email: ")
    with Notipy("Testing notipy", mail):
        print("Running test")
        sleep(5)