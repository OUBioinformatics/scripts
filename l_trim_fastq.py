#!/usr/bin/env python 

# This script trims fastq sequences on the 5'-end if they contain a specific sequence
# We commonly use this to trim illimina reads so they start with a specific primer sequence

# Author: Boris Wawrik
# email : bwawrik@ou.edu

# last edited: April 13th, 2016

import argparse
import sys
import re

parser = argparse.ArgumentParser(description='command line input parameters')
parser.add_argument('--i', type=str,
                    help='input fastq file containing genes sequecnes')
parser.add_argument('--p', type=str,
                    help='primer sequence to trim to')
parser.add_argument('--o', type=str,
                    help='output file name')

def parse_degeneracy(seq):
  seq = seq.replace("N","[ATGC]")
  seq = seq.replace("R","[AG]")
  seq = seq.replace("Y","[TC]")
  seq = seq.replace("S","[GC]")
  seq = seq.replace("W","[AT]")
  seq = seq.replace("K","[TG]")
  seq = seq.replace("M","[AC]")
  seq = seq.replace("B","[TGC]")
  seq = seq.replace("D","[ATG]")
  seq = seq.replace("H","[ATC]")
  seq = seq.replace("V","[AGC]")
  return seq

def main():
    args = parser.parse_args()
    
    output_file = open(args.o, 'w')
    input_file = open (args.i, 'r')
 
    EOf = 0;
    
    while (EOf == 0):
      line1 = input_file.readline()
      line2 = input_file.readline()
      line3 = input_file.readline()
      line4 = input_file.readline()
      
      if (line1 == ""):
        EOf =1
      if (line1 !=""):
        location = -1
        p = re.compile(parse_degeneracy(args.p))
        for m in p.finditer(line2):
          location = (m.start())
          break
        if (location == -1):
          output_file.write (line1)
          output_file.write (line2)
          output_file.write (line3)
          output_file.write (line4)
        if (location != -1):
          output_file.write (line1)
          output_file.write (line2[location:])
          output_file.write (line3)
          output_file.write (line4[location:])
          
    output_file.close()
    input_file.close()
if __name__ == "__main__":
  sys.exit(main())
