import json
import requests
import polars as pl
from datetime import datetime
import time as t
import multiprocessing as mp


def get_btc_historical(start, end, fname):

    dates = pl.datetime_range(start, end, "12H", eager=True)
    dates = [int(datetime.timestamp(x)) for x in list(dates)]
    pair = "btcusd"
    p = 0

    list_data = []
    for first, last in zip(dates, dates[1:]):
        p += 1

        parameters = {
            "step": 60,
            "limit": 720,
            "start": first,
            "end": last
        }

        req = requests.get(f"https://www.bitstamp.net/api/v2/ohlc/{pair}/",
                           params=parameters)

        req = req.json()["data"]["ohlc"]

        list_data += req

        if p == 13:
            t.sleep(60*10)
            p = 0

    df = pl.DataFrame(list_data).unique(subset="timestamp")
    file_name = "BAZAR_KHAFAJI_BTCUSD_FROM2021_"+fname+".csv"
    df.write_csv(file_name, separator=",")


if __name__ == '__main__':

    starte = [datetime(2021, 3, 31),
              datetime(2021, 9, 6),
              datetime(2022, 2, 12),
              datetime(2022, 7, 21),
              datetime(2022, 12, 27),
              datetime(2023, 6, 4),
              datetime(2023, 11, 10)
              ]

    ende = [datetime(2021, 9, 6),
            datetime(2022, 2, 12),
            datetime(2022, 7, 21),
            datetime(2022, 12, 27),
            datetime(2023, 6, 4),
            datetime(2023, 11, 10),
            datetime(2024, 4, 17)
            ]

    p1 = mp.Process(target=get_btc_historical, args=(starte[0], ende[0], "1", ))
    p2 = mp.Process(target=get_btc_historical, args=(starte[1], ende[1], "2",))
    p3 = mp.Process(target=get_btc_historical, args=(starte[2], ende[2], "3",))
    p4 = mp.Process(target=get_btc_historical, args=(starte[3], ende[3], "4",))
    p5 = mp.Process(target=get_btc_historical, args=(starte[4], ende[4], "5",))
    p6 = mp.Process(target=get_btc_historical, args=(starte[5], ende[5], "6",))
    p7 = mp.Process(target=get_btc_historical, args=(starte[6], ende[6], "7",))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()

    print("Done!")
