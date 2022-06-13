import datetime
from .auth import Authentication
from .log_handler import LogHandler


class Logger:
    log_data = list()
    log_handler = LogHandler()
    operation_logs = log_handler.read_operation_log_file()
    exception_logs = log_handler.read_exception_log_file()
    user = Authentication.get_username()

    def log_new_record(self, product_name, product_value):
        self.log_data = [
            {"username": self.user},
            {"operation": "new record"},
            {"values": {product_name: product_value}}
        ]

        date_time = str(datetime.datetime.now())
        self.operation_logs[date_time] = self.log_data
        self.log_handler.write_op_log_file(self.operation_logs)
    def log_update(self, product_name, product_value, old_values):
        self.log_data = [
            {"username": self.user},
            {"operation": "update record"},
            {"old_values": old_values},
            {"new values": {product_name: product_value}
             }
        ]
        date_time = str(datetime.datetime.now())
        self.operation_logs[date_time] = self.log_data
        self.log_handler.write_op_log_file(self.operation_logs)

    def log_delete_record_successful(self, product_name, product_value):

        self.log_data = [
            {"username": self.user},
            {"operation": "delete record"},
            {"success": True},
            {"deleted values": {product_name: product_value}
             }
        ]

        date_time = str(datetime.datetime.now())
        self.operation_logs[date_time] = self.log_data
        self.log_handler.write_op_log_file(self.operation_logs)

    def log_delete_record_failure(self):
        self.log_data = [
            {"username": self.user},
            {"operation": "delete record"},
            {"success": False}
        ]
        date_time = str(datetime.datetime.now())
        self.operation_logs[date_time] = self.log_data
        self.log_handler.write_op_log_file(self.operation_logs)

    def log_delete_key_error(self, error):
        self.log_data = [
            {"exception": str(error)}
            ]
        date_time = str(datetime.datetime.now())
        try:
            self.exception_logs[date_time] = self.log_data
        except:
            pass
        self.log_handler.write_ex_log_file(self.exception_logs)


