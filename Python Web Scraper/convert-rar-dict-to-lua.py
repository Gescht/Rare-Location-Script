import pickle

#the final dictionary with correct syntax
rareLocationData = {}

#load zoneID:mapID dictionary from file
with open("rareSpawnData.pkl", "rb") as f:
    rareLocationData = pickle.load(f)

with open("rareSpawnData.lua", "w") as the_file:
    the_file.write("{\n")
    for zoneName, zoneData in rareLocationData.items():
        the_file.write("\t\t[\""+zoneName+"\"] = {\n")
        for rareName, rareData in zoneData.items():
            the_file.write("\t\t\t[\""+str(rareName)+"\"] = {")
            
            for key, value in rareData.items():
                if type(value) is list:
                    the_file.write(key+" = {")
                    for element in value:
                        the_file.write(element+",")
                    the_file.write("},")
                else:
                    if type(value) is bool:
                        the_file.write(key+"="+str(value)+",")
                    else:
                        the_file.write(key+"="+value+",")
            the_file.write("},\n")

        the_file.write("\t\t},\n")
    the_file.write("}")