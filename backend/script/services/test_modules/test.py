import sys, json

raw = sys.argv[1:][0]
data = json.loads( raw )
res = sum( data )

print( res )