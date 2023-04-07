import os
import subprocess
from dotenv import dotenv_values, set_key
class Clone:
    def __init__(self):
        self.folder_path = os.environ.get('DOCUMENT_PROJECT_PATH')
    def cloneProject(self):
        config = dotenv_values(".env")
        projectType = input('Choose a project type, either production or development: ')
        if 'dev' in projectType:
            path = config['DOCUMENT_PROJECT_DEVELOPMENT_PATH']
            print(f"Cloning folder '{path}'")
            os.chdir(path)
            print(f"The current working directory is now {os.getcwd()}")
            url = input('get url to clone project: ')
            subprocess.run(['git', 'clone', url])
        if 'prod' in projectType:
            path = config['DOCUMENT_PROJECT_PRODUCTION_PATH']
            print(f"Cloning folder '{path}'")
            os.chdir(path)
            print(f"The current working directory is now {os.getcwd()}")
            url = input('get url to clone project: ')
            subprocess.run(['git', 'clone', url])