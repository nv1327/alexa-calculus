import wolframalpha

client = wolframalpha.Client("AAREUR-UVEWA5PATW")
res = client.query("Integral of sin(x) dx from 0 to 1")

print (res.details["Definite integral"])
