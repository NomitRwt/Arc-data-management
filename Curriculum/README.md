# Python pre-requisites
1. Variables, data type
2. Control flow, looping
3. Object oriented programming (good to know!)
4. Data structures and algorithms (what not to do!)

Primer on syntax
camelCase, PascalCase, snake_case

## Setting up vscode with arcgis interpreter
[Explained here](https://resources.esri.ca/getting-technical/how-to-configure-visual-studio-code-with-arcgis-pro-s-python-environment)

# [What is Arcpy?](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm)
Notes from esri documentation

## Introduction to arcpy
1. [Quick tour of arcpy](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/a-quick-tour-of-arcpy.htm)
- Tool vs non-tool
- Return values
2. [Essential vocabulary](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/essential-arcpy-vocabulary.htm)
3. [Package manager](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-conda.htm)

## Working with data
1. [Describing data](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/describing-data.htm)
2. [List fields as opposed to describe](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/fields-and-indexes.htm)
- Important properties of field object
- Name and Type.
3. [Spatial reference class](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/the-spatial-reference-object.htm)
- Using the describe method to get the spatial reference
- Creating new spatial reference class using wkid
4. Checking the existence of feature class
5. [Query data in python](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/specifying-a-query.htm)
- Query in cursors
- Field delimeters for query language (Not important but good to know)
6. [Cursors](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/data-access-using-cursors.htm)
- Search, Insert, Update
- arcpy.da cursors instead of old ones.
- Cursors using for and with statements. What is the difference?
- Cursors honor layer and table view definition queries and selections. The cursor object only contains the rows that would be used by any geoprocessing tool during an operation.
- The OBJECTID@ token can also be used as a shortcut in place of a table's object ID field name, to get the unique ID.
- The SHAPE@ token, which returns a geometry object, can be used to access the geometry field of a feature class without having prior knowledge of the field name. This can help in getting the x and y co-ordinate.
- Insert and update locks.
7. [Reading geometries](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/reading-geometries.htm)
- Reading point geometries
- Reading multipoint geometries
- Reading polyline or polygon geometries
- **Complex geometries**
8. [Writing geometries](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/working-with-numpy-in-arcgis.htm)
- **Pending**
9. [Using geometry objects](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/using-geometry-objects-with-geoprocessing-tools.htm)
- Input geometry objects
- Output geometry objects
10. [Validating table and field names](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/working-with-geodatabases.htm)
11. [Multiple value parameters](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/working-with-multivalue-inputs.htm)
- Delete fields can use a list of values

# Others
1. Creating point, line and polygon data
2. Raising arcpy.ExecuteError("Some error")
3. Spatial query
4. Joins and relate
5. Introduction to toolboxes

# Tutorial
1. [Data sanity check](https://github.com/NomitRwt/Arc-data-management/tree/main/Curriculum/Tutorial%201)
2. [Updating data](https://github.com/NomitRwt/Arc-data-management/tree/main/Curriculum/Tutorial%202)
3. [Arcgis API for Python: Introduction](https://github.com/NomitRwt/Arc-data-management/tree/main/Curriculum/Training%203)
4. [Reading and writing geometries](https://github.com/NomitRwt/Arc-data-management/tree/main/Curriculum/Tutorial%204)
5. [Toolboxes](link)
