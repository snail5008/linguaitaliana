
# Guida

## Gestire i corpus

### Creare e eliminare corpus

**nel terminale**:
```
$ corpusmanager --crea-corpus "l'italiano nei romanzi del 19esimo secolo"
$ corpusmanager --elenca-corpus
[235624] "l'italiano nei romanzi del 19esimo secolo"
$ corpusmanager --corpus-attivo 235624
$ corpusmanager --archivia-corpus
Vuoi archiviare [235624] "l'italiano nei romanzi del 19esimo secolo" (S)ì/(N)o? S
$ corpusmanager --elenca-corpus
$
$ corpusmanager --elenca-corpus-archiviati
[235624] "l'italiano nei romanzi del 19esimo secolo"
$

```
**con l'interfaccia web**:
```
Inserisci degli immagini qui
```

### Aggiungere testi ai corpus

**nel terminale**:
```
$ corpusmanager --corpus-attivo [ID]
$ corpusmanager --collega-testo [ID] ./libri/test.txt
Collegato testo [12454123] "./libri/test.txt"
$ corpusmanager --elenca-testi
[12454123] "./libri/test.txt"
$ corpusmanager --scollega-testo 12454123
Scollegato testo [12454123] "./libri/test.txt"
```
**con l'interfaccia web**:
```
Inserisci degli immagini qui
```
