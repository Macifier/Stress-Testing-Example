import os
import sys
tests = int(sys.argv[1])
n = int(sys.argv[2])
for i in range(tests):
    print("Test" ,str(i))
    os.system("python3 test_generator.py  "+ str(n) + " "+str(i) + " > input.txt")
    os.system("python3 mainSolution.py < input.txt > mainSolution.txt")
    os.system("python3 alteranateSolution.py < input.txt > altSolution.txt")
    with open("mainSolution.txt") as f:
        main = f.read()
    with open("altSolution.txt") as f:
        alt = f.read()
    if main != alt:
        break
