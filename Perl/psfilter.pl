#!/usr/bin/perl
#This script is used to filter the current user's processes
#Format: ps -ef | ./psfilter.pl
$argnum = $#ARGV + 1;
if ( $argnum > 1 )
{
	die "usage: $0 [username]\n";
}
elsif ( $argnum == 1 )
{
	$username = $ARGV[0];
}
else #1st argument is empty
{
	$username = getpwuid($<);
}
#Read input from ps command
while($input = <STDIN>)
{
	chomp($input);
	if ( "$input" =~ /^$username\s+/ )
	{
		$numlines = 1;
		@pieces = split(/\s+/, "$input");

	    print "$pieces[1] ";
        for($i=7; $i<=$#pieces; $i++)
        {
            print "$pieces[$i] ";
        }
        print "\n";

		$numlines++;
	}
}
