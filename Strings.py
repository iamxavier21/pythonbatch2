
def ani(sr):
    return dict(item.split("=") for item in sr.split(";"))
    
xav= ani("ab=c;def=ghi")
print xav
