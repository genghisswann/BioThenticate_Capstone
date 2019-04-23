import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import numpy as np
import datetime
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

#Establish a standard date format
yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y%m%d"))
today2 = str(datetime.datetime.now().strftime("%Y-%m-%d"))

def plotting():
    UI = input("(today)\n(yesterday)\n(other)\nWhich day do you want to plot: ")

    if UI == "today":
        print("plot today")
        dateSelect = today
    elif UI == "yesterday":
        print("plot yesterday")
        dateSelect = yesterday
    elif UI == "other":
        y = input("Enter year: ")
        m = input("Enter month: ")
        d = input("Enter day: ")

        dateSelect = str(y + m + d)
    else:
        print("Yikes...")

    thisFile = ('data/rawHR/' + 'HR_' + dateSelect + '.csv')
    print ("\nFile to be plotted is: ", thisFile)
    print("Plotting...\n")

    try:
        df = pd.read_csv(thisFile)
    except:
        print("Archive not updated to ", today2)

    #print(df.Time)
    #format = datetime.datetime.strptime(df.Time, '%H:%M:%S').time()
    #df.Time = pd.to_datetime(df.Time, format='%H:%M:%S')
    #print(df.Time)

    plt.figure(figsize=(16,6))
    plt.step(df.Time, df.HR)
    print(df.Time)

    #fig, ax = plt.subplots()
    #ax.plot(df.Time, df.HR)

    #start, end = ax.get_xlim()

    #ax.xaxis.set_ticks(np.arange(start, end, 1))
    #ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))

    #plt.locator_params(axis='x', nbins=10)

    locs, labels = plt.xticks()
    plt.ylabel('Heart Rate (BPM)')
    plt.xlabel('Time')
    boi = (len(df.index))
    plt.xticks(np.arange(0, boi))
    #plt.xticks(np.arange(12), ('12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))
    plt.show()

    #plt.xticks(np.arange(minTT, maxTT + 1, 1.0))



if __name__ == "__main__":
    plotting()