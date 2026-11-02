import csv

FILE = "dati/carburanti-impianti-2026-10-13.csv"

def carica(nomefile):
 """Legge il file, converte i numeri, scarta le righe sporche.
 Restituisce la lista delle righe buone e il numero di righe scartate."""
 return [], 0


def domanda1(dati):
 """Risponde alla domanda 1 della scheda."""
 return None


def domanda2(dati):
    prezzi, impianti = dati
    benzina_self = [
        p["prezzo"]
        for p in prezzi
        if p["carb"].lower() == "benzina" and p["isSelf"] == "1"
    ]

    if not benzina_self:
        return None

    p_min = min(benzina_self)
    p_max = max(benzina_self)
    p_med = round(sum(benzina_self) / len(benzina_self), 3)

    return {"minimo": p_min, "massimo": p_max, "medio": p_med}

def domanda3(dati):
    prezzi, impianti = dati
    prov_somme = {}
    prov_conteggi = {}

    for p in prezzi:
        if p["carb"].lower() == "benzina" and p["isSelf"] == "1":
            id_imp = p["idImpianto"]
            if id_imp in impianti:
                prov = impianti[id_imp]["provincia"]
                prov_somme[prov] = prov_somme.get(prov, 0.0) + p["prezzo"]
                prov_conteggi[prov] = prov_conteggi.get(prov, 0) + 1

    tabella = []
    for prov in prov_somme:
        cnt = prov_conteggi[prov]
        media = round(prov_somme[prov] / cnt, 3)
        tabella.append([prov, media, cnt])

    tabella.sort(key=lambda x: x[1], reverse=True)
    return tabella

def domanda_nostra(dati):
    prezzi, impianti = dati
    bandita_somme = {}
    bandita_conteggi = {}

    for p in prezzi:
        if p["carb"].lower() == "benzina" and p["isSelf"] == "1":
            id_imp = p["idImpianto"]
            if id_imp in impianti:
                bandiera = impianti[id_imp]["bandiera"]
                bandita_somme[bandiera] = bandita_somme.get(bandiera, 0.0) + p["prezzo"]
                bandita_conteggi[bandiera] = bandita_conteggi.get(bandiera, 0) + 1

    risultati = []
    for bandiera in bandita_somme:
        cnt = bandita_conteggi[bandiera]
        if cnt >= 50:
            media = round(bandita_somme[bandiera] / cnt, 3)
            risultati.append((bandiera, media, cnt))

    risultati.sort(key=lambda x: x[1])
    return risultati[:5]


def scrivi_risultati(nomefile, intestazione, tabella):
 """Scrive la tabella in un CSV con csv.writer."""
 pass


def main():
 dati, scartate = carica(FILE)
 print(f"Righe buone: {len(dati)}, scartate: {scartate}")
 print("Domanda 1:", domanda1(dati))
 print("Domanda 2:", domanda2(dati))
 tabella = domanda3(dati)
 scrivi_risultati("risultati.csv", ["colonna1", "colonna2"], tabella)
 print("Domanda nostra:", domanda_nostra(dati))


main()
