import os
import urllib.request as request
import zipfile
from pathlib import Path

from text_summarization.entity import DataIngestionConfig
from text_summarization.logging import logger
from text_summarization.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        local_data_file: str
        Downloads the zip file into the local data directory
        Function returns None
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file)
            
            logger.info(f"{filename} downloaded! With the following info: \n{headers}")
        
        else:
            logger.info(f"Similar File already exists")  


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)