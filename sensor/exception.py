import sys


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error Occured. Python Script: [{0}], Line Number: [{1}], Error Message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class SensorException(Exception):
    def __init__(self, error_message, error_detail:sys):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
