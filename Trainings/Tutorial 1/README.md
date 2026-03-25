# Pre-requisites, Data, Preprocessing

Contains the data from [survey of india](https://onlinemaps.surveyofindia.gov.in/Digital_Product_Show.aspx) about the administrative boundaries.

1. Check the data sanity in arcgis pro.
2. The "DISTRICT_BOUNDARY", "STATE_BOUNDARY" and the "SUBDISTRICT_BOUNDARY" have spelling errors in some of the fields.
3. Letter "A" has been replaced by ">" and "I" has been replaced by "|".
4. Identifying how many such errors have been made would be difficult manually.
5. We can use search cursor to check how many different spelling errors are made.
6. And then use an update cursor to rectify the errors.
