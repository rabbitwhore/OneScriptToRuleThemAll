import os
from dotenv import dotenv_values, set_key
class Setup:
    def __init__(self):
        self.path = os.environ.get('DOCUMENT_PATH')
    def getInstallPath(self):
        return self.path
    def installProject(self):
        if self.path:
            print('Project is installed')
        else:
            document_path = input('Enter path to install this project: ')
            self.path = document_path
            env_vars = dotenv_values()
            print(env_vars)
            set_key('.env', 'DOCUMENT_PATH', document_path)