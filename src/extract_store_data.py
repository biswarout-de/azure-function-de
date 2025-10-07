from azure.storage.blob import BlobServiceClient
import os
import pandas as pd
from io import StringIO

connection_string = os.getenv("az_storage_conn_str")
container_name = 'democontainergds'
blob_name = 'store_data.csv'

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)
blob_client = container_client.get_blob_client(blob_name)

blob_data = blob_client.download_blob().content_as_text()

df = pd.read_csv(StringIO(blob_data))
