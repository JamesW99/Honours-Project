from pymongo import MongoClient
import pymongo
# from pymongo import MongoClient

# mongodb+srv://yw2007:xuztix-wossod-4bubGu@cluster0.knj2e.mongodb.net/test
def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://yw2007:xuztix-wossod-4bubGu@cluster0.knj2e.mongodb.net/test"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient

    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['bikes']


def insert(dbName, collName, content):
    collection_name = dbName[collName]
    collection_name.insert_many(content)


    # item_0 = {}
    # collection_name.insert_one(item_0)


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # pass
    # Get the database
    # dbname = get_database()
    item_1 = {
        "model_name": "Blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340,
        "category": "kitchen appliance",
        "link": "U1IT00001"
    }

    item_2 = {
        "Model Name": "Egg",
        "size": "food",
        "quantity": 12,
        "price": 36,
        "item_description": "brown country eggs",
        "link": "U1IT00002"
    }
    insert(get_database(), "geometry", [item_1, item_2])

