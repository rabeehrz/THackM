
import spacy

def sortIt(sortTable):
    for i in range(0, len(sortTable)-1):
        for j in range(0, len(sortTable)-1-i):
            if(sortTable[j]["compatibilityValue"] < sortTable[j+1]["compatibilityValue"]):
                temp = sortTable[j]
                sortTable[j] = sortTable[j+1]
                sortTable[j+1] = temp
    
    return sortTable
def findLawyer(description, lawyersList):
    print("Start")
    nlp = spacy.load("en_core_web_md")  # make sure to use larger model!

    # description=input()

    tokens = nlp(description)
    testToken =[ {"key": 319, "value": nlp("hurt")},{"key": 300, "value": nlp("murder")},{"key": 304, "value": nlp("Dowry")},{"key": 312, "value": nlp("miscarriage")}]

    keyOutput = []
    ipc_code = []
    print("Test 1")
    for token in testToken:
        similarityValue = tokens.similarity(token["value"])
        print(tokens.text, token["value"].text, similarityValue)
        if(similarityValue > .5):
            keyOutput.append({"key": token["key"], "value": 1})
            ipc_code.append(token["key"])
        else:
            keyOutput.append({"key": token["key"], "value": 0})

    


    # lawyersList=[{"ipc":[{'key': 319, 'value': 6}, {'key': 300, 'value': 2}, {'key': 304, 'value': 0}, {'key': 312, 'value': 3}], "name": "Person1", "id": 1},{"ipc":[{'key': 319, 'value': 6}, {'key': 300, 'value': 0}, {'key': 304, 'value': 1}, {'key': 312, 'value': 4}], "name": "Person2", "id": 2}]

    victimDetails = keyOutput

    compatibility = []

    for lawyer in lawyersList:
        print(lawyer["ipc"])
        tempValue = 0

        for index in range(0,len(lawyer["ipc"])):
            # print(x)
            x = lawyer["ipc"][index]["value"]
            for yy in range(len(keyOutput)):
                y = victimDetails[yy]["value"]
                if(lawyer["ipc"][index]["key"] == victimDetails[index]["key"]):
                    tempValue = tempValue + x*y

        print(tempValue)
        # print(ipc_code)
        
        compatibility.append({"id": lawyer["id"], "name": lawyer["name"], "compatibilityValue": tempValue})

    finalCompatibility = sortIt(compatibility)
    finalCompatibility.append(ipc_code)
    return(finalCompatibility)

