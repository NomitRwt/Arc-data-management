# Buffer process automation

We need to select poles located within certain distance from the road. There are different types of roads in the "Streets_Types.gdb" database. For each road type we "manually" measure the width of the road at 5 different locations and create a "Buffer.csv" file. The rest of process is done using arcpy.

The script requires following three files in the working directory.
1. Buffer.csv
2. Street_Types.gdb
3. Poles.gdb
