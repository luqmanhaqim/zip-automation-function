import boto3
import os
from src.functions import event_handler


def handler(event, context):
    try:
        s3_client = boto3.client('s3')
        event_handler(s3_client, event)
        return "Function has been executed"
    
    except Exception as e:

        print(f"An error occurred: {str(e)}")
        return "An error occurred during function execution"
