import sys, getopt
import pandas as pd
import os

def excel_to_csv(file):
  workbook_url=file
  sheets_dict = pd.read_excel(workbook_url, sheet_name=None)
  
  filename = os.path.basename(workbook_url)
  filepath = os.path.dirname(os.path.realpath(workbook_url))
  namef=os.path.splitext(filename)
  destfilename='{}\\{}'.format(filepath,namef[0])
  
  for name, sheet in sheets_dict.items():
      sheet['sheet'] = name
      sheet.to_csv('{}_{}.csv'.format(destfilename, name), index=False)

def main(argv):
  inputfile = ''
  outputfile = ''
  short_options = "hi:"
  long_options = ["help", "ifile="]
  
  try:
    opts, args = getopt.getopt(argv,short_options,long_options)
  except getopt.GetoptError:
    print('excel_to_csv.py -i <inputfile>')
    sys.exit(2)
  
  for opt, arg in opts:
    if opt == '-h':
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
      
  excel_to_csv(inputfile)

if __name__ == "__main__":
  main(sys.argv[1:])