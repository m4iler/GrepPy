from sys import argv
import antigravity

if len(argv) <= 2:
    print("Ya ain't searching shit, lad!")
else:
    f = file(argv[2])
    for line in f:
        if argv[1] in line:
            print line

