

with open("1.txt") as f:
    contenuti = f.read()

def aggiungi_token(tipo, token, tokens):
    if token != "":
        tokens.append({ "tipo": tipo, "valore": token })

PUNTEGGIATURA = [',', '.', '(', ')', '-', '—', '?', '!']

token = ""
tokens = []
for i in contenuti:
    if i == " ":
        aggiungi_token("testo", token, tokens)
        token = ""
    elif i in PUNTEGGIATURA:
        aggiungi_token("testo", token, tokens)
        aggiungi_token("punteggiatura", i, tokens)
        token = ""
    elif i == "\n":
        aggiungi_token("testo", token, tokens)
        token = ""
    else:
        token += i

frequenza = {}

for i in tokens:
    if i["tipo"] == "testo":
        if i["valore"].lower() in frequenza.keys():
            frequenza[i["valore"].lower()] += 1
        else:
            frequenza[i["valore"].lower()] = 1

for i in sorted(frequenza, key=lambda parola: frequenza[parola]):
    print(i + "]" + (30 - (len(i + "]"))) * " " + "#" * frequenza[i])
