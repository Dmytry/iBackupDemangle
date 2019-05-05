#!/usr/bin/python3
# Copyright (c) 2019, Dmytry Lavrov
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of  nor the names of its contributors may be used to
#    endorse or promote products derived from this software without specific
#    prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

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
