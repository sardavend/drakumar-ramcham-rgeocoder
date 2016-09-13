import os
import glob
import socket
import sys 
import optparse

from extractor import Extractor


def parseOptions():
    usage="""usage: %prog --inputfile path/to/file/xls --outputfile path/to/reversa/out """
    parser = optparse.OptionParser(usage)

    help = """Path where the xlsx file is located"""
    parser.add_option('--inputfile', help=help)

    help="""Path where the reversa.out is located"""

    parser.add_option('--outputfile', help=help)

    options, args = parser.parse_args()

    if options.inputfile and options.outputfile:
        return options
    else:
        parser.error("Please provide all the Options")


def run():
    options = parseOptions()
    #infiles = glob.glob(os.path.join(path,'*.txt'))
    extractor = Extractor(options.inputfile, options.outputfile)
    if options.inputfile[-4:] == 'xlsx':
        try:
            extractor.extractFromExcel()
        except RuntimeError as e:
            print e
    else:
        print 'File Type not supported\n File Type supported are : xlsx'


    
if(__name__ == '__main__'):
    run()







