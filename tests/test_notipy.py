from notipy_me import Notipy
from time import sleep
import pandas as pd

def test_notipy_me():
    with Notipy() as nm:
        print("Running test")
        nm.add_report(
            pd.DataFrame({
                "small":[12,3,5],
                "test":[122,32,52]
            })
        )
        sleep(5)