import numpy as np
import pandas as pd

def sort_accounts(df):
    print("Sorting accounts")
    accounts = df.index
    drivers = df.copy(deep = True)
    for account in accounts:
        if (len(account.split('.')) != 2) and (len(account.split('.')[-1]) > 1):
            drivers.drop(account, inplace=True)

    structures = pd.DataFrame()
    systems = pd.DataFrame()
    components = pd.DataFrame()
    for driver in drivers.index:
        if driver[0:4] == "A.21" or driver[0:5] == "A.261" or driver[0:5] == "A.245":
            structures = pd.concat([structures, drivers.loc[[driver]]])
        elif driver[0:5] == "A.252":
            systems = pd.concat([systems, drivers.loc[[driver]]])
        elif driver[0:5] == "A.221" or driver[0:5] == "A.225" or driver[0:5] == "A.229" or driver[0:7] == "A.226.8" or driver[0:7] == "A.226.9" \
          or driver[0:5] == "A.231" or driver[0:5] == "A.235" or driver[0:5] == "A.236" or driver[0:5] == "A.237" or driver[0:5] == "A.262" \
          or driver[0:4] == "A.24" or driver[0:4] == "A.25":
            components = pd.concat([components, drivers.loc[[driver]]])
        elif driver[0:5] == "A.222" or driver[0:5] == "A.223" or driver[0:5] == "A.224" or driver[0:5] == "A.233" \
          or driver[0:5] == "A.234" or driver[0:6] == "A.226.":
            systems = pd.concat([systems, drivers.loc[[driver]]])

    return structures, systems, components