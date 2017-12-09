import wolframalpha

client = wolframalpha.Client("AAREUR-UVEWA5PATW")
res = client.query("Integral of sin(x) dx")

print (res.details["Indefinite integral"])
