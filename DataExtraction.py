#THIS MODULE SERVES THE PURPOSE OF MANUALLY EXTRACTING DATA FROM THE FITBIT.
#CURL FUNCTIONS ARE REQUIRED TO FETCH FILES

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import seaborn as sns
import json
import pandas as pd


#GENERAL FITBIT DATA
#Opens file obtained from Fitbit site
def exProfileData():
    print("Beginning Data Extraction Process...\n")
    with open('data/user1/profile.json') as file:
        json_profile = json.load(file)

    profile = json_profile['user']
    keys = profile.keys()
    subset_keys = sorted(set(keys) - set(['topBadges', 'dateOfBirth', 'avatar', 'avatar150', 'encodedId']))

    #Print entire dataset from Fitbit site
    userInput = input("\nDo you want to print data in terminal? y/n: ")
    if userInput == 'y':
        for i, key in enumerate(subset_keys):
            print('{:<30}: {}'.format(key, profile[key]))

    print('{:.2f}'.format(profile['strideLengthRunning'] / profile['strideLengthWalking']))

    #Write exctracted to file
    userInput = input("\nDo you want write data to file? y/n: ")
    if userInput == 'y':
        with open ("exData.txt", "w+") as file:
            for i, key in enumerate(subset_keys):
                file.write('{:<30}: {}'.format(key, profile[key]))
                file.write("\n")
            file.close()


#HR DATA
def exHRData():
    print("Beginning HR Data Extraction...\n")


    with open('data/user1/HR_2019-04-04_1d_1min.json') as f:
        HR_intra_1min_json = json.load(f)

    HR_intra_1min_json.keys()
    print(HR_intra_1min_json.keys(), "\n")
    HR_intra_1min = pd.DataFrame(HR_intra_1min_json['activities-heart-intraday']['dataset'])
    HR_intra_1min['TimeStamp'] = pd.to_datetime(HR_intra_1min.time)

    #print("Timestamp: ", HR_intra_1min.time, "\n")
    #print("Value: ", HR_intra_1min.value, "\n")

    plt.figure(figsize=(18, 5))
    plt.step(HR_intra_1min.TimeStamp, HR_intra_1min.value)
    plt.ylabel('Heart Rate (BPM)')
    plt.xlabel('Time')
    plt.show()

if __name__ == "__main__":
    #exProfileData()
    exHRData()