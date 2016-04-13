#!/usr/bin/env python 

# This script splits a fasta file into several smaller files 

# Author: Boris Wawrik
# email : bwawrik@ou.edu

# last edited: April 13th, 2016

import argparse
import sys
import os
import requests

parser = argparse.ArgumentParser(description='command line input parameters')
parser.add_argument('--i', type=str,
                    help='input fasta file containing genes sequecnes')
parser.add_argument('--o', type=str,
                    help='output file name')
parser.add_argument('--n', type=long,
                    help='number of sequences in each sub-file')



def main():
    args = parser.parse_args()
    infile = args.i
    outfile = args.o
    n_seqs = args.n
    
    path = os.path.dirname(infile)
    
    frag = 0
    end_reached =0
    
    file_a = open(infile, 'r')    
    
    while end_reached == 0:
    
      output_file_name = path + '/' + outfile + '.' + str(frag)
      file_b = open(output_file_name, 'w')    
      position =1
 
      while position < n_seqs:
      
          line_1 = file_a.readline()
          line_2 = file_a.readline()
          file_b.write (line_1)
          file_b.write (line_2)
          if line_1 =="":
            end_reached =1
          position = position +1

      frag = frag + 1  
      file_b.close()
 
    file_a.close()
    
    
if __name__ == "__main__":
    sys.exit(main())
