from pymongo import MongoClient

myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))
mydatabase = myclient['test']
# mycollection = mydatabase['aggpipeline']

# sample_data = [{"x": 1, "tags": ["dog", "cat"]},
#                {"x": 2, "tags": ["cat"]},
#                {"x": 3, "tags": ["mouse", "cat", "dog"]},
#                {"x": 4, "tags": []}
#                ]
# result = mycollection.insert_many(sample_data)

from bson.son import SON

# pipeline = [
#     {
#         "$unwind": "$tags"
#     },
#     {
#         "$group": {"_id": "$tags", "count": {"$sum": 1}}
#     },
#     {
#         "$sort": SON([("_id", -1), ("tags", -1)])
#     }
# ]

mycollection = mydatabase['practice']
# sample_data = [
#     {"abcd": 1, "efgh": {"ijkl": [1, 2, 3], "mnop": [7, 8, 9]}},
#     {"abcd": 2, "efgh": {"ijkl": [3, 4, 5], "mnop": [1, 9, 5]}},
#     {"abcd": 3, "efgh": {"ijkl": [2, 6, 3], "mnop": [6, 7, 2]}},
#     {"abcd": 4, "efgh": {"ijkl": [1, 5, 6], "mnop": [9, 8, 7]}},
#     {"abcd": 5, "efgh": {"ijkl": [6, 1, 2], "mnop": [9, 6, 5]}},
#
# ]
#
# result = mycollection.insert_many(sample_data)

pipeline = [
    {
        "$unwind": "$ijkl"
    },
    {
        "$group": {"_id": "$ijkl", "count": {"$sum": 1}}
    },
    {
        "$sort": SON([("_id", -1)])
    }
]

import pprint
pprint.pprint((list(mycollection.aggregate(pipeline))))
