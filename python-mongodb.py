from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def main():
    try:
        ## Connecting with the localhost
        myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))
        print("Connection Successful", myclient)

        # list of all the databases
        # list_of_db = myclient.list_database_names()
        # print("databases available in mongodb ", list_of_db)

        ## create new database
        mydb = myclient['test']
        # print("Database Created...", mydb)
        # list_of_db = myclient.list_database_names()
        # print("databases available in mongodb after adding new database ", list_of_db)

        ## create collection
        collection = mydb['student']
        # record = {
        #     "_id": 25,
        #     "Name": "Rajnish",
        #     "Roll_number": 120,
        #     "Branch": "CSE",
        #     "Marks": 50
        # }
        #
        # record_1 = collection.insert_one(record)
        # print("Records ", record_1)
        #
        # list_of_db = myclient.list_database_names()
        # print("databases available in mongodb after adding new database ", list_of_db)
        #
        ## to insert multiple records
        #
        #
        # records = {
        #     "record1": {
        #         "_id": 17,
        #         "name": "rohan",
        #         "roll_number": 103,
        #         "branch": "cse",
        #         "marks": 45
        #     },
        #     "record2": {
        #         "_id": 18,
        #         "name": "ram",
        #         "roll_number": 104,
        #         "branch": "cse",
        #         "marks": 55
        #     }
        # }
        #
        # for record in records.values():
        #     collection.insert_one(record)
        #
        # mylist = [
        #     {
        #         "_id": 19,
        #         "name": "john",
        #         "roll_number": 103,
        #         "branch": "cse",
        #         "marks": 45
        #     },
        #     {
        #         "_id": 20,
        #         "name": "jenny",
        #         "roll_number": 108,
        #         "branch": "cse",
        #         "marks": 55
        #     },
        #     {
        #         "_id": 21,
        #         "name": "joe",
        #         "roll_number": 105,
        #         "branch": "cse",
        #         "marks": 55
        #     }
        # ]

        # collection.insert_many(mylist)

        ## to retrive the data
        # x = collection.find_one()
        # print("Record: ", x)
        #
        # all_documents = collection.find()
        # for each_record in all_documents:
        #     print("Doc : ", each_record)
        #
        ## display only limited field

        # for x in collection.find({},{"_id":0 , "Name":1, "Branch":1}):
        #     print("Only fields with 1 : ", x)

        ## operation in mongodb
        # curson = collection.find({"marks": {"$gt": 45}})
        # print("The records greater than 45: ")
        # for record in curson:
        #     print("Record %s " %record)
        #
        # curson = collection.find({"Marks": {"$lt": 45}})
        # print("The records less than 45: ")
        # for record in curson:
        #     print("Record %s " % record)

        ## search or display record in between
        # ob = collection.find({"$and": [{"Marks":{"$gt": 45}}, {"Marks": {"$lt": 55}}]})
        # print("And condition records")
        # for record in ob:
        #     print("Record: ", record)

        # ob = collection.find({"$or": [{"marks": {"$gt": 45}}, {"marks": {"$lt": 55}}]})
        # print("or condition records")
        # for record in ob:
        #     print("Record: ", record)

        ## sorting the database
        # mydoc = collection.find().sort("name")
        # for x in mydoc:
        #     print("Sorting...", x)
        #
        # print("In descending order.....................")
        # mydoc = collection.find().sort("name", -1)
        # for x in mydoc:
        #     print("Sorting...", x)

        ## update

        # filter = {'roll_number': 104}
        # newvalues = {"$set":{"marks":35}}
        # collection.update_one(filter, newvalues)
        #
        # all_documents = collection.find()
        # for each_record in all_documents:
        #     print("Doc : ", each_record)

        ##upsert
        # collection.update_many(
        #     {"marks":{"$gte": 40}},
        #     {"$set":{"passed": "True"}}
        # )
        # collection.update_many(
        #     {"marks": {"$lt": 40}},
        #     {"$set": {"passed": "False"}}
        # )
        # collection.update_many(
        #     {"Marks": {"$gt": 40}},
        #     {"$set": {"passed": "True"}}
        # )
        # collection.update_many(
        #     {"Marks": {"$lte": 40}},
        #     {"$set": {"passed": "False"}}
        # )
        # print("Records updated......")
        # cursor = collection.find()
        # for record in cursor:
        #     print(record)




    except ConnectionFailure as e:
        print("error ", e)


if __name__ == '__main__':
    main()