# imports
from pathlib import Path
import argparse

from pymongo import MongoClient
import pandas as pd


def flags() -> dict:
    
    # creating flags
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', '-u', type=str, default=None, help='Username')
    parser.add_argument('--password', '-pw', '-p', type=str, default=None, help='User password')
    
    args = parser.parse_args()
    return vars(args)


if __name__=='__main__':
    
    # init inputs
    user_flags = flags()

    assert user_flags['user'] is not None, 'Missing username field identified. [--user|-u]=None'
    assert user_flags['password'] is not None, 'Missing passoword field identified. [--password|-pw|-p]=None'
    
    csv_file_path = Path('data/raw/chatbot_dataset.csv')
    if not csv_file_path.exists():
    
        # checking connection
        client = MongoClient(host=f'mongodb+srv://{user_flags["user"]}:{user_flags["password"]}@chatbot-cluster.bhc8uij.mongodb.net/')
        try:
            client.admin.command(command='ping')
            print('\033[1;32mConnected\033[0m')
        except Exception as error:
            print(f'\033[1;31mFailed\033[0m : {error}')
        
        # collecting data from
        # database
        db = client.get_database(name='ChatBot-DB')
        col = db.get_collection(name='raw-dataset')
        content = col.find()
        
        df = {'question': [], 'answer': []}
        for docs in content:
            for keys in df:
                try:
                    df[keys].append(docs[keys])
                except Exception as error:
                    print(f'Ignoring document: {error}')
        df = pd.DataFrame(data=df)
        
        # generating .csv file
        csv_file_path.parent.mkdir(exist_ok=True)
        df.to_csv(path_or_buf='data/raw/chatbot_dataset.csv')
    else:
        print('Dataset already exists.')
