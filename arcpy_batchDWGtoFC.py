"""
Converts a directory of DWG files to a geodatabase while cleaning the names up to be FC friendly.

Python 3
May 2023
"""
import arcpy
import os
import glob


# Set local variables and location for the consolidated file geodatabase
path = r"C:\Users\..."
dwg_path = r"C:\Users\...\*.DWG"
gdb = '.gdb'

gdb_location = os.path.join(path, gdb)
spatial_ref = arcpy.SpatialReference("GDA2020_MGA_Zone_56")

# Create the primary file geodatabase
arcpy.management.CreateFileGDB(path, gdb)

# Convert all dwg files found in the path
for f in glob.glob(dwg_path, recursive=True):
        fm = os.path.join(path, f)
        out_name = os.path.splitext(os.path.basename(f))[0]
        out1 = out_name.replace(" ", "_")
        out2 = out1.replace("-","_")
        #print(clean_name)
        print("CONVERTING: {0}".format(fm))
        arcpy.conversion.CADToGeodatabase(input_cad_datasets =fm, out_gdb_path = gdb_location, out_dataset_name = out2,reference_scale = 1000,
                                          spatial_reference = spatial_ref)


