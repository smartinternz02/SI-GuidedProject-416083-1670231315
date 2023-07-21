# Importing of Libraries
import boto3
import csv

# Create client 
client  = boto3.client('rekognition',
                       aws_access_key_id = "AKIAQHCWTI4H5BCV2VXV",
                       aws_secret_access_key = "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",
                                             region_name = 'us-east-2'
                       )

def create_collection(collection_id): 

    #Create a collection
    print('Creating collection:' + collection_id)
    
    #Using inbuilt function within rekognition client
    response=client.create_collection(CollectionId=collection_id) 
    
    #Printing the collection details, save the printed output in a text file.
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')
    
def main():
    collection_id='studentsxyz' #Assign Collection ID Name
    create_collection(collection_id) # Creation of Collection ID

if __name__ == "__main__":
    main() 
