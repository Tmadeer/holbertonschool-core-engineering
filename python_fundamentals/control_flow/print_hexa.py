#!/usr/bin/env python3
print(*("{} = {}".format(i, hex(i)) for i in range(0, 99)), sep="\n")
