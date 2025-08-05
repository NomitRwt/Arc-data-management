# Pre-requisites
# should be run in arcgis notebook
# the layer on which the symbology needs to be applied need to present in the contents pane

# import the modules
import arcpy, csv

# load the csv into a dictionary
# csv sample
# Layer Name, Red, Green, Blue,
# A, 0, 0, 255
# B, 0, 25, 0
#.....
csv_path = "path"

# Convert the dictionary vaLues into a dictionary
color_dict = {}

with open(csv_path, 'r') as f:
  reader = csv.DictReader(f)
  for row in reader:
    color_dict[row["Layer Name"]] = (int(row["Red"]), int(row["Green"]), int(row["Blue"]))


# Use the current project and active map
aprx = arcpy.mp.ArcGISProject("CURRENT")  # "CURRENT" is used for scripts run within Pro
map_obj = aprx.activeMap  # Or aprx.listMaps("Map")[0] for the first map

# Apply the symbology on all the valid layers
for lyr in map_obj.listLayers():
  
  # Should be a feature and not table etc.
  if not lyr.isFeatureLayer:
    continue

  # Should be one of the following geometry types Polygon, Polyline, Point
  desc = arcpy.Describe(lyr)
  if desc.shapeType not in ["Polygon", "Polyline", "Point"]:
    continue

  # Should have the field "Layer" in the attribute table
  fields = [f.name for f in arcpy.ListFields(lyr)]
  if "Layer" not in fields:
    continue

  # Get the symbology object for the layer
  sym = lyr.symbology

  # Check whether it has a renderer
  if hasattr(sym, "renderer"):
    # Update the renderer to unique value and the field based on which the symbology is applied
    sym.updateRenderer('UniqueValueRenderer')
    sym.renderer.fields = ['Layer']

    # Set symbology color based on color_dict
    # Iterate on all the groups
    for group in sym.renderer.groups:
      # Then items inside the groups
      for item in group.items:
        # Get the layer name
        lyr_name = item.values[0][0]
        # Check whether the layer is in color dict
        if lyr_name in color_dict:
          r, g, b = color_dict[lyr_name]
          # Get the value
          symbol = item.symbol
          # Set color for simple symbols (polygon, line, point)
          symbol.color = {'RGB': [r, g, b, 100]}  # 100 = full opacity
          # Update the symbol
          item.symbol = symbol
        else:
          print("Layer not in color dictionary")

    lyr.symbology = sym  # Apply symbology back to the layer

aprx.save()
print("Symbology updated.")
