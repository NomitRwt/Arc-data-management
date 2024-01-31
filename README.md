# Arc-data-management
A set of python scripts which have been used for GIS data management tasks, primarily using arcpy, python library. The repository contains standalone python scripts divided into separate folders depending on the process.

Following is an overview of the folders and process involved

## [Buffer process automation](https://github.com/NomitRwt/Arc-data-management/tree/main/Buffer_process_automation)

We need to select poles located within certain distance from the road. There are different types of roads in the "Streets_Types.gdb" database. For each road type we "manually" measure the width of the road at 5 different locations using an esri basemap and create a "Buffer.csv" file containing all the values. The buffer name for all the files should match with the names of the road types present in the "Streets_Types.gdb".

The script requires following three files in the working directory (The folder in which the script is present).
1. Buffer.csv
2. Street_Types.gdb
3. Poles.gdb

The rest of the process is done using arcpy.

First for each road type we generate the buffer, depending on the values present in the CSV (The road width that was measured). Now we merge all the buffer into a single feature class and apply a spatial query to select all the poles located within a distance of 40 feet. A new field is added to the "Poles.gdb" layer depicting whether it is located within certain distance or not.
