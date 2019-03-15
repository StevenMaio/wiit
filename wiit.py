'''
	The startpoint of the application.

	@name	: .\pdf_mgmt.py
	@author	: smaio
	@date	: 03/08/2019
'''
from src.manager.Manager import Manager

import argparse
import sqlite3


def main(**kwargs):
	manager = Manager()
	manager.start(**kwargs)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Bootie')
	parser.add_argument('action',
			choices=['add', 'edit', 'delete', 'search', 'open'],
			type=str,
			help='The action being performed.')
	parser.add_argument('--title',
			type=str,
			help='The file being added to the database.')
	parser.add_argument('--genre',
			'-g',
			type=str,
			help='The genre of the file being added.')
	parser.add_argument('--id',
			type=int,
			default=None,
			dest='file_id',
			help='The ID of the file in question')
	parser.add_argument('--authors',
			'-a',
			type=str,
			nargs='*',
			default=None,
			help='The author of the book')
	parser.add_argument('--tags',
			'-t',
			type=str,
			nargs='*',
			default=None,
			help='Tags to describe the file')
	parser.add_argument('--location',
			'-l',
			type=str,
			default=None,
			help='The location of the file being added')
	args = vars(parser.parse_args())
	print(args)
	main(**args)
