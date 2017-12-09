import wolframalpha

client = wolframalpha.Client("AAREUR-UVEWA5PATW")
res = client.query("What is the limit of x to the x as x approaches 0 plus")

print(res.details["Limit"])
