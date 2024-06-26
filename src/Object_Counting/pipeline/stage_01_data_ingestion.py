import sys
import os

# Add the 'utils' folder to Python's module search path
# print(os.getcwd())
sys.path.append(os.path.abspath('../OBJECT_COUNTING_1/src'))
# from src.Object_Counting.config.configuration import ConfigurationManager
# from src.Object_Counting.components import DataIngestion
# from src.Object_Counting import logger

from Object_Counting.config.configuration import ConfigurationManager
from Object_Counting.components import DataIngestion
from Object_Counting import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e