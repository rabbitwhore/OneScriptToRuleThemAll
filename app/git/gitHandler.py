import os
from dotenv import dotenv_values, set_key
import subprocess
class Git:
    def __init__(self):
        self.folder_path = os.environ.get('DOCUMENT_PROJECT_PATH')
        
    def configureGit(self):
        config = dotenv_values()
        prodFrontend = config.get('DOCUMENT_PROJECT_PRODUCTION_URL_FRONTEND', '')
        prodFrontend = prodFrontend or input('Enter git url for production frontend: ')
        prodBackend = config.get('DOCUMENT_PROJECT_PRODUCTION_URL_BACKEND', '')
        prodBackend = prodBackend or input('Enter git url for production backend: ')
        devFrontend = config.get('DOCUMENT_PROJECT_DEVELOPMENT_URL_FRONTEND', '')
        devFrontend = devFrontend or input('Enter git url for development frontend: ')
        devBackend = config.get('DOCUMENT_PROJECT_DEVELOPMENT_URL_BACKEND', '')
        devBackend = devBackend or input('Enter git url for development backend: ')
        pathToEnv = os.path.abspath('.env')
        try:
            if not config.get('DOCUMENT_PROJECT_PRODUCTION_URL_FRONTEND', '') and prodFrontend:
                set_key(pathToEnv, 'DOCUMENT_PROJECT_PRODUCTION_URL_FRONTEND', prodFrontend)
            if not config.get('DOCUMENT_PROJECT_PRODUCTION_URL_BACKEND', '') and prodBackend:
                set_key(pathToEnv, 'DOCUMENT_PROJECT_PRODUCTION_URL_BACKEND', prodBackend)
            if not config.get('DOCUMENT_PROJECT_DEVELOPMENT_URL_FRONTEND', '') and devFrontend:
                set_key(pathToEnv, 'DOCUMENT_PROJECT_DEVELOPMENT_URL_FRONTEND', devFrontend)
            if not config.get('DOCUMENT_PROJECT_DEVELOPMENT_URL_BACKEND', '') and devBackend:
                set_key(pathToEnv, 'DOCUMENT_PROJECT_DEVELOPMENT_URL_BACKEND', devBackend)
            print("Config for git is set")
        except FileNotFoundError:
            print("Error: .env file not found")
    
    def gitAdd(self, args):
        result = subprocess.run(['git', 'add', '.'])
        if result.returncode == 0:
            print('Add was successful')
        else:
            print(f"Add failed, error: {result.returncode}")
    
    def gitCommit(self, args, commit):
        if commit == "update":
            message = commit
        else: 
            message = input('Commit message: ')
        
        result = subprocess.run(['git', 'commit', '-m', message])
        if result.returncode == 0:
            print('Commit was successful')
        else:
            print(f"Commit failed, error: {result.returncode}")
    def gitPush(self, args):
        result = subprocess.run(['git', 'push'])
        if result.returncode == 0:
            print('Push was successful')
        else:
            print(f"Push failed, error: {result.returncode}")
    def gitClone(self):
        url = input('Clone url: ')
        result = subprocess.run(['git', 'clone', url])
        if result.returncode == 0:
            print('Clone was successful')
        else:
            print(f"Clone failed, error: {result.returncode}")
    def gitRunEverything(self, args):
        self.gitAdd(args)
        self.gitCommit(args, "update")
        self.gitPush(args)