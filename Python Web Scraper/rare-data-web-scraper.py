from bs4 import BeautifulSoup
import requests
import pickle
import threading
import re
import chompjs


#rares = npcID
#npcID is used on the webpage
rares = [
    25323,
    25406,
    25411,
    11676,
    14018,
    26791,
    14019,
    14016,
    14432,
    1531,
    14428,
    5796,
    1936,
    14431,
    1533,
    5795,
    5790,
    14430,
    1137,
    5826,
    3068,
    5786,
    5808,
    5809,
    5793,
    5789,
    5794,
    10356,
    99,
    471,
    1910,
    79,
    5807,
    1132,
    16855,
    5824,
    5822,
    5785,
    5823,
    16854,
    5787,
    8503,
    1260,
    14429,
    10357,
    61,
    1130,
    1911,
    472,
    10358,
    3056,
    100,
    1119,
    3535,
    5865,
    12431,
    2175,
    10359,
    2191,
    12432,
    3270,
    1425,
    12433,
    1424,
    3470,
    519,
    5837,
    14268,
    7017,
    2186,
    7015,
    5841,
    3672,
    5838,
    2184,
    14271,
    5829,
    3652,
    596,
    22062,
    22060,
    5835,
    599,
    506,
    14272,
    601,
    5912,
    14267,
    3586,
    5830,
    5842,
    520,
    5836,
    2192,
    5863,
    572,
    14266,
    3295,
    14270,
    3398,
    573,
    2172,
    3872,
    5831,
    1920,
    1399,
    14269,
    5797,
    5800,
    5864,
    5932,
    3735,
    1398,
    10559,
    7016,
    2476,
    10644,
    2283,
    1944,
    5828,
    616,
    14281,
    521,
    2090,
    10643,
    1948,
    12902,
    12876,
    5931,
    5799,
    14279,
    5849,
    14425,
    5847,
    1112,
    3253,
    5832,
    1037,
    1720,
    5798,
    5834,
    14273,
    10641,
    5848,
    14424,
    4015,
    10639,
    4438,
    5859,
    3773,
    947,
    462,
    4425,
    5827,
    5851,
    4842,
    5916,
    14280,
    10642,
    14426,
    584,
    574,
    10640,
    5928,
    6228,
    5930,
    14275,
    14427,
    14278,
    5915,
    2108,
    4030,
    4066,
    14276,
    14433,
    5933,
    503,
    1140,
    12037,
    18241,
    3792,
    6490,
    6488,
    5934,
    6489,
    771,
    14223,
    507,
    10647,
    14277,
    14225,
    10236,
    14228,
    534,
    2600,
    5937,
    14229,
    7895,
    14222,
    10238,
    10237,
    14221,
    2603,
    4132,
    2452,
    2751,
    5935,
    7354,
    2850,
    14230,
    14231,
    14487,
    14227,
    14236,
    1106,
    2606,
    14233,
    2258,
    7057,
    10239,
    2753,
    4380,
    14232,
    14237,
    14488,
    2598,
    2602,
    14234,
    2453,
    763,
    2604,
    2749,
    2609,
    14226,
    2744,
    14235,
    2605,
    4339,
    14224,
    11580,
    2779,
    2601,
    14491,
    14448,
    8211,
    5356,
    14492,
    11688,
    10818,
    14446,
    14447,
    8208,
    5352,
    8219,
    2447,
    5354,
    8210,
    14490,
    2754,
    14445,
    10080,
    8199,
    10082,
    5345,
    10820,
    2541,
    2752,
    1552,
    8218,
    10081,
    8200,
    12237,
    8279,
    8207,
    5343,
    1063,
    8203,
    5350,
    8280,
    5347,
    5346,
    8202,
    8296,
    8277,
    8216,
    8660,
    6118,
    5399,
    5400,
    5708,
    5349,
    14339,
    8302,
    8214,
    8281,
    8212,
    6651,
    8215,
    6648,
    8303,
    8205,
    14344,
    8201,
    6581,
    3581,
    8283,
    8278,
    8204,
    8924,
    6650,
    8282,
    8206,
    8213,
    6649,
    14342,
    8300,
    14345,
    6647,
    6652,
    9024,
    8217,
    13896,
    5367,
    1847,
    14343,
    8299,
    14346,
    6585,
    9042,
    8301,
    10077,
    6646,
    14341,
    9041,
    8298,
    14340,
    6582,
    9604,
    9602,
    2931,
    10817,
    10197,
    9046,
    10078,
    7104,
    7137,
    8923,
    10827,
    10825,
    14476,
    1848,
    8297,
    8981,
    10263,
    10196,
    10558,
    6583,
    11383,
    14475,
    9219,
    8304,
    14472,
    10821,
    10826,
    10200,
    8978,
    1850,
    11498,
    10393,
    9218,
    9217,
    1849,
    1844,
    14477,
    14478,
    10822,
    1885,
    10202,
    9596,
    15796,
    9718,
    10828,
    10509,
    11467,
    14474,
    10819,
    10199,
    8979,
    10823,
    10376,
    13977,
    8976,
    10198,
    6584,
    14473,
    11447,
    16184,
    12116,
    1841,
    9417,
    10809,
    11497,
    10119,
    10824,
    1837,
    14479,
    14479,
    10201,
    1838,
    14471,
    16380,
    18677,
    16379,
    10203,
    1843,
    14506,
    5348,
    18678,
    1851,
    18679,
    17075,
    1839,
    18682,
    18681,
    18680,
    18686,
    18685,
    18689,
    17144,
    18684,
    18699,
    18694,
    18698,
    18692,
    18696,
    18690,
    18693,
    18683,
    18695,
    18697,
    20932,
    32358,
    32398,
    32377,
    32386,
    32361,
    14697,
    32357,
    32409,
    16179,
    16181,
    32417,
    32429,
    16180,
    32438,
    32400,
    38453,
    32422,
    32481,
    32471,
    32485,
    32517,
    32475,
    33776,
    32447,
    32487,
    32500,
    32501,
    32495,
    35189,
    32491,
    32630,
    32338,
    31286,
    31289,
    31086,
    31071,
    39019,
    31074,
    31073,
    31093,
    31072,
    35074,
    31244,
    31156,
    31284,
    31287,
    31288,
    28282,
    28280
]

