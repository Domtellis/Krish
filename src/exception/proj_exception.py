import sys
from src.logging import logger

logger.logging.info("An exception has occured")

class Project_Exception(Exception):
    def __init__(self,error_message,error_details:sys):
        ## new code
        super().__init__(error_message)
        self.error_message = error_message
        
        # Extract traceback info safely
        _, _, exc_tb = error_details.exc_info()
        
        #self.lineno = exc_tb.tb_lineno
        #self.file_name=exc_tb.tb_frame.f_code.co_filename
        
        self.lineno = exc_tb.tb_lineno if exc_tb else None
        self.file_name=exc_tb.tb_frame.f_code.co_filename if exc_tb else None
        
        # new code
        # logger.error(self.__str__())  # Log the error immediately
        
    def __str__(self):
        #return f"Error occurred in python script name[{0})] line number [{1}] error message [{2}] "
        return f"Error occurred in python script [{self.file_name}] at line number [{self.lineno}] with error message [{self.error_message}]"
