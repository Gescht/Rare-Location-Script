from bs4 import BeautifulSoup
import pickle
import re
import chompjs
import html

#rares = npcID: zoneName
#npcID is used on the webpage
rares = {
    14432: "Teldrassil",
    1531: "Tirisfal Glades",
    14428: "Teldrassil",
    1936: "Tirisfal Glades",
    14431: "Teldrassil",
    1533: "Tirisfal Glades",
    14430: "Teldrassil",
    1137: "Dun Morogh",
    5826: "Durotar",
    3068: "Mulgore",
    5786: "Mulgore",
    5808: "Durotar",
    5809: "Durotar",
    10356: "Tirisfal Glades",
    99: "Elwynn Forest",
    471: "Elwynn Forest",
    1910: "Tirisfal Glades",
    79: "Elwynn Forest",
    5807: "Mulgore",
    1132: "Dun Morogh",
    16855: "Eversong Woods",
    5824: "Durotar",
    5822: "Orgrimmar",
    5785: "Mulgore",
    5823: "Durotar",
    16854: "Eversong Woods",
    5787: "Mulgore",
    8503: "Dun Morogh",
    1260: "Dun Morogh",
    14429: "Teldrassil",
    10357: "Tirisfal Glades",
    61: "Elwynn Forest",
    1130: "Dun Morogh",
    1911: "Tirisfal Glades",
    472: "Elwynn Forest",
    10358: "Tirisfal Glades",
    3056: "Mulgore",
    #100: "Elwynn Forest",
    1119: "Dun Morogh",
    3535: "Teldrassil",
    5865: "The Barrens",
    12431: "Silverpine Forest",
    2175: "Darkshore",
    10359: "Tirisfal Glades",
    2191: "Darkshore",
    12432: "Silverpine Forest",
    3270: "The Barrens",
    1425: "Loch Modan",
    12433: "Tirisfal Glades",
    1424: "Westfall",
    3470: "The Barrens",
    519: "Westfall",
    5837: "The Barrens",
    14268: "Loch Modan",
    7017: "Darkshore",
    2186: "Darkshore",
    7015: "Darkshore",
    5841: "The Barrens",
    3672: "The Barrens",
    5838: "The Barrens",
    2184: "Darkshore",
    14271: "Redridge Mountains",
    5829: "The Barrens",
    3652: "The Barrens",
    596: "Westfall",
    22062: "Ghostlands",
    22060: "Bloodmyst Isle",
    5835: "The Barrens",
    599: "Westfall",
    506: "Westfall",
    14272: "Redridge Mountains",
    5912: "Wailing Caverns",
    14267: "Loch Modan",
    3586: "The Deadmines",
    5830: "The Barrens",
    5842: "The Barrens",
    520: "Westfall",
    5836: "The Barrens",
    2192: "Darkshore",
    5863: "The Barrens",
    572: "Westfall",
    14266: "Loch Modan",
    3295: "The Barrens",
    14270: "Redridge Mountains",
    3398: "The Barrens",
    573: "Westfall",
    2172: "Darkshore",
    3872: "Shadowfang Keep",
    5831: "The Barrens",
    1920: "Silverpine Forest",
    1399: "Loch Modan",
    14269: "Redridge Mountains",
    5797: "The Barrens",
    5800: "The Barrens",
    5864: "The Barrens",
    5932: "Stonetalon Mountains",
    3735: "Ashenvale",
    1398: "Loch Modan",
    10559: "Ashenvale",
    7016: "Darkshore",
    2476: "Loch Modan",
    10644: "Ashenvale",
    2283: "Silverpine Forest",
    1944: "Silverpine Forest",
    5828: "The Barrens",
    616: "Redridge Mountains",
    14281: "Alterac Mountains",
    521: "Duskwood",
    2090: "Wetlands",
    10643: "Ashenvale",
    1948: "Silverpine Forest",
    12902: "Blackfathom Deeps",
    5931: "Stonetalon Mountains",
    5799: "The Barrens",
    14279: "Hillsbrad Foothills",
    5849: "The Barrens",
    14425: "Wetlands",
    5847: "The Barrens",
    1112: "Wetlands",
    3253: "The Barrens",
    5832: "The Barrens",
    1037: "Wetlands",
    1720: "The Stockade",
    5798: "The Barrens",
    5834: "The Barrens",
    14273: "Redridge Mountains",
    10641: "Ashenvale",
    5848: "The Barrens",
    14424: "Wetlands",
    4015: "Stonetalon Mountains",
    #10639: "Ashenvale",
    4438: "Razorfen Kraul",
    5859: "The Barrens",
    3773: "Ashenvale",
    947: "Redridge Mountains",
    462: "Westfall",
    4425: "Razorfen Kraul",
    5827: "The Barrens",
    5851: "The Barrens",
    4842: "Razorfen Kraul",
    5916: "Stonetalon Mountains",
    14280: "Hillsbrad Foothills",
    10642: "Ashenvale",
    14426: "The Barrens",
    584: "Redridge Mountains",
    574: "Duskwood",
    10640: "Ashenvale",
    5928: "Stonetalon Mountains",
    6228: "Gnomeregan",
    5930: "Stonetalon Mountains",
    #14275: "Hillsbrad Foothills",
    14427: "Thousand Needles",
    14278: "Hillsbrad Foothills",
    5915: "Stonetalon Mountains",
    2108: "Wetlands",
    4030: "Stonetalon Mountains",
    4066: "Stonetalon Mountains",
    #14276: "Hillsbrad Foothills",
    14433: "Wetlands",
    5933: "Thousand Needles",
    503: "Duskwood",
    1140: "Wetlands",
    12037: "Ashenvale",
    18241: "Desolace",
    3792: "Ashenvale",
    6490: "Scarlet Monastery",
    6488: "Scarlet Monastery",
    5934: "Thousand Needles",
    6489: "Scarlet Monastery",
    771: "Duskwood",
    14223: "Alterac Mountains",
    507: "Duskwood",
    10647: "Ashenvale",
    14277: "Hillsbrad Foothills",
    14225: "Desolace",
    14228: "Desolace",
    534: "Duskwood",
    2600: "Arathi Highlands",
    5937: "Thousand Needles",
    14229: "Desolace",
    7895: "The Barrens",
    14222: "Alterac Mountains",
    14221: "Alterac Mountains",
    2603: "Arathi Highlands",
    4132: "Thousand Needles",
    2452: "Alterac Mountains",
    2751: "Badlands",
    5935: "Thousand Needles",
    7354: "Razorfen Downs",
    2850: "Badlands",
    14230: "Dustwallow Marsh",
    14231: "Dustwallow Marsh",
    14487: "Stranglethorn Vale",
    14227: "Desolace",
    14236: "Dustwallow Marsh",
    1106: "Swamp of Sorrows",
    2606: "Arathi Highlands",
    14233: "Dustwallow Marsh",
    2258: "Alterac Mountains",
    7057: "Badlands",
    2753: "Badlands",
    4380: "The Barrens",
    14232: "Dustwallow Marsh",
    14237: "Dustwallow Marsh",
    14488: "Stranglethorn Vale",
    2598: "Arathi Highlands",
    2602: "Arathi Highlands",
    14234: "Dustwallow Marsh",
    2453: "Alterac Mountains",
    763: "Swamp of Sorrows",
    2604: "Arathi Highlands",
    2749: "Badlands",
    2609: "Arathi Highlands",
    14226: "Desolace",
    2744: "Badlands",
    14235: "Dustwallow Marsh",
    2605: "Arathi Highlands",
    4339: "Dustwallow Marsh",
    14224: "Badlands",
    2779: "Wetlands",
    2601: "Arathi Highlands",
    14491: "Stranglethorn Vale",
    14448: "Swamp of Sorrows",
    8211: "The Hinterlands",
    5356: "Feralas",
    14492: "Stranglethorn Vale",
    11688: "Desolace",
    14446: "Swamp of Sorrows",
    14447: "Swamp of Sorrows",
    8208: "Tanaris",
    5352: "Feralas",
    8219: "The Hinterlands",
    2447: "Alterac Mountains",
    5354: "Feralas",
    8210: "The Hinterlands",
    14490: "Stranglethorn Vale",
    2754: "Badlands",
    14445: "Swamp of Sorrows",
    10080: "Zul'Farrak",
    8199: "Tanaris",
    10082: "Zul'Farrak",
    5345: "Feralas",
    2541: "Stranglethorn Vale",
    2752: "Badlands",
    1552: "Stranglethorn Vale",
    8218: "The Hinterlands",
    10081: "Zul'Farrak",
    8200: "Tanaris",
    12237: "Maraudon",
    8279: "Searing Gorge",
    8207: "Tanaris",
    5343: "Feralas",
    1063: "Swamp of Sorrows",
    8203: "Tanaris",
    5350: "Feralas",
    8280: "Searing Gorge",
    5347: "Feralas",
    5346: "Feralas",
    8202: "Tanaris",
    8296: "Blasted Lands",
    8277: "Searing Gorge",
    8216: "The Hinterlands",
    8660: "Azshara",
    6118: "Ashenvale",
    5399: "Swamp of Sorrows",
    5400: "Swamp of Sorrows",
    5349: "Feralas",
    14339: "Felwood",
    8302: "Blasted Lands",
    8214: "The Hinterlands",
    8281: "Searing Gorge",
    8212: "The Hinterlands",
    6651: "Azshara",
    8215: "The Hinterlands",
    6648: "Azshara",
    8303: "Blasted Lands",
    8205: "Tanaris",
    14344: "Felwood",
    8201: "Tanaris",
    6581: "Un'Goro Crater",
    3581: "Stormwind City",
    8283: "Searing Gorge",
    8278: "Searing Gorge",
    8204: "Tanaris",
    8924: "Burning Steppes",
    6650: "Azshara",
    8282: "Searing Gorge",
    8213: "The Hinterlands",
    6649: "Azshara",
    14342: "Felwood",
    8300: "Blasted Lands",
    14345: "Felwood",
    6647: "Azshara",
    6652: "Azshara",
    9024: "Blackrock Depths",
    8217: "The Hinterlands",
    13896: "Azshara",
    1847: "Western Plaguelands",
    14343: "Felwood",
    8299: "Blasted Lands",
    6585: "Un'Goro Crater",
    9042: "Blackrock Depths",
    8301: "Blasted Lands",
    10077: "Burning Steppes",
    6646: "Azshara",
    9041: "Blackrock Depths",
    8298: "Blasted Lands",
    14340: "Felwood",
    6582: "Un'Goro Crater",
    9604: "Burning Steppes",
    9602: "Burning Steppes",
    2931: "Badlands",
    10817: "Eastern Plaguelands",
    10197: "Winterspring",
    9046: "Searing Gorge",
    10078: "Burning Steppes",
    7104: "Felwood",
    7137: "Felwood",
    8923: "Blackrock Depths",
    10827: "Eastern Plaguelands",
    10825: "Eastern Plaguelands",
    14476: "Silithus",
    1848: "Western Plaguelands",
    8297: "Blasted Lands",
    8981: "Burning Steppes",
    10263: "Blackrock Spire",
    10196: "Winterspring",
    10558: "Stratholme",
    6583: "Un'Goro Crater",
    11383: "Stranglethorn Vale",
    14475: "Silithus",
    9219: "Blackrock Spire",
    8304: "Blasted Lands",
    14472: "Silithus",
    10821: "Eastern Plaguelands",
    10826: "Eastern Plaguelands",
    10200: "Winterspring",
    8978: "Burning Steppes",
    1850: "Western Plaguelands",
    11498: "Feralas",
    10393: "Stratholme",
    9218: "Blackrock Spire",
    9217: "Blackrock Spire",
    1849: "Western Plaguelands",
    1844: "Western Plaguelands",
    14477: "Silithus",
    14478: "Silithus",
    10822: "Eastern Plaguelands",
    1885: "Western Plaguelands",
    10202: "Winterspring",
    9596: "Blackrock Spire",
    9718: "Blackrock Spire",
    10828: "Eastern Plaguelands",
    10509: "Blackrock Spire",
    11467: "Dire Maul",
    14474: "Silithus",
    10199: "Winterspring",
    8979: "Burning Steppes",
    10823: "Eastern Plaguelands",
    10376: "Blackrock Spire",
    8976: "Burning Steppes",
    10198: "Winterspring",
    6584: "Un'Goro Crater",
    14473: "Silithus",
    11447: "Feralas",
    16184: "Western Plaguelands",
    1841: "Western Plaguelands",
    10809: "Stratholme",
    11497: "Feralas",
    10119: "Burning Steppes",
    10824: "Eastern Plaguelands",
    1837: "Western Plaguelands",
    14479: "Silithus",
    10899: "Blackrock Spire",
    10201: "Winterspring",
    1838: "Western Plaguelands",
    14471: "Silithus",
    16380: [ "Blasted Lands", "Burning Steppes", "Azshara", "Tanaris", "Winterspring", "Eastern Plaguelands" ],
    18677: "Hellfire Peninsula",
    16379: [ "Blasted Lands", "Burning Steppes", "Azshara", "Tanaris", "Winterspring", "Eastern Plaguelands" ],
    1843: "Western Plaguelands",
    18678: "Hellfire Peninsula",
    1851: "Western Plaguelands",
    18679: "Hellfire Peninsula",
    1839: "Western Plaguelands",
    18682: "Zangarmarsh",
    18681: "Zangarmarsh",
    18680: "Zangarmarsh",
    18686: "Terokkar Forest",
    18685: "Terokkar Forest",
    18689: "Terokkar Forest",
    17144: "Nagrand",
    18684: "Nagrand",
    18694: "Shadowmoon Valley",
    18698: "Netherstorm",
    18692: "Blade's Edge Mountains",
    18696: "Shadowmoon Valley",
    18690: "Blade's Edge Mountains",
    18693: "Blade's Edge Mountains",
    18683: "Nagrand",
    18695: "Shadowmoon Valley",
    18697: "Netherstorm",
    20932: "Netherstorm",
    32358: "Borean Tundra",
    32398: "Howling Fjord",
    32377: "Howling Fjord",
    32386: "Howling Fjord",
    32361: "Borean Tundra",
    14697: [ "Blasted Lands", "Burning Steppes", "Azshara", "Tanaris", "Winterspring", "Eastern Plaguelands" ],
    32357: "Borean Tundra",
    32409: "Dragonblight",
    16179: "Karazhan",
    16181: "Karazhan",
    32417: "Dragonblight",
    32429: "Grizzly Hills",
    16180: "Karazhan",
    32438: "Grizzly Hills",
    32400: "Dragonblight",
    38453: "Grizzly Hills",
    32422: "Grizzly Hills",
    32481: "Sholazar Basin",
    32471: "Zul'Drak",
    32485: "Sholazar Basin",
    32517: "Sholazar Basin",
    32475: "Zul'Drak",
    33776: "Zul'Drak",
    32447: "Zul'Drak",
    32487: "Icecrown",
    32500: "The Storm Peaks",
    32501: "Icecrown",
    32495: "Icecrown",
    35189: "The Storm Peaks",
    32491: "Icecrown",
    32630: "The Storm Peaks",
    32435: "Dalaran",
}

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
#the temp dict with preloaded soup
rareSoupLocationData = {}

