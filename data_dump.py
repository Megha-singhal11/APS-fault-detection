import pymongo
import pandas as pd
import json #(default library)
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = '/config/workspace/aps_failure_training_set1.csv'
DATABASE_NAME = 'aps'
COLLECTION_NAME = 'sensor'


if __name__== '__main__':
    df = pd.read_csv(DATA_FILE_PATH)
    print(f'Rows and columns: {df.shape}')
# convert dataframe to jason format so that we can dump these record in mongodb 
    df.reset_index(drop=True, inplace= True) # changes in same memory record

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

# converting json record to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    