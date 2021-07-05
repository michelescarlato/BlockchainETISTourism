import json


def loadJson(filename):
    stringaJson = ""
    with open(filename, "r") as fileDaLeggere:
        for line in fileDaLeggere:
            stringaJson += line
    return json.loads(stringaJson)


# phase 1: multiple choice

def conversion1(inputData):  # ,values=""):
    outputData = {}
    keys = inputData.keys()
    for k in keys:
        if len(inputData[k]) > 1:
            # print(k, inputData[k],values[k])
            answerList = []

            for i in range(len(inputData[k])):
                answer = inputData[k][i]
                if answer == "S\u00ec":
                    answerList.append(multiple_choice_conversion[k][i])
            # print(answerList)
            outputData[k] = answerList
        elif len(inputData[k]) == 1:
            outputData[k] = inputData[k][0]
            if (outputData[k] == "S\u00ec"):
                outputData[k] = True
            elif (outputData[k] == "No"):
                outputData[k] = False
            elif (outputData[k] == "N/A"):
                outputData[k] = ""
        if k == 'Annual Household' and len(outputData[k]) != 0:
            outputData[k] = outputData[k][0]
        if k == "spend per day" and len(outputData[k]) != 0:
            outputData[k] = outputData[k][0:-1] + "EURO"
    return outputData


# phase2: single choice translation
def conversion2(inputData):
    for k in inputData.keys():

        try:
            if k in single_choice_questions.keys():
                inputData[k] = single_choice_questions[k][inputData[k]]
        except:
            pass
    return (inputData)


def conversion(inputData):
    return (conversion2(conversion1(inputData)))


# print(valueDict)

multiple_choice_conversion = {
    'Purpose': ['Holiday', 'Visiting relatives and friends', 'Work or business purposes', 'Conferences and exhibitions',
                'Education and training', 'Health', 'Religion/pilgrimages', 'Shopping', 'In transit'],
    'how many': ['Alone', 'With friends', 'With family', 'Organized group'],
    'primary transport': ['Train', 'Motorcycle', 'Airplane', 'Bicycle', 'Bus', 'Walk', 'Car', 'Caravan',
                          'Boat / Ship / Ferry', 'Own, friends, firm', 'Hired'],
    'method transport here': ['Train', 'Motorcycle', 'Airplane', 'Bicycle', 'Bus', 'Walk', 'Car', 'Caravan',
                              'Boat / Ship / Ferry', 'Own, friends, firm', 'Hired'],
    'Interesting Features': ['Beach facilities', 'Accessibility', 'Historic interest', 'Peace and quiet',
                             'Entertainment and recreation activities', 'Scenery and countryside', 'A particular event',
                             'Friendliness and hospitality of locals'],
    'kind of accommodation': ['Hotel / Resort / Motel', 'Rented house, flat, unit, etc.', 'Own property',
                              "Friend's / Relative's home", 'Bed and Breakfast or Guest home', 'Serviced apartment',
                              'Bungalow Cabin / Tent in a camping park', 'Holiday farm', 'Boat', 'Boat'],
    'Annual Household': ['Low (under 30.000 euros)', 'Medium (from 30.000 to 60.000 euros)', 'High (over 60.000 euros)',
                         'I prefer not to answer']
}

single_choice_questions = {
    'Gender': {
        'M': 'Male',
        'F': 'Female',
        '': 'Other'},
    'age': ['15-24', '25-49', '50-64', '65-79', '=>80'],
    'spend per day': ['< 25 EUR', '25 - 50 EUR', '50 - 100 EUR', '100 - 150 EUR', '150 - 200 EUR', '> 200 EUR'],
    'expenses': {'Nella cifra che aveva preventivato': 'Within what was planned',
                 'Più alta della cifra che aveva preventivato': 'Higher than planned',
                 'Più bassa della cifra che aveva preventivato': 'Cheaper than planned'
                 },
    'special needs': {
        "Molto d'accordo": 'Strongly agree',
        "D'accordo": 'Agree',
        'Neutrale': 'Neutral',
        'In disaccordo': 'Disagree',
        'Molto in disaccordo': 'Strongly Disagree'},

    'Overall Satisfaction': {
        "Molto d'accordo": 'Strongly agree',
        "D'accordo": 'Agree',
        "Moderatamente d'accordo": 'Moderately Agree',
        "Leggermente d'accordo": 'Slightly Agree',
        'Né in accordo né in disaccordo': 'Neither Agree Nor Disagree',
        'Neutrale': 'Neither Agree Nor Disagree',
        "Moderatamente in disaccordo": 'Moderately Disagree',
        'Leggermente in disaccordo': 'Slightly Disagree',
        'In disaccordo': 'Disagree',
        "Molto in disaccordo": 'Strongly Disagree',
        'Non so': 'I don’t know'},

    'Disability considerations': {
        "Molto d'accordo": 'Strongly agree',
        "D'accordo": 'Agree',
        "Moderatamente d'accordo": 'Moderately Agree',
        "Leggermente d'accordo": 'Slightly Agree',
        'Né in accordo né in disaccordo': 'Neither Agree Nor Disagree',
        'Neutrale': 'Neither Agree Nor Disagree',
        "Moderatamente in disaccordo": 'Moderately Disagree',
        'Leggermente in disaccordo': 'Slightly Disagree',
        'In disaccordo': 'Disagree',
        "Molto in disaccordo": 'Strongly Disagree',
        'Non so': 'I don’t know'},

    'Highest Degree': {
        'Non ho completato nessun livello': 'No schooling completed',
        'Elementari': 'Primary school',
        'Medie': 'Secondary school completed',
        'Diploma di Scuola superiore': 'High school graduate',
        'Scuola di specializzazione': 'Vocational schools',
        'Laurea triennale': "Bachelor’s degree",
        'Laurea specialistica/magistrale': "Master’s degree",
        'Laurea magistrale (vecchio ordinamento)': "Master’s degree",
        'Dottorato': 'Doctoral',
        'Preferisco non rispondere': 'I prefer not to answer'},

    'Professional Status': {
        'Studente': 'Student',
        'Pensionato': 'Retired',
        'Non occupato': 'Unemployed',
        'Impossibilitato a lavorare': 'Unable to work',
        'Dipendente stipendiato part-time': 'Part-time employed for wages',
        'Dipendente stipendiato full time': 'Full time employed for wages',
        'Autonomo': 'Self-employed',
        'Preferisco non rispondere': 'I prefer not to answer'
    }
}

# debugging
if __name__ == '__main__':
    outputDictDraft = loadJson('outputDraft.json')
    jsonAdmittedValuesDict = loadJson("jsonAnswersCompleted.json")
    valueDict = jsonAdmittedValuesDict
    try:
        valueDict = jsonAdmittedValuesDict['asset']['data']
    except:
        pass

    outputDictSecondDraft = conversion1(outputDictDraft)
    print(outputDictSecondDraft)

    with open("outputDraft2.json", "w") as jsonFile:
        jsonFile.write(json.dumps(outputDictSecondDraft))
