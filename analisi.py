import json

FILE_IMPIANTI = "dati/carburanti-impianti-2026-10-13.json"
FILE_PREZZI = "dati/carburanti-prezzi-2026-10-13.json"


def _estrai_campi(elemento):
    if isinstance(elemento, dict):
        if len(elemento) == 1:
            valore = next(iter(elemento.values()))
            if isinstance(valore, str):
                return valore.split("|")
        return elemento
    if isinstance(elemento, str):
        return elemento.split("|")
    return None


def carica_impianti(nomefile):
    impianti = {}
    scartate = 0
    with open(nomefile, "r", encoding="utf-8", errors="ignore") as f:
        dati_raw = json.load(f)

    if not isinstance(dati_raw, list):
        return impianti, 1

    for idx, elemento in enumerate(dati_raw):
        campi = _estrai_campi(elemento)
        if isinstance(campi, list):
            if idx == 0 and campi and campi[0].strip().lower() == "idimpianto":
                continue
            if len(campi) >= 10:
                id_imp = campi[0].strip()
                impianti[id_imp] = {
                    "bandiera": campi[2].strip(),
                    "comune": campi[6].strip(),
                    "provincia": campi[7].strip()
                }
            else:
                scartate += 1
        elif isinstance(campi, dict):
            id_imp = str(campi.get("idImpianto", "")).strip()
            if id_imp:
                impianti[id_imp] = {
                    "bandiera": str(campi.get("Bandiera", campi.get("bandiera", ""))).strip(),
                    "comune": str(campi.get("Comune", campi.get("comune", ""))).strip(),
                    "provincia": str(campi.get("Provincia", campi.get("provincia", ""))).strip()
                }
            else:
                scartate += 1
        else:
            scartate += 1

    return impianti, scartate


def carica_prezzi(nomefile):
    dati = []
    scartate = 0
    with open(nomefile, "r", encoding="utf-8", errors="ignore") as f:
        dati_raw = json.load(f)

    if not isinstance(dati_raw, list):
        return dati, 1

    for idx, elemento in enumerate(dati_raw):
        campi = _estrai_campi(elemento)
        if isinstance(campi, list):
            if idx == 0 and campi and campi[0].strip().lower() == "idimpianto":
                continue
            if len(campi) >= 4:
                try:
                    dati.append({
                        "idImpianto": campi[0].strip(),
                        "descCarburante": campi[1].strip(),
                        "prezzo": float(campi[2].strip()),
                        "isSelf": campi[3].strip()
                    })
                except ValueError:
                    scartate += 1
            else:
                scartate += 1
        elif isinstance(campi, dict):
            try:
                dati.append({
                    "idImpianto": str(campi.get("idImpianto", "")).strip(),
                    "descCarburante": str(campi.get("descCarburante", "")).strip(),
                    "prezzo": float(str(campi.get("prezzo", "")).strip()),
                    "isSelf": str(campi.get("isSelf", "")).strip()
                })
            except (ValueError, TypeError):
                scartate += 1
        else:
            scartate += 1

    return dati, scartate


def domanda1(impianti, prezzi, scartate_impianti, scartate_prezzi):
    tot_distributori = len(impianti)
    tot_scartate = scartate_impianti + scartate_prezzi
    tipi_carburante = set(p["descCarburante"] for p in prezzi)
    self_count = sum(1 for p in prezzi if p["isSelf"] == "1")
    servito_count = sum(1 for p in prezzi if p["isSelf"] == "0")
    return {
        "distributori": tot_distributori,
        "scartate": tot_scartate,
        "num_tipi": len(tipi_carburante),
        "self": self_count,
        "servito": servito_count
    }


def domanda2(prezzi):
    benzina_self = [
        p["prezzo"] for p in prezzi
        if p["descCarburante"].lower() == "benzina" and p["isSelf"] == "1"
    ]
    if not benzina_self:
        return None
    return {
        "minimo": min(benzina_self),
        "massimo": max(benzina_self),
        "medio": round(sum(benzina_self) / len(benzina_self), 3)
    }


