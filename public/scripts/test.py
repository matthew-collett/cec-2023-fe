import sys
import json



def testFunction():
    test = {'test': 'hi', 'please': 'work'}
    print(json.dumps(test))
    sys.stdout.flush()

testFunction()