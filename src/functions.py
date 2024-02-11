from zipfile import ZipFile
import os
import json 
import logging 
import datetime
import dateutil.tz

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def zip_file(source_file,output_file):

    try:
        with ZipFile(output_file,'w') as zip:
            zip.write(source_file, arcname=os.path.basename(source_file))

        logger.info(f"File {os.path.basename(source_file)} has been zipped.")
        return True
    
    except Exception as e:
        logger.error(f"An error occurred while zipping: {str(e)}")
        return False

def read_object_from_s3(s3,bucket_name, object_key):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        return response['Body'].read()
    except Exception as e:
        logger.error(f"An error occurred while reading from S3: {str(e)}")
        return None

def event_handler(s3,event):

    

    for record in event['Records']:
        # Get bucket and key from the event
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']

        if object_key.endswith('.json'):
            # Read the JSON object from S3
            json_data = read_object_from_s3(s3,bucket_name, object_key)
            if json_data:
                # Write the JSON data to a temporary file

                temp_file = '/tmp/' + os.path.basename(object_key)
                with open(temp_file, 'wb') as f:
                    f.write(json_data)

                temp_file_without_extension = os.path.splitext(os.path.basename(object_key))[0]
                # Get current timestamp
                malaysia = dateutil.tz.gettz('Asia/Kuala_Lumpur')
                timestamp = datetime.datetime.now(tz=malaysia).strftime("%Y%m%d%H%M%S")
                # Zip Json file
                zip_output_file = f"/tmp/{temp_file_without_extension}_{timestamp}.zip"
                if zip_file(temp_file, zip_output_file):
                    # Upload the zip file back to the bucket
                    zip_key = f'{temp_file_without_extension}_{timestamp}' + '.zip'
                    try:
                        s3.upload_file(zip_output_file, bucket_name, zip_key)
                        logger.info(f"File {zip_key} uploaded successfully!")
                    except Exception as e:
                        logger.error(f"An error occurred while uploading the zip file: {str(e)}")

                    # Delete the original JSON file
                    try:
                        s3.delete_object(Bucket=bucket_name, Key=object_key)
                        logger.info(f"File {object_key} deleted successfully!")
                    except Exception as e:
                        logger.error(f"An error occurred while deleting the original JSON file: {str(e)}")

                    # Clean up temporary files
                    os.remove(temp_file)
                    os.remove(zip_output_file)

    return {
        'statusCode': 200,
        'body': json.dumps('Files processed successfully!')
    }


            

