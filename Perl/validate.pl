#!/usr/bin/perl

#4 values
#first name, last name, zip code, email address
print "First name: ";
$firstname = <STDIN>;
chomp($firstname);
unless ( "$firstname" =~ /^[A-Z][A-Za-z-]*$/ )
{
	die "First name must start with a capital letter and contain only letters and hypens!\n";
}

print "Last name: ";
$lastname = <STDIN>;
chomp($lastname);
unless ( "$lastname" =~ /^[A-Z][A-Za-z-]*$/ )
{
	die "Last name must start with a capital letter and contain only letters and hypens!\n";
}

print "Zip Code: ";
$zip = <STDIN>;
chomp($zip);
unless ( "$zip" =~ /^\d{5}$/ )
{
	die "Zip code must be exactly 5 digits!\n";
}

print "Email address: ";
$email = <STDIN>;
chomp($email);
unless ( "$email" =~ /^[\w\.\-]+\@[\w\.\-]+\.[\w\.\-]+$/ )
{
	die "Email address must be USER\@DOMAIN, where both USER and DOMAIN must be only letters, numbers, dots, underscores, and hyphens!\n";
}
print "Validated!\n";
