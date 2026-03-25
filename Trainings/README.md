Small notes

[Documentation used for reference](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/describing-data.htm)
- Insert cursor adds new rows.
- Cursors honor layer and table view definition queries and selections. The cursor object only contains the rows that would be used by any geoprocessing tool during an operation.
- The OBJECTID@ token can also be used as a shortcut in place of a table's object ID field name, to get the unique ID.
- The SHAPE@ token, which returns a geometry object, can be used to access the geometry field of a feature class without having prior knowledge of the field name. This can help in getting the x and y co-ordinate.
- Insert and update locks.
- The **shape/geometry** field in the attribute table holds the geometry object. You can also check the tutorial on geopandas.
- Point worth noting: In arcpy, when you retrieve the geometry of a feature, it's represented as a sequence of points that describe the shape of the feature. For example, a rectangle might be represented by five points: the first and last points are the same to close the polygon. So a qaudrilateral feature would have five vertices.

**Also for future possibility**:
- Working on complex geometries (recursive islands)
- A bit about toolboxes
