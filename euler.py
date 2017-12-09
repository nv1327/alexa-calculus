import wolframalpha

client = wolframalpha.Client("AAREUR-UVEWA5PATW")
res = client.query("What is e to the (i pi)")

print(res.details["Result"])
