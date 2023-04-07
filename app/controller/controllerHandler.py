
from ..git.gitHandler import Git
from ..structure.structureHandler import StructureHandler
from ..help.help import HelpAction
from ..controller.argumenterrorparser import ArgumentErrorParser
class Controller:
    def __init__(self):
        self.parser = ArgumentErrorParser(add_help=False)

        subparsers = self.parser.add_subparsers(dest='command')

        git_parser = subparsers.add_parser('git', add_help=False)
        git_subparsers = git_parser.add_subparsers(dest='subcommand')

        git_init_parser = git_subparsers.add_parser('init project', add_help=False)
        git_init_parser.set_defaults(func=Git().configureGit)

        git_add_parser = git_subparsers.add_parser('add', add_help=False)
        git_add_parser.set_defaults(func=lambda args: Git().gitAdd(args))

        git_commit_parser = git_subparsers.add_parser('commit', add_help=False)
        git_commit_parser.set_defaults(func=lambda args: Git().gitCommit(args, ""))

        git_push_parser = git_subparsers.add_parser('push', add_help=False)
        git_push_parser.set_defaults(func=lambda args: Git().gitPush(args))

        git_run_everything_parser = git_subparsers.add_parser('e', add_help=False)
        git_run_everything_parser.set_defaults(func=lambda args: Git().gitRunEverything(args))

        project_parser = subparsers.add_parser('project', add_help=False)
        project_parser.set_defaults(func=lambda args: StructureHandler("wtf").pt(args))

        question_mark_help_parser = subparsers.add_parser('?', add_help=False)
        question_mark_help_parser.set_defaults(func=lambda args: HelpAction().help(args))

        self.parser.add_argument('--help', '-h', action='store_true')
        
        self.args, self.unknown = self.parser.parse_known_args()
        
    def panel(self):
        if self.args:
            if self.args.command:
                if hasattr(self.args, 'func'):
                    self.args.func(self.args)
                else:
                    print(f'No function defined for subcommand "{self.args.command}"')
            elif self.args.help:
                HelpAction().help(self.args)
            else:
                print("Command not defined")
        else:
            print('No command')