import wolframalpha

client = wolframalpha.Client("AAREUR-UVEWA5PATW")
res = client.query("Derivative of sin(x)")

#print (res.details["Indefinite integral"])
print(res.details["Derivative"])
