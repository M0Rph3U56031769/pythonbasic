from .datahandling import DataHandling


class ListWorkers:

    @staticmethod
    def list_workers():

        handler = DataHandling()
        inventory = handler.read_json()

        for item in inventory:
            print(inventory[item])
