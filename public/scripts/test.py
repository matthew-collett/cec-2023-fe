import sys
import json
from typing import Dict

def out(string: str) -> None:
    print(string)
    sys.stdout.flush()

if __name__ == '__main__':
    body = {
        'tableHeader': ['Student ID', 'Student Name', 'School'],
        'tableData': [
            [0, 'Billy', 'Smalltown Elementary'],
            [1, 'Henry', 'Riverbank High'],
            [2, 'Mike', 'Oaktree Middle School'],
            [3, 'Tom', 'Ocean Height High'],
            [4, 'George', 'Seashore Drive Elementary']
        ]
    }
    out(json.dumps(body))