
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://theharism:zFgWhlb6z612sLzZ@cyberbasket.cpurxpb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def store_preferences(processed_data, collection_name):
    # Get a reference to the specified collection in the database
    db = client['mydatabase']
    collection = db[collection_name]
    
    result = collection.insert_one(processed_data)
    
    print(f"Inserted document with ID: {result.inserted_id}")