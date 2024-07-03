import arcpy

arcpy.env.workspace = r"C:\Users\nomitrawat\Documents\Training\Data\Sample"

fc = "POLYGONS.shp"
type = "Polygon"

with arcpy.da.SearchCursor(fc, ['SHAPE@', 'OID@', 'TYPE']) as cursor:
    for row in cursor:
        
        if row[2]==type:
            # Access the geometry object of the feature
            geom = row[0]

            # Get the number of parts in the geometry
            num_parts = geom.partCount

            # Iterate through each part
            for part_index in range(num_parts):
                # Get the array of points for the current part
                part_array = geom.getPart(part_index)

                # Output the points in the current part
                print(f"Part {part_index} points:")
                for pnt in part_array:
                    if pnt != None:
                        print(f"({pnt.X}, {pnt.Y})")
                print()  # Empty line for separation