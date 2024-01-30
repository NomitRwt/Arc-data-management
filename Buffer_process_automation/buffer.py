import arcpy, os

# Following items should be present in directory where the script is running
# 1. CSV containing the buffer values
# 2. Geodatabase containing different street types
# 3. Geodatabase containing the poles feature class
cwd = os.getcwd()
workspace = os.path.join(cwd, "Street_Types.gdb")
fc_poles = os.path.join(cwd, "Poles.gdb\pole_data")

# The workspace is set to the "Street_Types.gdb" geo-database which is "NOT" the primary database
arcpy.env.workspace = workspace

f = open("Buffer.csv", "r")
data = f.readlines()

# 1. Boolean to skip the header
# 2. Boolean to check if all the feature class mentioned in csv are there in database
# 3. Count of total buffer fc created
# 4. List of buffered fc
header_exists, fc_all_exists, count, buffer_fc = True, True, 0, []

for line in data:

    if header_exists:
        header_exists = False
        continue
    
    line_split = line.split(",")
    input_name, m1, m2, m3, m4, m5 = line_split[0], float(line_split[1]), float(line_split[2]), float(line_split[3]), float(line_split[4]), float(line_split[5].replace("\n", ""))

    # Calculate the buffer distance
    # 1. Take the average
    # 2. Half of this is the buffer
    # 3. Type conversion to string
    # 4. Add feet in the end
    buffer_distance, output_name = str(((m1+m2+m3+m4+m5)/5)/2) + " Feet", input_name + "_buffer"


    if arcpy.Exists(input_name):
        print("Found the feature class: "+input_name)
        print("Buffer distance for the above feature class: "+buffer_distance)
        
        try:
            arcpy.analysis.Buffer(input_name, output_name, buffer_distance)
            count += 1
            print("Buffer created")
            print("\n")
            buffer_fc.append(output_name)
        except Exception as e:
            print("Some error occured while creating buffer")
            print(e)
    
    else:
        fc_all_exists = False
        print("ALERT!!!")
        print("Cannot find the feature class: "+input_name)
        print("\n")

# The script would not create the merged feature class if any of the layer is missing
if fc_all_exists:
    print("Total buffered fc's "+ str(count))
    print("\n")
    arcpy.management.Merge(buffer_fc, "fc_street_merge")

    print("Merged feature class created")
    print("\n")

if arcpy.Exists(fc_poles):
    arcpy.management.AddField(fc_poles, "Road_Access", "TEXT", "","", 1)
    print("'Road Access' field added")

else:
    print("Poles fc is missing, cannot add 'Road Access' field")

#Calculate the "Road_Access" field as "N" for all the rows
arcpy.management.CalculateField(fc_poles, "Road_Access", '"""N"""') #Notice the third argument

#Make the feature layer for selecting features within 40 feet of buffer distance
#And populate the field
arcpy.management.MakeFeatureLayer(fc_poles, "fc_poles_lyr")
arcpy.management.SelectLayerByLocation("fc_poles_lyr", "INTERSECT", "fc_street_merge", "40 Feet")
arcpy.management.CalculateField("fc_poles_lyr", "Road_Access", '"""Y"""')

print("Complete")