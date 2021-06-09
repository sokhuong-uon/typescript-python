import sys

res: int = 0
for v in sys.argv[1:]:
	res += int(v)
	print( res )