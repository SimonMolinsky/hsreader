import os
import yaml
from hsreader.download import download
from hsreader.show import show

__version__ = '0.1.0'

# Prepare output URL and FILENAME
file_path = os.path.realpath(__file__)
yml_file = os.path.normpath(os.path.join(file_path, '../config.yml'))
with open(yml_file, 'r') as yml:
    settings = yaml.safe_load(yml)

URL = settings['url']
FILENAME = settings['filename']
