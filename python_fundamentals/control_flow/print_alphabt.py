#!/usr/bin/env python3
result = ""

for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':
        result = "{}{}".format(result, chr(i))

print(result)
