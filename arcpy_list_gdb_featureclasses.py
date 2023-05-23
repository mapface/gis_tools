"""
Simple script designed to list feature classes in a GDB if a text list is needed for any reason. 

Python 3
May 2023
"""

import arcpy.mp
import os
arcpy.env.overwriteOutput = True

# Setup
gdb = r""

arcpy.env.workspace = gdb

#select all fc
fc_all = arcpy.ListFeatureClasses()

#clip all
for fc in fc_all:
    print(fc)

#finish
print("Script complete.")


