from zipfile import ZipFile
from config.config import config_obj

with ZipFile(config_obj.file_zip) as file:
    file.extractall()
