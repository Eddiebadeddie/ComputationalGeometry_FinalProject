import TestPolygon
import sys

argc = len(sys.argv)
debug = False
debug_index = 0

if(argc > 1):
    for x in range(len(sys.argv)):
        if sys.argv[x] == "debug":
            debug_index = x
            debug = True

test = TestPolygon.TestPolygon(debug)

test.Test1()

for i in range(1, argc):
    print()
    
    if i == debug_index:
        continue
    
    test.Test2(sys.argv[i])