#zoneName: zoneID
#zoneID is used on the webpage
mapData = {
    "4494": "Ahn'kahet: The Old Kingdom",
    "3428": "Ahn'Qiraj",
    "36": "Alterac Mountains",
    "45": "Arathi Highlands",
    "331": "Ashenvale",
    "3790": "Auchenai Crypts",
    "4277": "Azjol-Nerub",
    "16": "Azshara",
    "3524": "Azuremyst Isle",
    "3": "Badlands",
    "3959": "Black Temple",
    "719": "Blackfathom Deeps",
    "1584": "Blackrock Depths",
    "1583": "Blackrock Spire",
    "2677": "Blackwing Lair",
    "3522": "Blade's Edge Mountains",
    "4": "Blasted Lands",
    "3525": "Bloodmyst Isle",
    "3537": "Borean Tundra",
    "46": "Burning Steppes",
    "2817": "Crystalsong Forest",
    "4395": "Dalaran",
    "148": "Darkshore",
    "1657": "Darnassus",
    "41": "Deadwind Pass",
    "2257": "Deeprun Tram",
    "405": "Desolace",
    "2557": "Dire Maul",
    "65": "Dragonblight",
    "4196": "Drak'Tharon Keep",
    "1": "Dun Morogh",
    "14": "Durotar",
    "10": "Duskwood",
    "15": "Dustwallow Marsh",
    "139": "Eastern Plaguelands",
    "12": "Elwynn Forest",
    "3430": "Eversong Woods",
    "361": "Felwood",
    "357": "Feralas",
    "3433": "Ghostlands",
    "721": "Gnomeregan",
    "394": "Grizzly Hills",
    "3923": "Gruul's Lair",
    "4416": "Gundrak",
    "4272": "Halls of Lightning",
    "4820": "Halls of Reflection",
    "4264": "Halls of Stone",
    "3535": "Hellfire Citadel",
    "3483": "Hellfire Peninsula",
    "3562": "Hellfire Ramparts",
    "267": "Hillsbrad Foothills",
    "495": "Howling Fjord",
    "4742": "Hrothgar's Landing",
    "3605": "Hyjal Past",
    "3606": "Hyjal Summit",
    "210": "Icecrown",
    "4812": "Icecrown Citadel",
    "1537": "Ironforge",
    "4080": "Isle of Quel'Danas",
    "3457": "Karazhan",
    "38": "Loch Modan",
    "4131": "Magisters' Terrace",
    "3836": "Magtheridon's Lair",
    "3792": "Mana-Tombs",
    "2100": "Maraudon",
    "2717": "Molten Core",
    "493": "Moonglade",
    "215": "Mulgore",
    "3518": "Nagrand",
    "3456": "Naxxramas",
    "3523": "Netherstorm",
    "2367": "Old Hillsbrad Foothills",
    "1637": "Orgrimmar",
    "4813": "Pit of Saron",
    "4298": "Plaguelands: The Scarlet Enclave",
    "2437": "Ragefire Chasm",
    "722": "Razorfen Downs",
    "491": "Razorfen Kraul",
    "44": "Redridge Mountains",
    "3429": "Ruins of Ahn'Qiraj",
    "796": "Scarlet Monastery",
    "2057": "Scholomance",
    "51": "Searing Gorge",
    "3607": "Serpentshrine Cavern",
    "3791": "Sethekk Halls",
    "3789": "Shadow Labyrinth",
    "209": "Shadowfang Keep",
    "3520": "Shadowmoon Valley",
    "3703": "Shattrath City",
    "3711": "Sholazar Basin",
    "1377": "Silithus",
    "3487": "Silvermoon City",
    "130": "Silverpine Forest",
    "406": "Stonetalon Mountains",
    "1519": "Stormwind City",
    "33": "Stranglethorn Vale",
    "2017": "Stratholme",
    "1417": "Sunken Temple",
    "4075": "Sunwell Plateau",
    "8": "Swamp of Sorrows",
    "440": "Tanaris",
    "141": "Teldrassil",
    "3845": "Tempest Keep",
    "3519": "Terokkar Forest",
    "3848": "The Arcatraz",
    "17": "The Barrens",
    "2366": "The Black Morass",
    "3713": "The Blood Furnace",
    "3847": "The Botanica",
    "4100": "The Culling of Stratholme",
    "1581": "The Deadmines",
    "3557": "The Exodar",
    "4500": "The Eye of Eternity",
    "4809": "The Forge of Souls",
    "47": "The Hinterlands",
    "3849": "The Mechanar",
    "4265": "The Nexus",
    "4493": "The Obsidian Sanctum",
    "4228": "The Oculus",
    "4987": "The Ruby Sanctum",
    "3714": "The Shattered Halls",
    "3717": "The Slave Pens",
    "3715": "The Steamvault",
    "717": "The Stockade",
    "67": "The Storm Peaks",
    "3716": "The Underbog",
    "400": "Thousand Needles",
    "1638": "Thunder Bluff",
    "85": "Tirisfal Glades",
    "4723": "Trial of the Champion",
    "4722": "Trial of the Crusader",
    "1337": "Uldaman",
    "4273": "Ulduar",
    "490": "Un'Goro Crater",
    "1497": "Undercity",
    "206": "Utgarde Keep",
    "1196": "Utgarde Pinnacle",
    "4603": "Vault of Archavon",
    "4415": "Violet Hold",
    "718": "Wailing Caverns",
    "28": "Western Plaguelands",
    "40": "Westfall",
    "11": "Wetlands",
    "4197": "Wintergrasp",
    "618": "Winterspring",
    "3521": "Zangarmarsh",
    "3805": "Zul'Aman",
    "66": "Zul'Drak",
    "1176": "Zul'Farrak",
    "1977": "Zul'Gurub"
}

