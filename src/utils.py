from zipfile import ZipFile
import os
import json 
import logging 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# zip file function
def zip_file(source_file,output_file):

    try:
        with ZipFile(output_file,'w') as zip:
            zip.write(source_file, arcname=os.path.basename(source_file))

        logger.info(f"File {os.path.basename(source_file)} has been zipped.")
        return True
    
    except Exception as e:
        logger.error(f"An error occurred while zipping: {str(e)}")
        return False

# read object from s3 function
def read_object_from_s3(s3,bucket_name, object_key):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        return response['Body'].read()
    except Exception as e:
        logger.error(f"An error occurred while reading from S3: {str(e)}")
        return None
    