import wolframalpha
import json

client = wolframalpha.Client("AAREUR-UVEWA5PATW")

def main(inputstatement):
    res = client.query(inputstatement)
    if (inputstatement.lower().find("indefinite integral")!=-1):
        answer = res.details["Indefinite integral"]
    elif (inputstatement.lower().find("definite integral")!=-1):
        answer = res.details["Definite integral"]
    elif (inputstatement.lower().find("derivative")!=-1):
        answer = res.details["Derivative"]
    elif (inputstatement.lower().find("taylor series")!= -1):
        answer = "Taylor series functionality is not yet implemented"
    elif (inputstatement.lower().find("limit") != -1):
        answer = res.details["Limit"]
    else:
        answer = res.details["Result"]
    return answer

def lambda_handler(event, context):
    print(main("Derivative of 2x"))
    print(main(event['request']['intent']['slots']['query']['value']))

#we need to put the key ['value'] into main.main() but parse for a different json key as output
