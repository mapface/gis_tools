'''
This script will add the Feature Class name as an attribute to a new Field

Python 2
circa 2021
'''
import arcpy, os, sys
from arcpy import env

# Allow for file overwrite
arcpy.env.overwriteOutput = True

# Set the workspace directory 
env.workspace = r"C:\Users\...\.gdb" 

# Get the list of the featureclasses to process
fc_tables = arcpy.ListFeatureClasses()

# Loop through each FC and perform the processing
for fc in fc_tables:
    print("processing " + fc)

    # Define field name and expression
    field = "FILENAME"
    expression = str(fc) #populates field   

    # Create a new field with a new name
    arcpy.AddField_management(fc,field,"TEXT")

    # Calculate field here
    arcpy.CalculateField_management(fc, field, '"'+expression+'"', "PYTHON")
