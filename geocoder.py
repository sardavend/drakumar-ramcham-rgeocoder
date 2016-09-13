import time

def getKey(lat , lon):

	"""Returns a Key of type xxxx:yyyy where xxxx and yyyy are the first 4 numbers of the latitude:longitude absolute value and without decimal point """
	lat = str(lat).replace('-','').replace('.','')[0:4]
	lon = str(lon).replace('-','').replace('.','')[0:4]
	return lat + ':' + lon

def buildGeoReference(lat, lon, descrip):
	descrip = descrip.split(',')
	direccion = descrip[0]
	ciudad = descrip[1]
	referenceId = ciudad[0:2] + str(int(time.time()))
	latitude = str(lat)
	longitude = str(lon)
	distance= '0'
	description = descrip
	noDescription1= '--'
	newGeoReference = [referenceId,latitude,longitude,distance,direccion,ciudad,ciudad]
	return '$'.join(newGeoReference)








