1. Nested Document Query:
The purpose of this query was to display measurement data along with related information from the site and constituency collections in a nested, hierarchical format. This query highlighted MongoDB's capacity to represent complex hierarchical relationships within a single document.

```
[
    {
        // Joins data from the "site" collection with the "measurement" collection based on Site_ID.
        $lookup: {
            from: "site", // The collection to join with
            localField: "Site_ID", // Field from the input documents
            foreignField: "SiteID", // Field from the documents of the "from" collection
            as: "siteInfo", // The array field to add to input documents; contains the joined documents
        },
    },
    {
        // Unwinds the "siteInfo" array to output a document for each element
        $unwind: {
            path: "$siteInfo", // The field path to an array field to unwind
        },
    },
    {
        // Performs another join with the "constituency" collection based on the ConstituencyID from siteInfo
        $lookup: {
            from: "constituency", // The collection to join with
            localField: "siteInfo.ConstituencyID", // Field from the "siteInfo" documents (after first $lookup)
            foreignField: "ConstituencyID", // Field from the documents of the "constituency" collection
            as: "siteInfo.constituencyInfo", // Where to put the joined documents in "siteInfo"
        },
    },
    {
        // Unwinds the "constituencyInfo" array (nested within "siteInfo") to output a document for each element
        $unwind: {
            path: "$siteInfo.constituencyInfo", // The field path to an array field to unwind
        },
    },
    {
        // Reshapes each document to include the original measurement data, site data, and constituency data
        $project: {
            measurementData: "$$ROOT", // Includes all original measurement data
            siteData: "$siteInfo", // Includes joined data from "site" collection
            constituencyData: "$siteInfo.constituencyInfo", // Includes joined data from "constituency" collection
        },
    },
]

```

2. Flat Document Structure Query:
This query aimed to combine data from the measurement, site, and constituency collections into a single flat document structure for each measurement, while also addressing the challenge of excluding null values. The flat document structure query represented the database's ability to transform data into a streamlined format, suitable for analysis or reporting purposes.

```
[
    {
        // Stage 1: Join with the "site" collection
        $lookup: {
            from: "site",                 // Specify the collection to join with
            localField: "Site_ID",        // Field from the input documents
            foreignField: "SiteID",       // Field from the documents of the "from" collection
            as: "siteInfo"                // Output array field containing the joined documents
        }
    },
    {
        // Stage 2: Unwind the joined "siteInfo" documents
        $unwind: {
            path: "$siteInfo",                     // Path to the field to be unwound
            preserveNullAndEmptyArrays: true      // Keep the documents even if "siteInfo" is null or an empty array
        }
    },
    {
        // Stage 3: Join with the "constituency" collection
        $lookup: {
            from: "constituency",                    // Specify the collection to join with
            localField: "siteInfo.ConstituencyID",   // Field from "siteInfo" documents
            foreignField: "ConstituencyID",          // Field from the documents of the "constituency" collection
            as: "constituencyInfo"                   // Output array field containing the joined documents
        }
    },
    {
        // Stage 4: Unwind the joined "constituencyInfo" documents
        $unwind: {
            path: "$constituencyInfo",                // Path to the field to be unwound
            preserveNullAndEmptyArrays: true         // Keep the documents even if "constituencyInfo" is null or an empty array
        }
    },
    {
        // Stage 5: Replace the root of the document with a merged object
        $replaceRoot: {
            newRoot: {
                $mergeObjects: [          // Merge multiple documents into a single document
                    {
                        // Convert the document to an array, filter out null fields, and convert it back to an object
                        $arrayToObject: {
                            $filter: {
                                input: { $objectToArray: "$$ROOT" },
                                as: "field",
                                cond: { $ne: ["$$field.v", null] }
                            }
                        }
                    },
                    "$siteInfo",            // Include "siteInfo" in the merged object
                    "$constituencyInfo"     // Include "constituencyInfo" in the merged object
                ]
            }
        }
    },
    {
        // Stage 6: Exclude specific fields from the final output
        $project: {
            "Site_ID": 0,                // Exclude "Site_ID" field
            "siteInfo": 0,               // Exclude "siteInfo" field
            "constituencyInfo": 0        // Exclude "constituencyInfo" field
        }
    }
]

```

3. Highest NOx Record Query:
The goal of this query was to find the measurement record with the highest NOx concentration, demonstrating MongoDB's ability to sort and filter large datasets. This query illustrated MongoDB's efficiency in processing large datasets to quickly identify key records based on specific criteria. To make the results more informative, certain variables were chosen from different collections to be displayed in the final document. 

```
[
  {
    // Sorts the documents by the NOx field in descending order
    $sort: {
      NOx: -1,
    },
  },
  {
    // Limits the result to only the top document (the one with the highest NOx value)
    $limit: 1,
  },
  {
    // Performs a lookup (join) to add related data from the "site" collection
    $lookup: {
      from: "site", // The collection to join
      localField: "Site_ID", // Field from the current documents
      foreignField: "SiteID", // Field from the "site" collection documents
      as: "siteInfo", // The name of the new array field to add to the current documents
    },
  },
  {
    // Unwinds the "siteInfo" array to transform each element into a separate document
    $unwind: {
      path: "$siteInfo",
    },
  },
  {
    // Performs another lookup to add related data from the "constituency" collection
    $lookup: {
      from: "constituency", // The collection to join
      localField: "siteInfo.ConstituencyID", // Field from the "siteInfo" documents
      foreignField: "ConstituencyID", // Field from the "constituency" collection documents
      as: "siteInfo.constituencyInfo", // The name of the new array field to add to "siteInfo"
    },
  },
  {
    // Unwinds the "constituencyInfo" array (nested within "siteInfo")
    $unwind: {
      path: "$siteInfo.constituencyInfo",
    },
  },
  {
    // Projects (selects and renames) specific fields for the final output
    $project: {
      Date_Time: 1, // Includes the Date_Time field
      Site_ID: 1, // Includes the Site_ID field
      NOxMax: "$NOx", // Renames the NOx field to NOxMax
      siteName: "$siteInfo.Name", // Extracts the site name from "siteInfo"
      constituencyName: "$siteInfo.constituencyInfo.Name", // Extracts the constituency name
      MP: "$siteInfo.constituencyInfo.MP", // Extracts the MP name from "constituencyInfo"
    },
  },
]

```

The use of $lookup and $unwind facilitated the integration of data across multiple collections, while $project, $replaceRoot and $mergeObjects were crucial for shaping the final output according to the requirements of each specific query. 
