import urllib.request
import json

def main():
    urldata= "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    weburl = urllib.request.urlopen(urldata)
    print("Result Code: ", weburl.getcode())

    if(weburl.getcode() == 200):
        data=weburl.read()
        printResults(data)
    else:
        print("Cannot Parse the data")
def printResults(data):
    theJson = json.loads(data)
    if "title" in theJson["metadata"]:
        print(theJson["metadata"]["title"])
    count = theJson["metadata"]["count"]
    print(str(count)+" Events recorded")

    for i in theJson["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" %i["properties"]["mag"], i["properties"]["place"])
        # print(i["properties"]["place"])

    print("Events that were felt-------------------\n")
    for i in theJson["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0 :
                print("%2.1f" %i["properties"]["mag"], i["properties"]["place"], "reported"+str(i["properties"]["felt"])+" times")
        

main()