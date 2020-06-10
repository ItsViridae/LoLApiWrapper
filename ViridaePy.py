import requests
import json
import time
import pymongo
import config

# MongoDb
client = pymongo.MongoClient(config.mongoConnnectionString)
db = client['viridaedb']

# Key
apiKey = config.api_key

# Riot Api Endpoints See: Riot Developer Portal
riotApi_GetSummonerInfo_BySummonerName = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
riotApi_GetSummonerMatchHistory_BySummonerId = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/"
riotApi_Get_Matches_GameId = "https://na1.api.riotgames.com/lol/match/v4/matches/"
riotApi_GET_ChampionMasteries_BySummonerId = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"

#Batch Queries
#SummonerNamesList = ["Learn2Program", "Ali00P", "PorkPounder", "Redmarmalade", "LonelySupport"]
ScottAccountNameList = ["Learn2Program", "UsedIgniteOnWeed", "Ali00P", "PorkPounder", "Redmarmalade", "LonelySupport"]
ScottAccountIdList = []

#filled probably by a inputbox
summonerName = ""
summonerId = ""
accountId = ""
gameIdList = []
summonerIdList = []
matchList = []
matchesValuesOnlyList = []
SummonerInfoDictionary = {}

def MakeApiCall(query):
    # Check Limiter for # of Calls 
    # 20 requests every 1 second
    # 100 requests every 2 minutes
    response = requests.get(query)
    return response.json()

def GetAll_ChampionMasteries_ForOne_SummonerId(domain, summId, key):
    queryBuilder = "{0}{1}?api_key={2}"
    query = queryBuilder.format(domain, summId, key)
    championMasteryData = MakeApiCall(query)
    Game_OverWriteDataToFile("SummonerId_"+summId, championMasteryData)
    #MongoDbResponse = db.ChampionMastery.insert_one(championMasteryData)
    #print("Successfully Stored into MongoDB... MongoDBResponse: ", MongoDbResponse)
    #Pull championId : value
    #Pull championPoints : value        <--MasteryPoints
    #Pull summonerId : value            <-- who it belongs too

def GetAll_ChampionMasteries_ForAllAccounts_InAccountIDList(domain, listOfAccountId, key):
    for accid in listOfAccountId:
        queryBuilder = "{0}{1}?api_key={2}"
        query = queryBuilder.format(domain, accid, key)
        championMasteryData = MakeApiCall(query)
        result = db.ChampionMastery.insert_one(championMasteryData)
        print(result)
        print("Successfully added All ChampionMastery from Specific Id", accid)
        time.sleep(0.5)

def GetAll_AccountIds_ForAllAccountNames(domain, ScottAccountNameList, key):
    for name in ScottAccountNameList:
        queryBuilder = "{0}{1}?api_key={2}"
        query = queryBuilder.format(domain, name, key)
        summonerInfo = MakeApiCall(query)
        print("Summoner Name: " + name)
        summonerName = summonerInfo['name']
        summonerId = summonerInfo['id']
        accountId = summonerInfo['accountId']
        if summonerId not in summonerIdList:
            summonerIdList.append(summonerId)
        if accountId not in ScottAccountIdList:
            ScottAccountIdList.append(accountId)
        time.sleep(0.5)
    print(ScottAccountIdList)
    print(summonerIdList)
    #GetAll_ChampionMasteries_ForAllAccounts_InAccountIDList(riotApi_GET_ChampionMasteries_BySummonerId, ScottAccountIdList, apiKey)

def GetMatches(domain, accId, key):
    queryBuilder = "{0}{1}?api_key={2}"
    query = queryBuilder.format(domain, accId, key)
    summonerMatchInfo = MakeApiCall(query)
                                                #Loops through all 100 Matches
    for match in summonerMatchInfo["matches"]:                             
        gameIdList.append(match['gameId'])      #gets all Gameid's and adds them to the GameIdList
                                                #Call GameID and pass ApiCallQuery with the GameIdList
    GetGameInfoById(riotApi_Get_Matches_GameId, apiKey, gameIdList)
    
