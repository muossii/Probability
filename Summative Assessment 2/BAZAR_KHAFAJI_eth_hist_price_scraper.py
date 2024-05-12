import json
import requests
import polars as pl
from datetime import datetime
import time as t
import multiprocessing as mp


def get_eth_historical(start, end, fname):

    dates = pl.datetime_range(start, end, "1d", eager=True)
    dates = [int(datetime.timestamp(x)) for x in list(dates)]
    pair = "ethusd"
    p = 0

    list_data = []
    for first, last in zip(dates, dates[1:]):
        p += 1

        parameters = {
            "step": 300,
            "limit": 228,
            "start": first,
            "end": last
        }

        req = requests.get(f"https://www.bitstamp.net/api/v2/ohlc/{pair}/",
                           params=parameters)

        req = req.json()["data"]["ohlc"]

        list_data += req

        if p == 43:
            t.sleep(60*10)

    df = pl.DataFrame(list_data).unique(subset="timestamp")
    file_name = "BAZAR_KHAFAJI_ETHUSD_"+fname+".csv"
    df.write_csv(file_name, separator=",")


if __name__ == '__main__':

    start_dates = ["2015/8/7 00:00:00", "2017/10/9 00:00:00", "2019/12/12 00:00:00", "2022/2/13 00:00:00"]

    end_dates = ["2017/10/9 00:00:00", "2019/12/12 00:00:00", "2022/2/13 00:00:00", "2024/4/16 00:00:00"]

    starte = [datetime(2015, 8, 7),
              datetime(2017, 10, 9),
              datetime(2019, 12, 12),
              datetime(2022, 2, 13)
              ]

    ende = [datetime(2017, 10, 9),
            datetime(2019, 12, 12),
            datetime(2022, 2, 13),
            datetime(2024,4,16)
            ]

    p1 = mp.Process(target=get_eth_historical, args=(starte[0],ende[0],"1", ))
    p2 = mp.Process(target=get_eth_historical, args=(starte[1], ende[1], "2",))
    p3 = mp.Process(target=get_eth_historical, args=(starte[2], ende[2], "3",))
    p4 = mp.Process(target=get_eth_historical, args=(starte[3], ende[3], "4",))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("Done!")