#dictionary for creature type
getCreatureType = {
    "1": "Beast",
    "2": "Dragonkin",
    "3": "Demon",
    "4": "Elemental",
    "5": "Giant",
    "6": "Undead",
    "7": "Humanoid",
    "8": "Critter",
    "9": "Mechanical",
    "10": "Uncategorized",
    "11": "Totem",
    "12": "Non-combat Pet",
    "13": "Gas Cloud"
}

#dictionary to multiply respawn timers, to get seconds
#currently unused, respawn time is just to display info
dictRespawnTime = {
    "minute": 60,
    "minutes": 60,
    "hour": 3600,
    "hours": 3600,
    "day": 86400,
    "days": 86400
}

rareAmounts = str(len(rares))

#the final dictionary with correct syntax
rareLocationData = {}

threads = []
counterProg = 0

#npc id blank url
mapurl = "https://wowgaming.altervista.org/aowow/?npc="

#convert x and y float coordinates to xxxxyyyy string with set length
def convertCoord(coordinate):
    coordList = coordinate.split(".")
    if len(coordList[0])<2:
        coordList[0] = "0" + coordList[0]
    if len(coordList) == 1:
        coordList.append("00")
    elif len(coordList[1])<2:
        coordList[1] = coordList[1] + "0"
    return coordList[0] + coordList[1]
def transformCoordinate(xCoord,yCoord):
    return convertCoord(str(xCoord)) + convertCoord(str(yCoord))

