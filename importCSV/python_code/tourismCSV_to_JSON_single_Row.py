import csv
import json
import jsonAdapter
from BigchainDBConnector import sendTransactionToBigChainDB

# step 1: key extraction
def createEmptyDictandKeys():
    # uses the file mapping.csv in witch json keys are mapped to csv columns.
    # returns the empty dict and
    outputDictDraft0 = {}
    mappingKeywordsToCSV = {}
    with open("mapping.csv", "r") as miocsv:
        reader = csv.reader(miocsv, delimiter=',', quotechar='"')
        filedata = list(reader)
        for d in filedata:  #
            mappingKeywordsToCSV[d[0]] = eval(d[1])
            outputDictDraft0[d[0]] = []
    return outputDictDraft0, mappingKeywordsToCSV
    # print(mappingKeywordsToCSV)

# Processing
# MAIN FUNCTION
# [reading CSV DATA and single row conversion in Dict]

# steps:
# Creates an empty dict and key mapping
# then for each key, it extracts the corresponding data from the csv
# then it does conversion 1 and conversion 2

def rowExtraction(row):
    outputDict={}
    with open("CSV_turisti2019.csv", "r") as myCSV:
        reader = csv.reader(myCSV, delimiter=',', quotechar='"')
        filedata = list(reader)
        outputDictDraft, mappingKeywordsToCSV = createEmptyDictandKeys()
        # for a given key:
        for j in mappingKeywordsToCSV.keys():
            for i in mappingKeywordsToCSV[j]:
                #print(filedata[row][i])
                outputDictDraft[j].append(filedata[row][i])
        outputDictData = jsonAdapter.conversion(outputDictDraft)
        outputDictData["Survey Type"]= "visitors"
        outputDict['data']=outputDictData
    return outputDict


def sendTX(row):
    # calls the function sendTransactionToBigChainDB to send the json of a given row number
    outputDict = rowExtraction(row)
    #assetdata = json.dumps(outputDict)
    sendTransactionToBigChainDB(outputDict)

if __name__ == "__main__":
    # USAGE
    # single row
    aRow = 300 # max index: 651
    sendTX(aRow)

    # save into JSON    # [alternatively you can perform the transaction here ]
    # with open("output"+str(aRow)+".json", "w") as jsonFile:
    #    jsonFile.write(json.dumps(outputDict))

    # # # for each element in the csv
    # for row in range(1, 651):
    #    sendTX(row)
    
    #    outputDict = rowExtraction(row)
    #    print(row, outputDict)
