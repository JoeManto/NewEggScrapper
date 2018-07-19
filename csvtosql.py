import csv


import argparse

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('file', nargs='?', help='name of csv with out extension')
parser.add_argument('tableName', nargs='?', help='name of the table to be created')

args = parser.parse_args()

filePath = args.file +'.csv'
tableName = args.tableName
sqlFile = open('sqlTest.sql', 'w')

def writeRowToFile(file,rowString):
	file.write("%s\n" % rowString)

with open(filePath,'rb') as cvsfile:
	rows = csv.reader(cvsfile, delimiter= ',')
	for row in rows:
		queryString = 'INSERT INTO '+ tableName + "('"
		for i,items in enumerate(row):
			queryString += str(items)
			if (i < len(row)-1):
				queryString += "','"
		queryString += "')\n" 
		writeRowToFile(sqlFile,queryString)
		print(queryString)

