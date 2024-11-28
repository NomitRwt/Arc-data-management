# Arc-data-management
A repository containing notes and guides primary related to arcpy.

## [Configure vscode with arcgis interpreter](https://resources.esri.ca/getting-technical/how-to-configure-visual-studio-code-with-arcgis-pro-s-python-environment)
Great resource if you want to run standalone scripts or build using the arcgis environment. Can also look at the following path if you can't find the interpreter.

C:\Users\someuser\AppData\Local\Programs\ArcGIS\Pro\bin\Python\envs\arcgispro-py3.

## [Video Resource: Building geoprocessing tools in arcgis](https://mediaspace.esri.com/media/t/1_z44wd2wj)

Noteworthy points:
1. Sharing geoprocessing tools across organisation using arcgis online.
2. Adding input messages for the toolboxes, in the metadata of the tool.

## [Video Resource: Building geoprocessing tools with python](https://mediaspace.esri.com/media/t/1_mqpjjlpc)

Noteworthy points:
1. Using feature layer as the data type for the input parameter has advantages.
2. Setting progressor

## [Previous Work: Buffer process automation](https://github.com/NomitRwt/Arc-data-management/tree/main/Buffer_process_automation)

We need to select poles located within certain distance from the road. There are different types of roads in the "Streets_Types.gdb" database. For each road type we "manually" measure the width of the road at 5 different locations using an esri basemap and create a "Buffer.csv" file containing all the values. The buffer name for all the files should match with the names of the road types present in the "Streets_Types.gdb".

The script requires following three files in the working directory (The folder in which the script is present).
1. Buffer.csv
2. Street_Types.gdb
3. Poles.gdb

The rest of the process is done using arcpy.

First for each road type we generate the buffer, depending on the values present in the CSV (The road width that was measured). Now we merge all the buffer into a single feature class and apply a spatial query to select all the poles located within a distance of 40 feet. A new field is added to the "Poles.gdb" layer depicting whether it is located within certain distance or not.

## [Previous Work: Excel_to_shapefile](https://github.com/NomitRwt/Arc-data-management/tree/main/Excel_to_shapefile)

Convert data from specific excel sheet to shapefile.

## [Notes and Tutorials](https://github.com/NomitRwt/Arc-data-management/tree/main/Curriculum)

Notes, tutorial and data.
