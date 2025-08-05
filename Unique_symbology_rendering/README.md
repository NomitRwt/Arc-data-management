# Notes
The following feature layer renderers are currently supported in arcpy.mp:

1. SimpleRenderer
2. GraduatedColorsRenderer
3. GraduatedSymbolsRenderer
4. UnclassedColorsRenderer
5. **UniqueValueRenderer**

## Unique value renderer
1. If you change your current renderer to the UniqueValueRenderer, you first have to set the **appropriate fields** property value.
2. The property is **plural** because you can build a set of unique values based on multiple fields.
3. Therefore, the fields property takes a list, even if there is only one field being used.
4. Once you apply your fields, the renderer will automatically generate all the unique values.
5. If, for whatever reason, new values are added to the layer, you will need to reset the renderer so that all the values are added again. 
6. You can do this by changing the fields property, or you can use the addValues method.
7. You need to understand **how unique values are managed** in the renderer so you can navigate through the class structure to change individual items and their values.
8. The **groups property returns a list of ItemGroup** objects.
9. Each **ItemGroup represents a category of items that each have their own heading**.
10. By default, there is **one ItemGroup**.
11. The **items property** returns a **list of Item objects**.
12. Once you have an item, you can change properties such as label and description. You can also **modify the symbol for each item**.
13. The reason the values property is plural and returns a list is because you can also group items in an ItemGroup. Therefore, each item could have **multiple values**.
14. The following is one way to outline the class structure:
        groups—Returns a list of ItemGroup objects
            1. heading
            2. items—Returns a list of Item objects
                1. description
                2. label
                3. symbol
                4. values
15. You can also **add and remove values** from the renderer.
16. Each **unique value** is actually an **item** in the **object model** and **each item** is associated within an **ItemGroup**.
17. To addValues or removeValues, you need to work with a **Python dictionary**.
18. The dictionary key is the name of the group heading, and its value is a list of values based on the fields property.
19. There is also a **listMissingValues** method that allows you to determine what values are currently missing from the renderer.
20. Values would only be missing if you intentionally called removeValues, because—by default—the renderer automatically creates all unique values when the fields property is set.
21. **If your objective is to create new group headings to organize your unique value items, you must first call removeValues to remove the items, and then use addValues to create a new group with a new heading label**.
