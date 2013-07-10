README.

Introduction:
This python script wraps a regex that captures all money formats. Example formats:
$1
$1,000,000
$1000000
One million dollars
$5.25
5 million 200 thousand 27 hundred dollars
Etc.

Given an input file with text, the program creates an output file which contains the same text except all money format expressions will be surrounded by []

Ex:
'Last year we donated 25 million dollars and twenty cents' --> 'Last year we donated [25 million dollars and twenty cents]'

Requirements:
Python 2.6 or higher

Therefore, the command I recommend to use is:
$> python2.6 moneyFinder.py INPUTFILENAME OUTPUTFILENAME


Errors / issues:
The path to the INPUTFILENAME and OUTPUTFILENAME parameters can be a relative or absolute path, but if either one of these files cannot be opened (i.e. INPUTFILENAME points to a file that doesn't exist, etc) the script will exit with an error code. Similarly, if not all command line parameters are submitted the application will exit with a usage message and an error code.

Aside from that, there should really be no issues. The python script imports the re and sys modules (re for regex operations and sys to get the command line arguments) so your installation of python should contain these libraries.
