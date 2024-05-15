# Trim quotes
def removequotes(text):
    if text[0:1] == '"': # Remove first quote
       text = text[1:]
    if text[-1:] == '"':
        text = text[:-1]
    return text


str = "ALLEN LIU"





print(removequotes(str))


