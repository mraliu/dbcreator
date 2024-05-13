str = "C:/Users/allen/Documents/dbcreator/pokemon.csv"

# nstr = str[::-1] # can reverse a string

# rfind finds last occurance of /


# Get filename
def getfilename(filenamedir):
    return filenamedir[filenamedir.rfind("/")+1:]

# Get name of file
def getnameoffile(filename):
    return filename[:filename.rfind(".")]


filename = getfilename(str)

print(getnameoffile(filename))