#load rare soup dictionary from file
#[npcID]: [zoneName,websiteSoup]
with open("rareSoupDict.pkl", "rb") as f:
    rareSoupLocationData = pickle.load(f)

rareErrors = []

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

#save rarespawn data to dictionary
def setRareSpawnData(zName,rName,rId,rLvl,rType,rElite,rRespawn,rEvent,rLocation):
    #check if the master dictionary already has an entry for the zoneID
    #if it does, we cannot assign an empty sub dictionary to the zoneID key
    if zName in rareLocationData:
        rareLocationData[zName][rName] = {}
    else:
        rareLocationData[zName] = { rName: {}}

    #save all the data about the rarespawn in the master dict
    rareLocationData[zName][rName]["id"]              = str(rId)
    rareLocationData[zName][rName]["level"]           = rLvl
    rareLocationData[zName][rName]["creature_type"]   = rType
    if rElite:
        rareLocationData[zName][rName]["elite"]       = True
    if rRespawn:
        rareLocationData[zName][rName]["respawn"]     = rRespawn
    if rEvent:
        rareLocationData[zName][rName]["event"]       = True
    rareLocationData[zName][rName]["locations"]       = rLocation


def getCoordinates(typeListOrDict,nID):
    returnList = []
    if type(typeListOrDict) is list:
        returnList.append(typeListOrDict[0]["coords"])
    elif isinstance(typeListOrDict, dict):
        for zoneFloor, zoneCoords in typeListOrDict.items():
            returnList.append(zoneCoords["coords"])
    else:
        rareErrors.append([nID,"zoneData is neither list nor dict"])
    return returnList

