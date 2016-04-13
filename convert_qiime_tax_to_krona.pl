#!/usr/bin/env perl
use warnings;
use IO::String;
use File::Basename;
use File::Copy;
use Cwd;

#-----------------------------------------------------------------------------
# This script converts a qiime taxonomic output to krona plot format.
# Author: Boris Wawrik
# email : bwawrik@ou.edu
# last edited: April 13th, 2016
#-----------------------------------------------------------------------------
#----SUBROUTINES--------------------------------------------------------------
#-----------------------------------------------------------------------------
sub get_file_data
{
  my ($file_name) = @_;
  my @file_content;
  open (PROTEINFILE, $file_name);
  @file_content = <PROTEINFILE>;
  close PROTEINFILE;
  return @file_content;
} # end of subroutine get_file_data;

sub WriteArrayToFile
{
  my ($filename, @in) = @_;
  my $a = join (@in, "\n");
  open (OUTFILE, ">$filename");
  foreach my $a (@in)
{
    print OUTFILE $a;
    print OUTFILE "\n";
  }
close (OUTFILE);
}

#-----------------------------------------------------------------------------
# inputs and parameters
#-----------------------------------------------------------------------------
my $InputTaxTable = $ARGV[0];
my $OutputTaxTable = $ARGV[1];

#-----------------------------------------------------------------------------
# get file data and parse
#-----------------------------------------------------------------------------

my @input_array = get_file_data ($InputTaxTable); chomp @input_array;
my @output_array;

foreach my $st (@input_array)
{
my @test_hashtag = split("",$st);
if ($test_hashtag[0] ne "#")
    {
    my @fs = split (/\t/, $st); 
    my @ks = split (";__", $fs[0]);
    my $outstring = $fs[1];
    foreach my $r (@ks)
           {
           $outstring=$outstring."\t".$r;
           }
    push (@output_array,$outstring);
    }
}

WriteArrayToFile ($OutputTaxTable, @output_array);
