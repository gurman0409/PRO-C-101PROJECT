import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(file_from , file_to):
        dbx = dropbox.Dropbox(self,access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root , filename)

                relative_path = os.path.relpath(local_path , file_from)
                dropbox_path = os.path.join(file_to , relative_path)

                with open(local_path , 'rb') as f:
                    dbx.files_upload(f.read() , dropbox_path , mode = WriteMode('overwrite'))

def main():
    access_token = 'sl.BfyMyLL9Fns4TmsE-84Krs0aaiCx7eGsL_hoe3QHeGSUJdtoreV_cgOKWweVMdBLUvPu-WH5oVR4YW95I1n4tdmsJ4UWf-z__s0e-LIW4s5GchTyhynyJ9QY8wQpdLKTSGRy1Ao'

    transferData = TransferData(access_token)

    file_from = str(input("Enter the foldder path to transfer - "))
    file_to = input("Enter the full path to upload to dropbox - ")

    transferData.upload_file(file_from , file_to)
    print("File has been moved ")

main()