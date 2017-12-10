import wolframalpha
import json

client = wolframalpha.Client("AAREUR-UVEWA5PATW")

def main(inputstatement):
    if (inputstatement.lower().find("indefinite integral")!=-1):
        inputstatement = inputstatement[inputstatement.lower().find("indefinite integral"):]
        res = client.query(inputstatement)
        answer = res.details["Indefinite integral"]
    elif (inputstatement.lower().find("definite integral")!=-1):
        inputstatement = inputstatement[inputstatement.lower().find("definite integral"):]
        res = client.query(inputstatement)
        answer = res.details["Definite integral"]
    elif (inputstatement.lower().find("derivative")!=-1):
        inputstatement = inputstatement[inputstatement.lower().find("derivative"):]
        res = client.query(inputstatement)
        answer = res.details["Derivative"]
    elif (inputstatement.lower().find("taylor series")!= -1):
        answer = "Taylor series functionality has not currently been implemented"
    elif (inputstatement.lower().find("limit") != -1):
        inputstatement = inputstatement[inputstatement.lower().find("limit"):]
        res = client.query(inputstatement)
        answer = res.details["limit"]
    else:
        answer = "Invalid calculation"

    return answer

def lambda_handler(event, context):
    output = main(event['request']['intent']['slots']['query']['value'])

    return {"version":"1.0","response":{"outputSpeech":{"type":"PlainText","text":output}},"sessionAttributes":{}}

#we need to put the key ['value'] into main.main() but parse for a different json key as output
