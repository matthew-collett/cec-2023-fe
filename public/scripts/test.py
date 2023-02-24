import sys
import json
from typing import Dict

def out(string: str) -> None:
    print(string)
    sys.stdout.flush()

if __name__ == '__main__':
    test: Dict[str, str] = {'test': 'hi', 'please': 'work'}
    out(json.dumps(test))
