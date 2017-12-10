import wolframalpha
client = wolframalpha.Client("AAREUR-UVEWA5PATW")

#example: inputstatement = "What is the definite integral of 5 x squared from 1 to 3"
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
