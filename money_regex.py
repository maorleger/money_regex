
import re
import sys



number = r'([0-9]{1,3}(,[0-9]{1,3})*(\.[0-9]?[0-9])?)'
wordNumbersSingle = r'(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen)'
wordNumbersDouble = r'(twenty|thirty|fourty|fifty|sixty|seventy|eighty|ninety)'
wordNumbers = r'({0}|{1}( {0})?)'.format(wordNumbersSingle, wordNumbersDouble)
quantityGroup = r'(({0}|{1})( ?({0} |{1} )?((m|b|tr)illion|thousand|hundred))*)'.format(number, wordNumbers)
dollarAppears = r'(\${0}(( {1}| {2})? dollars?)?)'.format(quantityGroup, number, wordNumbers)
noDollarSign = r'({0}( (({1}|{2}) )?dollars?))'.format(quantityGroup, number, wordNumbers)

pattern = r'({0}|{1})'.format(dollarAppears, noDollarSign)



if len(sys.argv) ==3:
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
else:
    print ('Usage: python2.6 money_regex.py INPUTFILENAME OUTPUTFILENAME')
    exit(1)

try:
    inputFile = open(inputFileName, 'r')
    outputFile = open(outputFileName, 'w')
    for line in inputFile:
        outputFile.write(re.sub(pattern, r"[\g<1>]", line))
    inputFile.close()
    outputFile.close()
except IOError as (errno, strerror):
    print ('IO Error({0}): {1}'.format(errno, strerror))
    exit(1)


