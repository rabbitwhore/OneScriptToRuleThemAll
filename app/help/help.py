
class HelpAction():
    def __init__(self):
        self.usage =  """usage: Danztool 
    
    description: 
        Danztool is a tool for danzpunkten
    
    arguments:
        -h, --help shows help message
        -git init project, configure urls for git
        -git add, runs git add .
        -git commit, runs git commit -m "", with a message
        -git push, runs git push
            """ 
    def help(self, args):
        print(self.usage)