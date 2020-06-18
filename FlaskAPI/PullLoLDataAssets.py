import requests
import json
# Get Current Patch
def getCurrentVersion():
    versionResponse = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")
    version_patch_RawData = versionResponse.json()
    currentVersion = version_patch_RawData[0]
    print(currentVersion)
    return currentVersion

#champions, items, summoner_spells, spells
def GetDDragonData_Champions():
    version = getCurrentVersion()
    #Champions Data
    response = requests.get("http://ddragon.leagueoflegends.com/cdn/"+version+"/data/en_US/champion.json")
    allChampionRawData = json.loads(response.text)

    ChampionIdToName = {}
    for key,champion in allChampionRawData['data'].items():
        ChampionIdToName[int(champion['key'])] = champion['name']
    print(ChampionIdToName)
    return ChampionIdToName

def GetDDragonData_Items():
    version = getCurrentVersion()
    response = requests.get("http://ddragon.leagueoflegends.com/cdn/"+version+"/data/en_US/item.json")
    allItemsRawData = json.loads(response.text)
    QuickPrinter(allItemsRawData)

    #Items Data
    ItemIdToName = {}
    for key,item in allItemsRawData['data'].items():
        ItemIdToName[int(key)] = item['name']
    print(ItemToToName)
    return ItemIdToName

def QuickPrinter(String_to_Print):
    print(json.dumps(String_to_Print, indent=4, sort_keys=True))

#main()
version = getCurrentVersion()
GetDDragonData_Champions()
GetDDragonData_Items()