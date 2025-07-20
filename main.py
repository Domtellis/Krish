import sys
from src.logging import logger
from src.exception.proj_exception import Project_Exception
from src.components.dataingestion import DataIngestion
from src.components.dataingestion import DataIngestionArtifact
from src.components.dataingestion import DataIngestionConfig


#logger.logging.info("Hello test log")

#try:
#    print(1/0)
#except Exception as e:
#    raise Project_Exception(str(e),sys)    


##### For DataIngestion, Validation ,et al

if __name__ == "__main__":
    
    data_ingestion = DataIngestion()
    train_data, test_data = data_ingestion.initiate_data_ingestion()
    
    