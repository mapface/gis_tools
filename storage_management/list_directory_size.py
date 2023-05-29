"""
Script to list the sizes of sub folders of the input path.
Just enter input path and a name for the CSV to write.

Python 3
Date Created: 24/11/2021
"""

import os
import csv
from datetime import datetime

# path
path = "C:\..."

# csv
csv_name = 'test.csv'

# list of directories
list = os.listdir(path)

# current date
dt_now = datetime.now()
now = dt_now.date()


# function to get folder size
def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size


# function to convert bytes into human readable format
def sizeof_fmt(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


# write csv
with open(csv_name, 'w', newline="") as csv_file:
    csv_write = csv.writer(csv_file, delimiter=',')
    csv_write.writerow(['Date', 'Drive', 'Folder', 'Size_HumanReadable', 'Size_Bytes'])
    for x in list:
        folder = path + "\{0}".format(x)
        drive = os.path.splitdrive(folder)[0]
        hr_size = sizeof_fmt((getFolderSize(folder)))
        byte_size = str(getFolderSize(folder))
        csv_write.writerow([now, drive, folder, hr_size, byte_size])
        print(os.path.basename(folder) + " Size: " + hr_size + " / " +
              byte_size + " bytes.")

print("Script finished.")
