import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_path = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if name == " main " :
    df = pd.read_csv(DATA_FILE_path)
    print(f"Rows and columns : {df.shape}")
    
 ### covert dataframe into jason format so that we can dump these record in mongodb
    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values()) # converting to json
    print(json_record[0])

# insert converted  jason into mongodb 
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    








