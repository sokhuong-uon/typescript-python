import sys, json

def emit( data ):
	incoming = input()
	data =  json.loads( incoming )
	print( json.dumps( data ) )

