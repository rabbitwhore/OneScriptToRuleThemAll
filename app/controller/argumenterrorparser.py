import argparse
import sys
class ArgumentErrorParser(argparse.ArgumentParser):
    def error(self, message):
        if "argument command" in message:
            print(f'Error: Your command does not exist')
        else:
            print(f'Error: {message}')
        sys.exit(1)