"""
Scipt to batch convert KMZ/KML files to feature classes.

This is a modified version of the ESRI script, changed to account for duplicate names (appends a number as a suffix to create unique
feature class names)

Python 3
May 2023
"""

import arcpy
import os

# Set workspace (where all the KMLs are)
arcpy.env.workspace = r"C:\Users\AUAQ508040\Data\GoldCoastVehicleSignage\OTHER_KML"

# Set local variables and location for the consolidated file geodatabase
out_location = r"C:\Users\AUAQ508040\Data\GoldCoastVehicleSignage\OTHER_KML"
gdb = 'AllKMLLayers.gdb'
gdb_location = os.path.join(out_location, gdb)

# Create the primary file geodatabase
arcpy.management.CreateFileGDB(out_location, gdb)

# Convert all KMZ and KML files found in the current workspace
for f in arcpy.ListFiles('*.KM*'):
        km = os.path.join(arcpy.env.workspace, f)
        print("CONVERTING: {0}".format(km))
        arcpy.conversion.KMLToLayer(km, out_location)

# Change the workspace to fGDB location
arcpy.env.workspace = out_location

# Loop through all the file geodatabases in the workspace
wks = arcpy.ListWorkspaces('*', 'FileGDB')
# Skip the primary GDB
wks.remove(gdb_location)

for fgdb in wks:
    # Change the workspace to the current file geodatabase
    arcpy.env.workspace = fgdb

    # For every feature class inside, copy it to the primary and use the name 
    # from the original fGDB  
    feature_classes = arcpy.ListFeatureClasses('*', '', 'Placemarks')

    fgdb_name = os.path.basename(fgdb)[:-4]  # Get the name of the source file geodatabase
    
    for fc in feature_classes:
            fc_name = fc[:-4] if fc.endswith('.shp') else fc  # Remove extension from feature class name
            target_fc_name = f"{fgdb_name}_{fc_name}"
            count = 1
            while target_fc_name in arcpy.ListFeatureClasses():  # Check if feature class name already exists
                target_fc_name = f"{fgdb_name}_{fc_name}_{count}"  # Append _1, _2, _3, etc. until a unique name is found
                count += 1
    print(f"COPYING: {fc} TO: {target_fc_name}")
    fc_copy = os.path.join(fgdb, 'Placemarks', fc)
    arcpy.conversion.FeatureClassToFeatureClass(fc_copy, gdb_location, target_fc_name)