#attempt to extract rarespawn coordinates
#return success state
def getRareLocationData(soup,nID):
    rareName        = None
    rareID          = nID
    rareLevel       = None
    rareType        = None
    rareElite       = False
    rareRespawnTime = None
    rareEvent       = False
    
    #type at index 13
    #level and elite at 15
    #coords at 17
    #start at 12 for unexpected difference
    for elemnt in soup[12:]:

        #get the script text data
        data = elemnt.text
        #get rare creature type
        if "\"breadcrumb\":" in data:
            rareType = getCreatureType[re.findall(r"(?:\"breadcrumb\":\[0,4,)(\d)",data)[0]]
        #get rare level and elite status
        elif "Markup.printHtml(\"[ul]" in data:
            if re.match(r"(Event:)",data):
                rareEvent = True
            extraData = re.findall(r"(?:Level: )(?:(?:\d+) - )*(\d+)(?:\[\/li\]\[li\]Classification: (?:\[span class=icon-boss\])?Rare)(?: ?)(.*?)(?:\[\/li\]\[li\]React)", data)
            rareLevel = extraData[0][0]
            if "Elite" == extraData[0][1]:
                rareElite = True
        #check if the script contains location data
        elif "g_mapperData" in data:            
            #get raw location data
            data = re.findall(r"({.*?})(?:;)", data)[0]
            #add location data to dict
            petLocation = chompjs.parse_js_object(data)
            #iterate all zones the pet is in
            for zoneID, zoneData in petLocation.items():
                
                rareZoneName  = mapData[zoneID]
                rareLocations = []

                indent          = "\t"
                indent += "\t"

                for rareData in zoneData[0]["coords"]:
                    if "tooltip" in rareData[2]:
                        rareLocations.append(transformCoordinate(rareData[0],rareData[1]))
                        indent += "\t"
                        for name, info in rareData[2]["tooltip"].items():
                            if rareName is None:
                                rareName = name
                                indent += "\t"
                            elif rareName != name:
                                print(str(nID)+"\t\t"+"different name")
                                                
                            dataRespawnTime = info["info"]["1"]
                            respawntimeList = re.findall(r"(?:<span class=\"q0\">Respawn in: )((?:\d|\.)+)(?:&nbsp;)(.+?)(?:<\/span>)",dataRespawnTime)
                            respawntimer = respawntimeList[0][0] + " " + respawntimeList[0][1]                            
                            if rareRespawnTime is None:
                                rareRespawnTime = respawntimer
                                indent += "\t"
                            elif rareRespawnTime != respawntimer:
                                print(str(nID)+"\t\t"+"different respawn time ")
                
    
                #check if the master dictionary already has an entry for the zoneID
                #if it does, we cannot assign an empty sub dictionary to the zoneID key
                if rareZoneName in rareLocationData:
                    rareLocationData[rareZoneName][rareName] = {}
                else:
                    rareLocationData[rareZoneName] = { rareName: {}}

                #save all the data about the rarespawn in the master dict
                rareLocationData[rareZoneName][rareName]["id"]              = str(rareID)
                rareLocationData[rareZoneName][rareName]["level"]           = rareLevel
                rareLocationData[rareZoneName][rareName]["creature_type"]   = rareType
                if rareElite:
                    rareLocationData[rareZoneName][rareName]["elite"]       = True
                rareLocationData[rareZoneName][rareName]["respawn"]         = rareRespawnTime
                if rareEvent:
                    rareLocationData[rareZoneName][rareName]["event"]       = True
                rareLocationData[rareZoneName][rareName]["locations"]       = rareLocations

skipahead = True

#fetch rarespawn location data
def handleRareData(nID):
    
    printString = ""

    #counter to visualize progress in command line when executed
    global counterProg
    counterProg += 1
    
    printString = str(counterProg)+" / "+rareAmounts+"\t\t"+str(nID)

    #build the final rarespawn id url
    url = mapurl + str(nID)
    #get webpage script data
    soup = BeautifulSoup(requests.get(url).text, "html.parser").find_all("script")

    #attempt to extract pet coordinates
    getRareLocationData(soup,nID)

    print(printString)


#create threads for rares
for npcId in rares:
    t = threading.Thread(target=handleRareData,args=[npcId])
    t.start()
    threads.append(t)

#join all threads together
for thread in threads:
    thread.join()

for zone, zoneData in rareLocationData.items():
    print(zone)
    for rareName, rareData in zoneData.items():
        indent = "\t"
        print(indent+rareName)
        indent += "\t"
        for key, value in rareData.items():
            if type(value) is list:
                print(indent+key)
                for element in value:
                    print(indent+"\t"+element)
            else:
                if type(value) is bool:
                    print(indent+key+"\t"+str(value))
                else:
                    print(indent+key+"\t"+value)

#write pet npcID with (missing location) and (not taught by item) data to file
# [npcID]
with open("rareSpawnData.pkl", "wb") as df:
    pickle.dump(rareLocationData, df)