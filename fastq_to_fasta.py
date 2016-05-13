#!/usr/bin/env python

# script to convert fastq to fasta file

# Author: Boris Wawrik
# email : bwawrik@ou.edu

# last edited: May 12th, 2016

import argparse
import sys
import os

parser = argparse.ArgumentParser(description='command line input parameters')
parser.add_argument('--i', type=str,
                    help='input fasta file containing genes sequecnes')
parser.add_argument('--o', type=str,
                    help='output file name')


def main():
    args = parser.parse_args()

    file_a = open(args.i, 'r')
    file_b = open(args.o, 'w')

    end_reached = 0

    while end_reached == 0:
          line_1 = file_a.readline()
          line_2 = file_a.readline()
          line_3 = file_a.readline()
          line_4 = file_a.readline()

          line_1 = ">" +  line_1[1:]

          file_b.write (line_1)
          file_b.write (line_2)
          if line_1 =="":
            end_reached =1
    file_b.close()
    file_a.close()


if __name__ == "__main__":
    sys.exit(main())

