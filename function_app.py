import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="landing-zn",
                               connection="azuredemosagds_STORAGE") 
def blobTriggerFuncDemo(myblob: func.InputStream):
    logging.info(f" Custom Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Content: {myblob}")

