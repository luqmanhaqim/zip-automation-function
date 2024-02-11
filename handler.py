import boto3

from src.functions import zipFile



def handler():
    source_file = r"C:\python\Automation\zip automation function\test_file.json"
    output_file = r"C:\python\Automation\zip automation function\test_file.zip"

    return zipFile(source_file, output_file)

if __name__ == "__main__":
    handler()