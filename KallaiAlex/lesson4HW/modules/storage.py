# todo: validate the data in the json
#import json
#from jsonschema import validate
import logging
import os


class Storage:
    """
    This class is for synchronizing the data between
    the inventory in memory and the physical storage
    """

    fileName = "inventory.json"
    relativeFilePath = "storage"

    # Check if the storage file was created, if not, create it
    def __init__(self) -> None:
        # Set up logging
        self.logger = logging.Logging(False)
        # Generate the paths
        self.programFilePath = os.path.dirname(__file__)
        self.storageFolderPath = os.path.join(self.programFilePath, self.relativeFilePath)
        self.storageFilePath = os.path.join(self.programFilePath, self.relativeFilePath, self.fileName)

        # Create the file if it doesn't exist yet
        if not self.filecreated(self.storageFilePath):
            self.createfile(self.storageFilePath)

    def filecreated(self, path) -> bool:
        try:
            logging.Logging.fileexists(path)  # using static method, because it's already written
            return True
        except:
            self.logger.error(f"There was a problem with checking if {path} file exists.")
            return False

    def createfile(self, path) -> bool:
        try:
            logging.Logging.createFile(path)
            return True
        except:
            self.logger.error(f"There was a problem with creating {path} file.")
            return False

    def readfile(self) -> str:
        try:
            with open(self.storageFilePath, "r") as f:
                lines = f.readlines()
            return lines
        except:
            self.logger.error(f"There was a problem with opening the {self.storageFilePath} file for reading.")


    def writefile(self, datatowrite) -> bool:
        try:
            with open(self.storageFilePath, "w") as f:
                f.write(datatowrite)
            return True
        except:
            self.logger.error(f"There was a problem with writing to the {self.storageFilePath} file.")
            return False

def main():
    inventory = Storage()
    inventory.writefile("valami")
    print(inventory.readfile())


if __name__ == "__main__":
    main()
