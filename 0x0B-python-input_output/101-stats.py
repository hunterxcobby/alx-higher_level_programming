#!/usr/bin/python3

"""Log Parsing Module
Will contain script that reads stdin line by line and computes metrics:
Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import sys

metrics = {
    'total_size': 0,
    'status_codes': {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                     404: 0, 405: 0, 500: 0},
    'line_count': 0
}

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) >= 7:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                metrics['total_size'] += file_size
                if status_code in metrics['status_codes']:
                    metrics['status_codes'][status_code] += 1
                metrics['line_count'] += 1

                if metrics['line_count'] % 10 == 0:
                    print("File size: {}".format(metrics['total_size']))
                    for code in sorted(metrics['status_codes']):
                        if metrics['status_codes'][code] > 0:
                            print("{}: {}".format(
                                code, metrics['status_codes'][code]
                            ))

        except ValueError:
            continue
except KeyboardInterrupt:
    pass

print("File size: {}".format(metrics['total_size']))
for code in sorted(metrics['status_codes']):
    if metrics['status_codes'][code] > 0:
        print("{}: {}".format(code, metrics['status_codes'][code]))
