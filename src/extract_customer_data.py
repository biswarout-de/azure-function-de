from azure.storage.blob import BlobServiceClient
import pandas as pd
import os
from io import StringIO

connection_string = os.getenv("az_storage_conn_str")
conatiner_name = 'democontainergds'
blob_name = 'customer_subscription.csv'

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(conatiner_name)
blob_client = container_client.get_blob_client(blob_name)

blob_data = blob_client.download_blob().content_as_text()

df = pd.read_csv(StringIO(blob_data))

print(df)