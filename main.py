from dotenv import load_dotenv
import os
from setup import Setup
from app.structure.structureHandler import StructureHandler
from app.git.cloneHandler import Clone

from app.controller.controllerHandler import Controller
def main():
    load_dotenv()
    setup = Setup()
    setup.installProject()
    path = setup.getInstallPath()
    file = StructureHandler(path)
    file.createEnvironment()
    
    controller = Controller()
    controller.panel()
if __name__ == '__main__':
    main()