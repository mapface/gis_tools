'''
This script was written to merge annotation masks by name, which followed the convention such as Mountains_14A.

Had some issues with similarily named features.

Python 2
circa 2019
'''

import arcpy, os
from collections import defaultdict

# set annotation gdb and output gdb
arcpy.env.workspace = r'C:\...\.gdb'
output_gdb = r'C:\...\.gdb'
arcpy.env.overwriteOutput = True

# create list from anno gbd of feature classes
fcnames = list(set([fc[:-6] for fc in arcpy.ListFeatureClasses(feature_type='POLYGON')]))
# turn list into tuple
lookfor = tuple(fcnames)
print lookfor

# create dictionary, loop through based on lookfor tuple and merge based on fc name and suffix
d = defaultdict(list)
[d[l] for l in lookfor]  # Add the keys

for feature in arcpy.ListFeatureClasses(feature_type='POLYGON'):
    for k, v in d.items():  # d.iteritems() py2/ArcMap
        if feature.startswith(k):
            d[k].append(feature)
            print("Appending" + " " + k)

print d

for k, v in d.items():
    arcpy.Merge_management(inputs=v, output=os.path.join(output_gdb, k + '_AM'))
    print("Merging" + " " + k)
