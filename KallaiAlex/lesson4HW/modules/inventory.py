import logging
import storage


class Inventory:
    """"
    This class is for functions that manage the inventory
    """

    def __init__(self):
        # Set up logging
        self.logger = logging.Logging(True)

        # Set up internal storage variable
        self.inventoryDict: dict = {}

        # Set up file storage
        self.store = storage.Storage()

    def additem(self, name, amount):
        self.inventoryDict.update({str(name):int(amount)})
        self.logger.log(f"added {name} record with {amount} amount")
        self.syncstorage()

    def checkoutitem(self, name: str, amount: int):
        if name in self.inventoryDict:
            self.inventoryDict[name] -= amount
            self.logger.log(f"'{name}' record was decreased by {amount} in the inventory.")
            self.syncstorage()
        else:
            self.logger.log(f"'The inventory does not contain {name}' record!")

    def changeitem(self, name: str, amount: int):
        if name in self.inventoryDict:
            self.inventoryDict[name] = amount
            self.logger.log(f"'{name}' record was changed to {amount} in the inventory.")
            self.syncstorage()
        else:
            self.logger.log(f"'The inventory does not contain {name}' record!")

    def listitems(self):
        print("\nThe items in the inventory are:")
        for listItem in self.inventoryDict:
            print(f"\t{listItem} -- {self.inventoryDict[listItem]}")
        print("END\n")
        pass

    def deleteitem(self, name):
        if name in self.inventoryDict:
            self.inventoryDict.pop(name)
            self.logger.log(f"'{name}' record was deleted from the inventory.")
            self.syncstorage()
        else:
            self.logger.log(f"'{name}' record was NOT deleted from the inventory.")

    def syncstorage(self) -> bool:
        try:
            self.store.writefile(self.inventoryDict)
        except:
            self.logger.error("Syncing the class variable with the storage file was unsuccessful.")
