def csv2array(file: str):
    return open(file, encoding="utf8").read().splitlines()



onerow = csv2array("exercises.csv")[1]


for entity in onerow.split(","):
    print(type(entity), entity, entity.isnumeric())