#attempt to extract rarespawn coordinates
#return success state
def getRareLocationData(soup,nID,defaultZoneName):
    rareName        = None
    rareID          = nID
    rareLevel       = None
    rareType        = None
    rareElite       = False
    rareRespawnTime = None
    rareEvent       = False
    rareLocations   = []

    #type at index 13
    #event, level and elite at 15
    #coords at 17
    #start at 11 for unexpected difference
    for elemnt in soup[11:]:

        #get the script text data
        data = elemnt.text
        #get rare creature type
        if "\"breadcrumb\":" in data:
            rareName = html.unescape(re.findall(r"(?:,\"name\":\")(.+?)(?:\"};\n)",data)[0])
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
                if not(type(defaultZoneName) is list) and rareZoneName != defaultZoneName:
                    rareErrors.append([nID,"zone <"+rareZoneName+"> instead of <"+defaultZoneName+">"])
                for rareData in getCoordinates(zoneData,nID)[0]:
                    if "tooltip" in rareData[2]:
                        rareLocations.append(transformCoordinate(rareData[0],rareData[1]))
                        for name, info in rareData[2]["tooltip"].items():
                            rareName = name
                            dataRespawnTime = info["info"]["1"]
                            respawntimeList = re.findall(r"(?:<span class=\"q0\">Respawn in: )((?:\d|\.)+)(?:&nbsp;)(.+?)(?:<\/span>)",dataRespawnTime)
                            respawntimer = respawntimeList[0][0] + " " + respawntimeList[0][1]                            
                            if rareRespawnTime is None:
                                rareRespawnTime = respawntimer
                            elif rareRespawnTime != respawntimer:
                                rareErrors.append([nID,"respawn <"+respawntimer+"> instead of <"+rareRespawnTime+">"])

                # with location coords
                setRareSpawnData(rareZoneName,rareName,rareID,rareLevel,rareType,
                                    rareElite,rareRespawnTime,rareEvent,rareLocations)
                return

    # WITHOUT location coords
    #rare has a list of defaultzones
    if type(defaultZoneName) is list:
        for zone in defaultZoneName:
            setRareSpawnData(zone,rareName,rareID,rareLevel,rareType,
                        rareElite,rareRespawnTime,rareEvent,rareLocations)
    #rare has only one defaultzone
    else:
        setRareSpawnData(defaultZoneName,rareName,rareID,rareLevel,rareType,
                        rareElite,rareRespawnTime,rareEvent,rareLocations)

