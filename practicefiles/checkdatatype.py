pokemons = ['1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False', '2,Ivysaur,Grass,Poison,405,60,62,63,80,80,60,1,False', '3,Venusaur,Grass,Poison,525,80,82,83,100,100,80,1,False', '3,VenusaurMega Venusaur,Grass,Poison,625,80,100,123,122,120,80,1,False', '4,Charmander,Fire,,309,39,52,43,60,50,65,1,False', '5,Charmeleon,Fire,,405,58,64,58,80,65,80,1,False', '6,Charizard,Fire,Flying,534,78,84,78,109,85,100,1,False', '6,CharizardMega Charizard X,Fire,Dragon,634,78,130,111,130,85,100,1,False', '6,CharizardMega Charizard Y,Fire,Flying,634,78,104,78,159,115,100,1,False', '7,Squirtle,Water,,314,44,48,65,50,64,43,1,False', '8,Wartortle,Water,,405,59,63,80,65,80,58,1,False', '9,Blastoise,Water,,530,79,83,100,85,105,78,1,False', '9,BlastoiseMega Blastoise,Water,,630,79,103,120,135,115,78,1,False', '10,Caterpie,Bug,,195,45,30,35,20,20,45,1,False', '11,Metapod,Bug,,205,50,20,55,25,25,30,1,False', '12,Butterfree,Bug,Flying,395,60,45,50,90,80,70,1,False', '13,Weedle,Bug,Poison,195,40,35,30,20,20,50,1,False', '14,Kakuna,Bug,Poison,205,45,25,50,25,25,35,1,False', '15,Beedrill,Bug,Poison,395,65,90,40,45,80,75,1,False', '15,BeedrillMega Beedrill,Bug,Poison,495,65,150,40,15,80,145,1,False']

def createstructure(data):
    tablestructure = [False for _ in range(len(data[0].split(",")))]
    for d in data:
        headings = d.split(",")
        for id, field in enumerate(headings):
            tablestructure[id] = field.isnumeric()
    tablestructure = ["INTEGER" if dt == True else "TEXT" for dt in tablestructure ]
    return tablestructure


print(createstructure(pokemons))