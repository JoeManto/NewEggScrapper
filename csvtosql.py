import csv

tableName = "Gpu"
sqlFile = open('sqlTest.sql', 'w')

def writeRowToFile(file,rowString):
	file.write("%s\n" % rowString)

with open("index1.csv",'rb') as cvsfile:
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

