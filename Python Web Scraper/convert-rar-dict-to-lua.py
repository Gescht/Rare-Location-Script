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
                #handle location data
                if type(value) is list:
                    the_file.write(key+" = {")
                    for element in value:
                        the_file.write(element+",")
                    the_file.write("},")
                #handle elite
                elif type(value) is bool:
                    the_file.write(key+"="+str(value).lower()+",")
                #handle respawn or creature type
                elif "respawn" == key or "creature_type" == key:
                    the_file.write(key+"=\""+value+"\",")
                else:
                    the_file.write(key+"="+value+",")
            the_file.write("},\n")

        the_file.write("\t\t},\n")
    the_file.write("}")