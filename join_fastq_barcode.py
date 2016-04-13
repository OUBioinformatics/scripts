#!/usr/bin/env python 

# script to join two fastq files with identical read identifiers
# For example, if barcodes were seperated into a seperate fastq file, this 
# script lets you join them back with the read portion of the data

# Author: Boris Wawrik
# email : bwawrik@ou.edu

# last edited: April 13th, 2016


import argparse
import sys
import re

parser = argparse.ArgumentParser(description='command line input parameters')
parser.add_argument('--i', type=str,
                    help='input fastq file containing genes sequecnes')
parser.add_argument('--bc', type=str,
                    help='barcode file')
parser.add_argument('--o', type=str,
                    help='output file name')

def main():
  args = parser.parse_args()
  
  output_file = open(args.o, 'w')
  input_file = open (args.i, 'r')
  barcode_file = open (args.bc, "r")


  EOf = 0;

  while (EOf == 0):
    line1 = input_file.readline()
    line2 = input_file.readline()
    line3 = input_file.readline()
    line4 = input_file.readline()
    barcode_line1 = barcode_file.readline()
    barcode_line2 = barcode_file.readline()
    barcode_line3 = barcode_file.readline()
    barcode_line4 = barcode_file.readline()

    barcode_line2 = barcode_line2.rstrip('\n')
    barcode_line4 = barcode_line4.rstrip('\n')
    

    if (line1 == ""):
      EOf =1
    if (line1 != ""):
      if (line1 == barcode_line1):  
          output_file.write(line1)
          output_file.write(barcode_line2 + line2)
          output_file.write(line3)
          output_file.write(barcode_line4 + line4)

  output_file.close()
  input_file.close()
  barcode_file.close()

if __name__ == "__main__":
  sys.exit(main())
