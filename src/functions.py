from zipfile import ZipFile
import os



source_file = "C:\python\Automation\zip automation function\test_file.json"
output_file= "C:\python\Automation\zip automation function\test_file.zip"



def zipFile(source_file,output_file):

    try:
        with ZipFile(output_file,'w') as zip:
            zip.write(source_file, arcname=os.path.basename(source_file))

        print(f"file {os.path.basename(source_file)} has been zipped ")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

            