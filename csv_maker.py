# make a csv from text

import csv
import sys

def main():
	if len(sys.argv) < 3:	
		print 'USAGE: csv_maker.py source_data output_file'
	filename = sys.argv[1]
	output = sys.argv[2]
	in_txt = csv.reader(open(filename, "rb"), delimiter = ' ')
	out_csv = csv.writer(open(output, 'wb'))
	out_csv.writerows(in_txt)

if __name__ == '__main__':
	main()