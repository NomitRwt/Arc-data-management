# Watershed Delineation

## Introduction
Involves the following steps. [Available at esri's documentation.](https://support.esri.com/en-us/knowledge-base/how-to-create-a-watershed-model-using-hydrology-in-arcg-000023169)

## Tools
### Fill
Makes the raster "continous". Fills the sinks and removes the peaks. [About fill tool.](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/how-fill-works.htm)

### Flow Direction
Determines the direction of flow for each cell. [About flow direction tool.](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/how-flow-direction-works.htm) Sidenote the D8 parameter consider the flow from a cell to it's neighbouring 8 cells.

### Flow Accumulation
The different direction of flow sum up to create flow accumulation. [About the flow accumulation tool.](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/how-flow-accumulation-works.htm)

### Pour Points and snap pour points

### Watershed
Create a raster that contributes to a pour point. [About the watershed tool.](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/watershed.htm)
