##  @package wiit
#   The startpoint of the application.
#   @name	: .\pdf_mgmt.py
#   @author	: smaio
#   @date	: 03/08/2019

from src.manager.Manager import Manager
from src.util.cli_parsers import *

import argparse
import click


## The main function of wiit
#
#   @param kwargs key word arguments used by Manager
def main(**kwargs) -> None:
	manager = Manager()
	manager.start(**kwargs)

@click.group(help='command line tool for managing pdf files')
def cli():
    pass

cli.add_command(add)
cli.add_command(edit)
cli.add_command(delete)
cli.add_command(search)
cli.add_command(open_file)

if __name__ == '__main__':
    cli()
#    parser = argparse.ArgumentParser(description='A command-line python tool for managing pdf files.')
#    parser.add_argument('action',
#                        choices=['add', 'edit', 'delete', 'search', 'open'],
#                        type=str,
#                        help='The action being performed.')
#    parser.add_argument('--title',
#                        type=str,
#                        default=None,
#                        help='The name of a file. Used in the commands: \'add\', \'edit\', and \'search\'.')
#    parser.add_argument('--genre',
#                        '-g',
#                        type=str,
#                        default=None,
#                        help='The genre of a file.')
#    parser.add_argument('--id',
#                        type=int,
#                        default=None,
#                        dest='file_id',
#                        help='The ID of a file')
#    parser.add_argument('--authors',
#                        '-a',
#                        type=str,
#                        nargs='*',
#                        default=None,
#                        help='The author(s) of a file')
#    parser.add_argument('--tags',
#                        '-t',
#                        type=str,
#                        nargs='*',
#                        default=None,
#                        help='Tags to describe a file')
#    parser.add_argument('--location',
#                        '-l',
#                        type=str,
#                        default=None,
#                        help='The location of a file being added')
#    args = vars(parser.parse_args())
#    main(**args)
