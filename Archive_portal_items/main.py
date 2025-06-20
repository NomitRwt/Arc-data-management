# Required to login in Arcgis pro using the enterprise portal
# Script archives items using the group name and id

# Import the library and portal
from arcgis.gis import GIS
gis = GIS("pro")

# Gruop name and id
groups = {"A":"x", "B": "y", "C": "z"}

# Item details
for key, value in groups.items():
  print("\n")
  print(f"GROUP NAME: {key}")
  print("\n")
  for item in gis.groups.get(value).content():
    print(f"Title: {item.title}")
    print(f"Type: {item.type}")
    print(f"Owner: {item.owner}")
    print(f"Item ID: {item.id}")
    print(f"URL: {item.url}")
    print("_"*20)

# Downloading items (yet to be tested)

# Define the download path
# download_path = "path_to_local_drive"

# Search for all items
# all_items = gis.content.search(query="", max_items=10000)

# Download items
# for item in all_items:
    # item.download(save_path=download_path)

# Export and download hosted feature services
# for item in all_items:
