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
    prezzi_benzina_self = [
        d['prezzo'] for d in dati 
        if 'benzina' in d['tipo_carb'] and 'self' in d['modalita']
    ]
    if not prezzi_benzina_self:
        return "Nessun dato disponibile per benzina self."
    prezzi_ordinati = sorted(prezzi_benzina_self)
    minimo = prezzi_ordinati[0]
    massimo = prezzi_ordinati[-1]
    medio = sum(prezzi_ordinati) / len(prezzi_ordinati)
    cinque_piu_bassi = prezzi_ordinati[:5]
    cinque_piu_alti = prezzi_ordinati[-5:]
    return {
        "minimo": minimo,
        "massimo": massimo,
        "medio": round(medio, 3),
        "5_piu_bassi": cinque_piu_bassi,
        "5_piu_alti": cinque_piu_alti
    }

def domanda3(dati):
    prov_prezzi = defaultdict(list)
    for d in dati:
        if 'benzina' in d['tipo_carb'] and 'self' in d['modalita']:
            prov_prezzi[d['provincia']].append(d['prezzo'])
    medie_provincia = []
    for prov, prezzi in prov_prezzi.items():
        if prezzi:
            media = sum(prezzi) / len(prezzi)
            medie_provincia.append((prov, round(media, 3)))
    medie_provincia.sort(key=lambda x: x[1], reverse=True)
    posizione_bs = None
    for i, (prov, media) in enumerate(medie_provincia, start=1):
        if prov.upper() == 'BS':
            posizione_bs = i
            break
    print(f"Posizione di Brescia (BS) nella classifica provinciale: {posizione_bs}")
    tabella = [[prov, media] for prov, media in medie_provincia]
    return tabella

def domanda_nostra(dati):
    """La domanda inventata dal gruppo."""
    return None


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