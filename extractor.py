from xlrd import open_workbook
from geocoder import getKey, buildGeoReference


class Extractor(object):
	"""Base class!!"""

	def __init__(self, inputFile, outputFile):

		self.inputFile = inputFile
		self.outputFile = outputFile


	def extractFromExcel(self):

		outreversa = []

		try:
			with open(self.outputFile,'r') as outReversaFile:
				outreversa = [line for line in outReversaFile]
		except IOError as e:
			print 'Error al abrir el archivo OUTREVERSA.OUT ' + e

		outreversa.sort(key=lambda puntos: puntos[0:9])
		excel = []
		try:
			workbook = open_workbook(self.inputFile)
		except IOError as e:
			print 'Error al abrir el archivo de Excel' + e

		for sheet in workbook.sheets():
			for row in range(sheet.nrows):
				if row == 0:
					continue
				temp=[]
				for col in range(sheet.ncols):
					temp.append(sheet.cell(row,col).value)
				excel.append(temp)



		counter = 0
		for excelLine in excel:
			newKeyFlag = True
			georeferenceKey= getKey(excelLine[2],excelLine[1])
			for index,geoLine in enumerate(outreversa):
				if georeferenceKey == geoLine[0:9]:
					newKeyFlag = False
					# the geoRefKey exist in outreversa.out
					geoLine = geoLine.split('|')
					lineHeader = geoLine[0:2]
					lineHeader[1] = str(int(lineHeader[1]) + 1)
					lineHeader = '|'.join(lineHeader)

					lineContent = geoLine[2].split('&')

					newLineContent = buildGeoReference(lat=excelLine[2],lon=excelLine[1],descrip=excelLine[3])
					lineContent.insert(-2, newLineContent)
					lineContent = '&'.join(lineContent)
					outreversa[index] = lineHeader + '|' + lineContent
					counter = counter + 1
					break

			if newKeyFlag:
				newGeoLine = georeferenceKey + '|1|' + buildGeoReference(lat=excelLine[2],lon=excelLine[1],descrip=excelLine[3]) + '&\n'
				outreversa.append(newGeoLine)
				counter = counter  + 1

		try:

			with open(self.outputFile,'w') as outReversaFile:
				for line in outreversa:
					outReversaFile.write(line.encode('utf8'))
				print 'new georeferences inserted: ', counter
		except IOError as e:
			print 'Ocurrio un error al escribir archivo OUTREVERSA.OUT', e
























