from pymongo import MongoClient

mongoclient = MongoClient("mongodb://%s:%s@127.0.0.1" %("admin","admin"))
mydb = mongoclient['test']
mycollection = mydb['aggregrate_table']

profiles =[
    {"user":"ram" ,"title":"Python"},
    {"user":"raj" ,"title":"Javascript"},
    {"user":"ram" ,"title":"C++"},
    {"user":"john" ,"title":"MongoDB"},
    {"user":"rohan" ,"title":"Perl"}
]

mycollection.insert_many(profiles)
agg_result = mycollection.aggregate(
    [
        {
            "$group":
            {
                "_id" : "$title",
                "Occurence": {"$sum": 1}

            }
        }
    ]
)

print("Result")
for i in agg_result:
    print(i)