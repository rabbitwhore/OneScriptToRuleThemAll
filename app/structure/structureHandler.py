import os
from dotenv import dotenv_values, set_key

class StructureHandler:
    def __init__(self, document_path):
        self.document_path = os.environ.get('DOCUMENT_PATH') if os.environ.get('DOCUMENT_PATH') else document_path 
    def createEnvironment(self):
        if os.environ.get('DOCUMENT_PROJECT_DEVELOPMENT_PATH') and os.environ.get('DOCUMENT_PROJECT_PRODUCTION_PATH'):
            print('Environment is already defined')
        else: 
            path = input("Create your project folder: ")
            if "/" not in path:
                folder_path = self.document_path + "/" + path
                if os.path.exists(folder_path):
                    print(f"The folder '{folder_path}' already exists.")
                else:
                    os.makedirs(folder_path)
                    production_path = folder_path + "/production"
                    development_path = folder_path + "/development"
                    os.makedirs(production_path)
                    os.makedirs(development_path)
                    pathToEnv = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/.env'
                    print(f"path to env '{pathToEnv}'")
                    set_key(pathToEnv, 'DOCUMENT_PROJECT_PATH', folder_path)
                    set_key(pathToEnv, 'DOCUMENT_PROJECT_DEVELOPMENT_PATH', development_path)
                    set_key(pathToEnv, 'DOCUMENT_PROJECT_PRODUCTION_PATH', production_path)

                    print(f"The folder '{production_path}' and '{development_path}' has been created and are saved inside your .env file.")
            else:
                print(f"You can't create subfolders, check your path: {path}")
    def pt(self, args):
        print("wtf")