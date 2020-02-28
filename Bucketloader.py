# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "redditdubai-bucket-sanc"
'''
# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)

print("Bucket {} created.".format(bucket.name))
'''

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)
    for blob in blobs:
         print(blob.name)

def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    print("Blob {} deleted.".format(blob_name))


def check_delete_blobs(bucket_name, blob_name):
    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)
    for blob in blobs:
         print(blob.name)
         if blob.name==blob_name:
             print("Found the Blob",blob_name)
             bucket = storage_client.bucket(bucket_name)
             blob = bucket.blob(blob_name)
             blob.delete()   	
             print("Blob deletd")
         else:
             print("Blob Not found")




#delete_blob(bucket_name,"test")
upload_blob(bucket_name,"/home/san/Calloubroup1/versions/Reddit_data.csv","reddit_csv")
#upload_blob(bucket_name,"/home/san/Calloubroup/versions/new_schema.json","reddit_schema")
list_blobs("redditdubai-bucket-sanc")
'''
check_delete_blobs("redditdubai-bucket-sanc","test")
list_blobs("redditdubai-bucket-sanc")
'''



