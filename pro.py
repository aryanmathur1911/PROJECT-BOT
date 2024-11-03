import os
import shutil
class DocumentManager:
    def __init__(self,base_directory='documents'):
        self.base_dictionary=base_directory
        self.setup_folders()  #used to create necessary folders on initialisation of class
    

    def setup_folders(self):   #if base directory is not there , it creates it.
        if not os.path.exists(self.base_directory):
            os.markedirs(self.base_directory) #create the base directory
    

        self.folders = {                           #dictionary 
            'images' : os.path.join(self.base_directory,'images'),
            'setups' : os.path.join(self.base_directory,'setups'),
            'texts' : os.path.join(self.base_directory,'texts'),
        }
        for folder in self.folder.values():
            if not os.path.exists(folder):
                os.makedirs(folder)
    

    def add_document(self, filename):
        file_extension = filename.split('.')[-1].lower()

        if file_extension in ['jpg','jpeg','png','gif']:
            destination_path=os.path.join(self.folders['images'],filename)
            shutil.move(filename,destination_path)
            print(f"Image file '{filename}' moved to images folder. ")
        
        elif file_extension in ['exe','msi']:
            destination_path=os.path.join(self.folders['setups'],filename)
            shutil.move(filename,destination_path)
            print(f"Setup file '{filename}' moved to setups folder. ")
        elif file_extension in ['txt','doc','docx']:
            destination_path=os.path.join(self.folders['texts'],filename)
            shutil.move(filename,destination_path)
            print(f"Text file '{filename}' moved to texts folder. ")
        else:
            print(f"File type '{file_extension}' not supported for automatic segregation")


    def list_documents(self):
        for folder_name,folder_path in self.folders.items():
            print(f"{folder_name.capitalize()} Documents :")
            docs = os.listdir(folder_path)
            if  docs:
                for doc in docs:
                    print(f"- {doc}")
                else:
                    print("No documents found")


    def delete_document(self,filename):
        for folder in self.folders.values():
            filepath=os.path.join(folder,filename)                
            if os.path.exists(filename):
                os.remove(filepath)
                print(f"Document '{filename}' deleted from {folder}.")
                return
            else:
                print(f"Document '{filename}' not found.")


    def read_document(self,filename):           #to read content of file
        filepath=os.path(self.folders['texts'],filename)            
        
        try:
            with open(filepath,'r') as f:
                content=f.read() 
            print(f"Content of '{filename}' : /n{content}")
        except FileNotFoundError:
            print(f"Document '{filename}' not found.")


def main():
    manager = DocumentManager()

    while(True):
        print("\nDocument Manager")
        print("1 . Add document")
        print("2 . List documents")
        print("3 . Delete document")
        print("4 . Read document")
        print("5 . Exit")

        choice=input("Choose an option : ")

        if(choice == '1'):
            filename=input("Enter filename with extension : ")
            if os.path.exists(filename):
                manager.add_document(filename)
            else:
                print(f"File '{filename}' doesnot exists.")
        
        elif choice == '2':
            manager.list_documents()
        elif choice == '3':
            filename=input("Enter filename to delete : ")
            manager.delete_document(filename)
        elif choice == '4':
            filename=input("Enter filename to read : ")
            manager.read_document(filename)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()
            




        



    

