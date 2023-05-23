"""
This script will copy the entire contents of a geodatabase into another geodatabase, disabling the Z and M values in the process.

Python 3
May 2023
"""

import arcpy
import os

arcpy.env.overwriteOutput = True

# Setup
gdb_in = rf"C:\Users\...\.gdb"
gdb_out = rf"C:\Users\...\.gdb"

arcpy.env.workspace = gdb_in

def copy_fc(input_fc, output_gdb):
        arcpy.env.workspace = input_fc
        arcpy.env.outputZFlag = "Disabled"
        arcpy.env.outputMFlag = "Disabled"
        arcpy.conversion.FeatureClassToGeodatabase(input_fc, output_gdb)


#select all fc
fc_all = arcpy.ListFeatureClasses()

for fc in fc_all:
        print(rf"{fc} working...")
        copy_fc(fc, gdb_out)
