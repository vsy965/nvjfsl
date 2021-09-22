from pymongo import MongoClient

def main():
    myclient = MongoClient("mongodb://%s:%s@127.0.0.1" %('admin', 'admin'))
    print("Connection Successfull...", myclient)
    mydb = myclient.test
    collection = mydb['Employee']
    # while(True):
    #     print("---Employee Details---")
    #     empid = int(input("Enter Employee ID: "))
    #     name = input("Enter Name: ")
    #     age = int(input("Enter Age: "))
    #     gender = input("Enter Gender: ")
    #     salary = int(input("Enter Salary: "))
    #     loop = int(input("Enter more details Yes:1 NO:0 :"))
    #     record = {
    #         "_id" : empid,
    #         "name" : name,
    #         "age" : age,
    #         "gender": gender,
    #         "salary" : salary
    #     }
    #     collection.insert_one(record)
    #     if loop == 0:
    #         break
    #
    # all_rec = collection.find()
    # for rec in all_rec:
    #     print(rec)

    print("Enter finding criteria... \n1. ID \n2. Name\n3. Age \n4. Gender")






if __name__ =="__main__":
    main()
