from bs4 import BeautifulSoup
import requests

## Lo script va modificato in base alle esigenze del lavoro:
## 1- È modificabile la struttura di content.find() in modo da ricercare contenuti diversi da "div" nel caso in cui
##    la pagina html in questione abbia il testo della poesia in un altra sezione.
## 2- È modificabile il path dove salvare il .txt finale. È inoltre necessario modificare il nome della cartella in
##    modo da salvare testi di autori diversi in diverse cartelle.

## NB: il seguente script richiede di fornire a python i link alle poesie. È dunque necessario un comportamento
##     attivo dell'utente. È possibile ottimizzare lo script per leggere pagine diverse da wikisource.org.

while True:
    i = 1
    while True:
        url = input("Inserisci il link alla poesia su Wikisource.org ")
        response = requests.get(url)
        content = BeautifulSoup(response.content, "html.parser")
        title = content.find('div', attrs={"class":"centertext ct"})
        poesia = []
        for div in content.findAll('div', attrs={"class":"poem"}):
            poesia.append(div.text)
            with open("D:/Minor/Dati_digitali/PROGETTO/poeti_prove/<CARTELLA CON NOME AUTORE>/poesia%s.txt" % i, "w",encoding="utf-8") as output:
                output.write(" ".join(poesia))
        i = i + 1

