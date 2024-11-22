# Python pre-requisites
1. Variables, data type
2. Control flow, looping
3. Object oriented programming (good to know!)
4. Data structures and algorithms (what not to do!)

Primer on syntax
camelCase, PascalCase, snake_case

# [Esri Documentation](https://pro.arcgis.com/en/pro-app/latest/arcpy/main/arcgis-pro-arcpy-reference.htm)
Short notes.

# Get Started
- Arcgis pro python environment comes with arcpy and along with it some other libraries.
- While `pip` is de-facto standard when managing libraries when exclusively in python. Arcgis pro uses conda as the package manager.
- Run a stand-alone python script using the command `c:\Progra~1\ArcGIS\Pro\bin\Python\scripts\propy.bat path_tp_your_script\my_script.py`
- How is using `propy.bat` benefitial
  - This is why you use propy.bat: it determines the application’s active conda environment and activates it in your stand-alone script.
- While the `c:\Progra~1\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe` is the default path.
- Third party libraries used in are available [here](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/available-python-libraries.htm)

## [What is Arcpy?](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm)
- Tool vs non-tool not found in standard toolbox, example can be utility functions like `ListFeatureClasses()`
- Tools return a result object
- Messages from running tools can be accessed using `GetMessages()` function.
- Similar to environment settings in toolbox interface we can set them in script itself.
- Also provides classes for setting spatial reference, extent and field mappings.
- Modular division of code similar to toolbox.
- Can add arcpy in an environment `conda install arcpy=3.4 -c esri`.
- Can also use a base version of arcpy that offers only bare minimum required libraries, `conda create -n my-env arcpy-base`.

## Working with data
1. [Describing data](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/describing-data.htm)
- Describe properties such as whether the feature class is a polygon, polyline or point.
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
