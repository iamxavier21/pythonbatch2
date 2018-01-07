
def dstring(pydict):
    xs=""
    for key,value in pydict.items():
        xs +=key+"="+value+";"
        return xs
