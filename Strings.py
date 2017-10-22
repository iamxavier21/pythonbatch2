
def ani(sr):
    return dict(item.split("=") for item in sr.split(";"))
    
xav= ani("abc=de;fg=hi")
print xav
