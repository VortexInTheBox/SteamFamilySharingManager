from SteamSettings import *
import sys
import subprocess
import json

def installPackage(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

try:
    import requests
    import vdf
except ImportError:
    installPackage("requests")
    installPackage("vdf")
finally:
    import requests
    import vdf

def userInfo(ids):
    urlUser = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/"
    params = {'key': KEY, 'format': FORMAT, 'steamids': json.dumps(ids)}

    response = (requests.get(url=urlUser, params=params)).json()

    return [x for x in response['response']['players']]

def extractFilePortion(filename, toFind):
    numbrackets = 0
    flag = False
    data = ""
    with open(filename, "r") as file:
        for line in file:
            if flag:
                if "{" in line:
                    numbrackets = numbrackets + 1
                elif "}" in line:
                    numbrackets = numbrackets - 1
                if numbrackets == 0:
                    break
                data = data + line
            if toFind in line:
                flag = True
        return data

def modifyFilePortion(filename, toReplace, replacement):
    with open(filename, "r") as file:
        filedata = file.read()

    filedata = filedata.replace(toReplace, replacement)

    with open(filename, 'w') as file:
        file.write(filedata)


def SteamID3_To_SteamID64(steamID3):
    return f"7656119{(int(steamID3) + 7960265728)}"

def SteamID64_To_SteamID3(steamID64):
    return str(int(steamID64[7:]) - 7960265728)

def modifyOrder(sharing):
    sharingList = list(sharing)
    i, j = [int(x) for x in input("Insert the two indicies of the users to swap(i j): ").split()]
    sharingList[i], sharingList[j] = sharingList[j], sharingList[i]
    return {k: sharing[k] for k in sharingList}

def sortInfoByList(toSort, listSortBy):
    sortedInfos = []
    for id in listSortBy:
        for info in toSort:
            if id == info['steamid']:
                sortedInfos.append(info)
    return sortedInfos

def printSharing(sharing):
    convertedSharingList = [SteamID3_To_SteamID64(x) for x in list(sharing)]
    infos = userInfo(convertedSharingList)
    sInfos = sortInfoByList(infos, convertedSharingList)

    for i, info in enumerate(sInfos):
        print(f"<{i}>{info['steamid']} {info['personaname']}")


sharingRaw = extractFilePortion(f"{STEAM_PATH}\config\config.vdf", "AuthorizedDevice")
sharing = vdf.loads(sharingRaw)

flag = False
printSharing(sharing)
while not flag:
    sharing = modifyOrder(sharing)
    printSharing(sharing)
    if input("Contiue?(y/n)") != 'y':
        flag = True

sharingModfied = "{\n" + vdf.dumps(sharing, True)

modifyFilePortion(f"{STEAM_PATH}\config\config.vdf", sharingRaw, sharingModfied)