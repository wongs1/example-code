#!/usr/bin/perl
#This finds a specified string in a file and
#replaces and outputs to another file.
if ( $#ARGV != 3 )
{
	die "usage: find_and_replace.pl input_file output_file current new\n";
}
$input = $ARGV[0];
$output = $ARGV[1];
$current = $ARGV[2];
$new = $ARGV[3];
open($IN, "<$input") or die "couldn't open $input";
open($OUT, ">$output") or die "couldn't open $output";
while ( $next = <$IN> )
{
	chomp($next);
	$next =~ s/$current/$new/gi;
	print $OUT "$next\n";
}
close($IN);
close($OUT);