def domanda3(prezzi, impianti):
    prov_somme = {}
    prov_conteggi = {}
    for p in prezzi:
        if p["descCarburante"].lower() == "benzina" and p["isSelf"] == "1":
            id_imp = p["idImpianto"]
            if id_imp in impianti:
                prov = impianti[id_imp]["provincia"]
                if not prov:
                    continue
                prov_somme[prov] = prov_somme.get(prov, 0.0) + p["prezzo"]
                prov_conteggi[prov] = prov_conteggi.get(prov, 0) + 1
    tabella = []
    for prov in prov_somme:
        cnt = prov_conteggi[prov]
        media = round(prov_somme[prov] / cnt, 3)
        tabella.append([prov, media, cnt])
    tabella.sort(key=lambda x: x[1], reverse=True)
    return tabella


def domanda_nostra(prezzi):
    impianti_prezzi = {}
    for p in prezzi:
        if p["descCarburante"].lower() == "benzina":
            id_imp = p["idImpianto"]
            if id_imp not in impianti_prezzi:
                impianti_prezzi[id_imp] = {}
            if p["isSelf"] == "1":
                impianti_prezzi[id_imp]["self"] = p["prezzo"]
            elif p["isSelf"] == "0":
                impianti_prezzi[id_imp]["servito"] = p["prezzo"]

    differenze = []
    for id_imp in impianti_prezzi:
        imp = impianti_prezzi[id_imp]
        if "self" in imp and "servito" in imp:
            differenze.append(imp["servito"] - imp["self"])

    if not differenze:
        return 0.0
    return round(sum(differenze) / len(differenze), 3)


def scrivi_risultati_json(nomefile, intestazione, tabella):
    risultati = [
        {
            intestazione[0]: riga[0],
            intestazione[1]: riga[1],
            intestazione[2]: riga[2]
        }
        for riga in tabella
    ]
    with open(nomefile, "w", encoding="utf-8") as f:
        json.dump(risultati, f, ensure_ascii=False, indent=2)


def main():
    print("Caricamento dei file JSON in corso...")
    impianti, scartate_imp = carica_impianti(FILE_IMPIANTI)
    prezzi, scartate_prz = carica_prezzi(FILE_PREZZI)

    print("\n" + "=" * 50)
    print(" RIEPILOGO CARICAMENTO DATI")
    print("=" * 50)
    print(f"• Impianti correttamente caricati: {len(impianti)} (Scartati: {scartate_imp})")
    print(f"• Prezzi correttamente caricati: {len(prezzi)} (Scartati: {scartate_prz})")

    d1 = domanda1(impianti, prezzi, scartate_imp, scartate_prz)
    print("\n" + "=" * 50)
    print(" DOMANDA 1: Statistiche Generali")
    print("=" * 50)
    print(f"• Totale distributori in anagrafica : {d1['distributori']:,}")
    print(f"• Totale righe scartate (complessivo): {d1['scartate']}")
    print(f"• Tipi di carburante differenti    : {d1['num_tipi']}")
    print(f"• Rilevazioni modalità Self-service  : {d1['self']:,}")
    print(f"• Rilevazioni modalità Servito     : {d1['servito']:,}")

    d2 = domanda2(prezzi)
    print("\n" + "=" * 50)
    print(" DOMANDA 2: Benzina Self-Service in Italia")
    print("=" * 50)
    if d2:
        print(f"• Prezzo minimo : {d2['minimo']:.3f} €/L")
        print(f"• Prezzo massimo: {d2['massimo']:.3f} €/L")
        print(f"• Prezzo medio  : {d2['medio']:.3f} €/L")

    tabella = domanda3(prezzi, impianti)
    scrivi_risultati_json("risultati.json", ["provincia", "prezzo_medio", "numero_prezzi"], tabella)
    print("\n" + "=" * 50)
    print(" DOMANDA 3: Prezzo Medio per Provincia")
    print("=" * 50)
    print(f"• Calcolate le medie per {len(tabella)} province.")
    print("• File 'risultati.json' generato con successo.")
    print("• Top 3 province più care:")
    for i, row in enumerate(tabella[:3], 1):
        print(f"  {i}. {row[0]}: {row[1]:.3f} €/L (su {row[2]} impianti)")
    print("• Top 3 province più economiche:")
    for i, row in enumerate(tabella[-3:], 1):
        print(f"  {i}. {row[0]}: {row[1]:.3f} €/L (su {row[2]} impianti)")

    dn = domanda_nostra(prezzi)
    print("\n" + "=" * 50)
    print(" DOMANDA NOSTRA: Differenza Media Servito vs Self (Benzina)")
    print("=" * 50)
    print(f"• Differenza media di prezzo: +{dn} €/L (circa {dn * 100:.1f} centesimi al litro)")
    print("=" * 50)


if __name__ == "__main__":
    main()
