from pyautocad import Autocad
import os, csv

# Initialize AutoCAD connection
acad = Autocad()

# Output CSV file path
output_csv_path = r"C:\Users\nomit.rawat\Documents\Drawing to vector\Test"
output_csv_name = "output_layers_colors.csv"
output_csv = os.path.join(output_csv_path, output_csv_name)

# Ensure the output directory exists
output_dir = os.path.dirname(output_csv)  # Extract the directory path
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # Create the directory if it doesn't exist

# CSV Header
csv_header = ["Layer Name", "Red", "Green", "Blue", "Linetype", "Lineweight", "Transparency"]

# Open CSV file to write data
with open(output_csv, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_header)  # Write the CSV header

    # Iterate through all layers in the AutoCAD document
    for layer in acad.doc.Layers:
        layer_name = layer.Name  # Get the layer name
        color = layer.TrueColor  # TrueColor object contains RGB information

        # Extract Red, Green, and Blue components
        red = color.Red
        green = color.Green
        blue = color.Blue

        # Extract Linetype
        linetype = layer.Linetype if layer.Linetype else "Default"

        # Extract Lineweight
        lineweight = layer.Lineweight
        # Convert lineweight to a readable value (e.g., mm or inches)
        lineweight_value = (
            lineweight.Name if hasattr(lineweight, "Name") else str(lineweight)
        )

        # # Extract Transparency
        # transparency = layer.Transparency  # Returns a Transparency object
        # transparency_value = (
        #     round(transparency / 255 * 100, 2) if transparency is not None else "0"  # 0 for no transparency
        # )

        # Write layer name and RGB values to the CSV
        writer.writerow([layer_name, red, green, blue, linetype, lineweight_value])

print(f"Layer color information has been exported to {output_csv}.")