def GetSummonerInfo_Using_SummonerName(domain, key, name):
    queryBuilder = "{0}{1}?api_key={2}"
    query = queryBuilder.format(domain, name, key)
    summonerInfo = MakeApiCall(query)
    #mongodbResultResponse = db.SummonerInfo.insert_one(summonerInfo)
    #print("\tSuccessfully Stored One SummonerInfo Into SummonerInfo-Collection... \n\tMongoDbResultResponse: ", mongodbResultResponse)
    # Store Summoner Id for later:
    summonerId = summonerInfo['id']
    summonerName = summonerInfo['name']
    accountId = summonerInfo['accountId']
    summonerLevel = summonerInfo['summonerLevel']
    if summonerId not in summonerIdList:
        summonerIdList.append(summonerId)
    if accountId not in ScottAccountIdList:
        ScottAccountIdList.append(accountId)
    if (summonerId not in SummonerInfoDictionary) or (accountId not in SummonerInfoDictionary) or (summonerLevel not in SummonerInfoDictionary) or (summonerName not in SummonerInfoDictionary):
        SummonerInfoDictionary.update({'name': summonerName, 'summonerId': summonerId, 'accountId': accountId, 'summonerLevel': summonerLevel})
    Game_OverWriteDataToFile(summonerName, SummonerInfoDictionary)

    # Using List of AccountID's
    #GetAll_ChampionMasteries_ForAllAccounts_InAccountIDList(riotApi_GET_ChampionMasteries_BySummonerId, ScottAccountList, apiKey)

    #   Using For-Loop SummonerIDs List, Make API Call Each Iteration
    # for summonerId in summonerIdList:
    #     GetAll_ChampionMasteries_ForOne_SummonerId(riotApi_GET_ChampionMasteries_BySummonerId, summonerId, apiKey)
    # print("finished inserting all Summoner's ChampionMasteries")
    
    #GetMatches(riotApi_GetSummonerMatchHistory_BySummonerId, summonerId, apiKey)
    #GetAll_AccountIds_ForAllAccountNames(riotApi_GetSummonerInfo_BySummonerName, accountIdList, apiKey)


def GetGameInfoById(domain, key, gameIdList):
    #get 1 game for Testing
    gameId = gameIdList[0]
    #end of testing
    queryBuilder = "{0}{1}?api_key={2}"
    query = queryBuilder.format(domain, gameId, key)
    gameInfo = MakeApiCall(query)
    Game_OverWriteDataToFile("Game1", gameInfo)
    
    # Printers

# Printers / Writer + Format Helpers
def QuickPrinter(String_to_Print):
    print(json.dumps(String_to_Print, indent=4, sort_keys=True))

    # Writing to Textfiles or whatever
def AppendDataToFile(fileName, dataToAdd):
    fName = fileName + ".txt"
    f = open(fName, "a")
    f.write(str(dataToAdd))
    f.write("\n")
    f.close()
    print("Done Appending to file...")
def Game_OverWriteDataToFile(fileName, data):
    fName = fileName + ".json"
    f = open(fName, "w")
    f.write(json.dumps(data, indent=4, sort_keys=True))
    f.close()
    print("Done Writing/OverWriting to file...")

#call Function
#GetAll_AccountIds_ForAllAccountNames(riotApi_GetSummonerInfo_BySummonerName, ScottAccountNameList, apiKey)

    # Multiple calls for all Names in ScottAccountNameList!
# for name in ScottAccountNameList:
#     GetSummonerInfo_Using_SummonerName(riotApi_GetSummonerInfo_BySummonerName, apiKey, name)
#     time.sleep(0.6)


#Call Order
#    GetSummonerInfo -> GetMatches -> GetGameInfoById -> TODO: Soon save Data

#    GetSummonerInfo -> GetAll_ChampionMasteries...