#fetch rarespawn location data
def handleRareData(nID,zName):

    printString = ""

    #counter to visualize progress in command line when executed
    global counterProg
    counterProg += 1

    printString = str(counterProg)+" / "+rareAmounts+"\t\t"+str(nID)

    #build the final rarespawn id url
    url = mapurl + str(nID)
    #get webpage script data from dict
    soup = rareSoupLocationData[nID][1].find_all("script")

    #attempt to extract pet coordinates
    getRareLocationData(soup,nID,zName)

    print(printString)

""" handleRareData(5912,"Wailing Caverns")
handleRareData(14432,"Teldrassil") """

for npcId, npcZone in rares.items():
    handleRareData(npcId,npcZone)
""" #create threads for rares
for npcId, npcZone in rares.items():
    t = threading.Thread(target=handleRareData,args=[npcId,npcZone])
    t.start()
    threads.append(t)

#join all threads together
for thread in threads:
    thread.join() """

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

#write final rarespawn data to lua file
with open("rareSpawnData.lua", "w") as the_file:
    the_file.write("{\n")
    for zoneName, zoneData in rareLocationData.items():
        the_file.write("\t\t[\""+zoneName+"\"] = {\n")
        for rareName, rareData in zoneData.items():
            the_file.write("\t\t\t[\""+str(rareName)+"\"] = {")
            
            for key, value in rareData.items():
                #handle elite 
                if type(value) is bool:
                    the_file.write(key+"="+str(value).lower()+",")
                #handle respawn or creature type
                elif "respawn" == key or "creature_type" == key:
                    the_file.write(key+"=\""+value+"\",")
                #handle location data
                elif type(value) is list:
                    the_file.write(key+" = {")
                    for element in value:
                        the_file.write(element+",")
                    the_file.write("},")
                else:
                    the_file.write(key+"="+value+",")
            the_file.write("},\n")

        the_file.write("\t\t},\n")
    the_file.write("}")

#write erros and rares tied to events to file
with open("rareErrors.txt", "w") as df:
    for element in rareErrors:
        df.write(str(element[0])+"\n"+str(element[1])+"\n\n")
