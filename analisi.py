import csv

FILE_IMPIANTI = "dati/carburanti-impianti-2026-10-13.csv"
FILE_PREZZI = "dati/carburanti-prezzi-2026-10-13.csv"

def carica_impianti(nomefile):
    """Carica l'anagrafica degli impianti gestendo la virgoletta anomala."""
    impianti = {}
    scartate = 0
    with open(nomefile, "r", encoding="utf-8", newline="") as f:
        f.readline() # Salta la riga "Estrazione del..."
        reader = csv.reader(f, delimiter="|", quoting=csv.QUOTE_NONE)
        for riga in reader:
            if len(riga) >= 10:
                id_imp = riga[0]
                impianti[id_imp] = {
                    "bandiera": riga[1],
                    "comune": riga[5],
                    "provincia": riga[6]
                }
            else:
                scartate += 1
    return impianti, scartate


def carica_prezzi(nomefile):
    """Carica il file dei prezzi dei carburanti."""
    dati = []
    scartate = 0
    with open(nomefile, "r", encoding="utf-8", newline="") as f:
        f.readline() # Salta la riga "Estrazione del..."
        reader = csv.reader(f, delimiter="|")
        for riga in reader:
            if len(riga) >= 4:
                try:
                    dati.append({
                        "idImpianto": riga[0],
                        "descCarburante": riga[1],
                        "prezzo": float(riga[2]),
                        "isSelf": int(riga[3])
                    })
                except ValueError:
                    scartate += 1
            else:
                scartate += 1
    return dati, scartate


def domanda1(impianti, prezzi, scartate_impianti, scartate_prezzi):
    """Risponde alla domanda 1 del dataset carburanti combinando impianti e prezzi."""
    
    # 1. Quanti distributori ci sono nell'anagrafica?
    tot_distributori = len(impianti)
    
    # 2. Quante righe scartate e perché?
    tot_scartate = scartate_impianti + scartate_prezzi
    motivo_scarto = "Righe vuote, con colonne insufficienti o con formato errato."
    
    # 3. Quanti tipi di carburante diversi compaiono?
    tipi_carburante = set(p["descCarburante"] for p in prezzi)
    
    # 4. Quanti prezzi sono self e quanti servito?
    self_count = sum(1 for p in prezzi if p["isSelf"] == 1)
    servito_count = sum(1 for p in prezzi if p["isSelf"] == 0)
    
    return {
        "distributori": tot_distributori,
        "scartate": tot_scartate,
        "motivo": motivo_scarto,
        "tipi": list(tipi_carburante),
        "num_tipi": len(tipi_carburante),
        "self": self_count,
        "servito": servito_count
    }


def domanda2(dati):
    """Risponde alla domanda 2."""
    return None


def domanda3(dati):
    """Risponde alla domanda 3. Restituisce la tabella
    che finirà in risultati.csv: una lista di righe."""
    return []


def domanda_nostra(dati):
    """La domanda inventata dal gruppo."""
    return None


def scrivi_risultati(nomefile, intestazione, tabella):
    """Scrive la tabella in un CSV con csv.writer."""
    pass

def main():
    # 1. Carichiamo entrambi i file
    impianti, scartate_imp = carica_impianti(FILE_IMPIANTI)
    prezzi, scartate_prz = carica_prezzi(FILE_PREZZI)
    
    print(f"Impianti caricati: {len(impianti)}, scartati: {scartate_imp}")
    print(f"Prezzi caricati: {len(prezzi)}, scartati: {scartate_prz}")
    
    # 2. Chiamiamo la domanda 1 passando tutti e 4 i dati richiesti
    d1 = domanda1(impianti, prezzi, scartate_imp, scartate_prz)
    print("--- DOMANDA 1 ---")
    print(f"Distributori in anagrafica: {d1['distributori']}")
    print(f"Righe scartate totali: {d1['scartate']}")
    print(f"Tipi di carburante: {d1['tipi']}")
    print(f"Prezzi Self: {d1['self']}, Servito: {d1['servito']}")
    
    print("Domanda 2:", domanda2(prezzi))
    
    tabella = domanda3(prezzi)
    scrivi_risultati("risultati.csv", ["provincia", "prezzo_medio", "numero_prezzi"], tabella)
    print("Domanda nostra:", domanda_nostra(prezzi))

main()