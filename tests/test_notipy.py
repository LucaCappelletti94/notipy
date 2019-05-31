from notipy_me import Notipy
from time import sleep
import pandas as pd

def test_notipy_me():
    try:
        with Notipy() as nm:
            print("Running test")
            sleep(3)
            nm.add_report(pd.DataFrame({"small":[12,3,5]}))
            sleep(2)
            raise ValueError("Test")
    except ValueError:
        pass