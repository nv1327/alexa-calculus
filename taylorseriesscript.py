import wolframalpha

client = wolframalpha.Client("AAREUR-UVEWA5PATW")
res = client.query("Taylor series of e to the x at x=2")

#print (res.details["Indefinite integral"])
print(res.details["Series expansion at x=2"])
