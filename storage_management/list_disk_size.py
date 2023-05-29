"""
Exports csv of disk storage size.
This will append new values to the current csv.
CSV should sit in the same folder as the script.
Created for a power BI workflow

Version: Python 3
Date Created: 24/11/2021
"""

import shutil
import csv
import os
from datetime import datetime

# disks
disks = ["A:/", "B:/", "C:/"]

# csv
csv_name = 'csv_name.csv'

# current date
dt_now = datetime.now()
now = dt_now.date()

with open(csv_name, 'a', newline="") as csv_file:
    csv_write = csv.writer(csv_file, delimiter=',')
    # only uncomment the line below if you want to create a new csv/need headings
    # csv_write.writerow(['Date', 'Drive', 'Total_Bytes', 'Total_Tb', 'Used_Bytes', 'Used_Tb', 'Free_Bytes', 'Free_Tb'])
    for x in disks:
        total, used, free = shutil.disk_usage(x)
        drive = os.path.splitdrive(x)[0]
        total_tb = round((total / float(1 << 40)), 2)
        used_tb = round((used / float(1 << 40)), 2)
        free_tb = round((free / float(1 << 40)), 2)
        csv_write.writerow([now, drive, total, total_tb, used, used_tb, free, free_tb])

print("Script finished.")
