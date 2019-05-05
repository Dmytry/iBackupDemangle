#!/usr/bin/python3
# Copyright (C) Dmytry Lavrov, 2019

import sys
import argparse
import sqlite3
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument("--input", help="Input folder")
parser.add_argument("--output", help="Output folder")
args=parser.parse_args();
input_path=Path(args.input);
output_path=Path(args.output);

conn=sqlite3.connect(str(input_path / 'Manifest.db'));
c=conn.cursor();
files=c.execute('SELECT fileID, domain, relativePath FROM FILES');
for row in files :
	#print(row)
	input_file=input_path / row[0][:2] / row[0]
	#print(input_file)
	output_file = output_path / row[1] / row[2]
	print(output_file)
	try:
		output_file.parent.mkdir(parents=True, exist_ok=True)
	except:
		print("Failed to make folder")
	if input_file.exists() :
		if output_file.exists() :
			print("Output file already exists!")
		else:
			try:
				input_file.rename(output_file)
				print(f'mv "{input_file}" "{output_file}"')
			except:
				print("Failed to rename")
