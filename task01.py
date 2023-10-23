#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

class bignum() :
    def __init__(self,h):
        import json
        data = json.loads(open(f'{h}.txt','r').read())
        lnum = data[0]
        for i in data: 
            if i > lnum: lnum = i
        else:pass
        print(lnum)
bignum("task01a")
bignum("task01b")
bignum("task01c")