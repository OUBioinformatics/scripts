#!/usr/bin/env python 


# This script uses bowtie2 to map reads onto a fasta file of contigs or genes.
# It requires bowtie2 and samtools. The easiest way to deploy is to use my docker
# repository-- pull 'bwawrik/bioinformatics:latest' to run

# Author: Boris Wawrik
# email : bwawrik@ou.edu

# last edited: April 13th, 2016



import argparse
import sys
import os

parser = argparse.ArgumentParser(description='command line input parameters')
parser.add_argument('--f_reads', type=str,
                   help='file containing forward reads')
parser.add_argument('--r_reads', type=str,
                   help='file containing reverse reads')
parser.add_argument('--t', type=str,
                   help='file containig contigs to which reads should be mapped')


def main():
    args = parser.parse_args()
    f_reads = args.f_reads
    r_reads = args.r_reads
    contigs = args.t
    path = os.path.dirname(contigs)
    os.system ("mkdir " + path + '/bowtie2')
    os.system ("cp " + contigs + " " + path + '/bowtie2/' + os.path.basename(contigs))
    
    build_command = "bowtie2-build " + contigs + " " + path + '/bowtie2/' + os.path.basename(contigs)
    os.system (build_command)

    sam_file = path + '/bowtie2/' + os.path.splitext(os.path.basename(contigs))[0] + '.sam'
    bam_file = path + '/bowtie2/' + os.path.splitext(os.path.basename(contigs))[0] + '.bam'
    sorted_file = path + '/bowtie2/' + os.path.splitext(os.path.basename(contigs))[0] + '.sorted'

    build_command = "bowtie2 -x " + path + '/bowtie2/' + os.path.basename(contigs) + ' -1 ' + f_reads + ' -2 ' + r_reads + ' -S ' + sam_file
    os.system (build_command)
    
    build_command = "samtools view -b -S -o " + bam_file + ' ' + sam_file
    os.system (build_command)
    
    build_command = "samtools sort " + bam_file + ' ' + sorted_file
    os.system (build_command)
 
    build_command = "samtools index " + sorted_file + '.bam'
    os.system (build_command)
    
    build_command = "samtools idxstats " + sorted_file + '.bam > ' + path + '/bowtie2/' + os.path.basename(contigs) + '.readcount.tab'
    print "\n\n" + build_command + "\n\n"
    os.system (build_command)
 
if __name__ == "__main__":
    sys.exit(main())
