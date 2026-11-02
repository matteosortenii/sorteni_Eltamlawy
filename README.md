# Progetto 1 - Prezzi Carburanti

## Gruppo
- Fares Eltamlawy: domanda_nostra, domanda2, domanda3, README.
- Matteo Sorteni: carica_impianti, carica_prezzi, domanda1,  scrivi_risultati.


## Il dataset
- **Fonte:** Ministero delle Imprese e del Made in Italy (MIMIT), portale Open Data.
- **Data dei dati:** Estrazione del 13/10/2026.
- **Dimensioni:** 
  - File anagrafica impianti: 23.929 righe, 10 colonne.
  - File prezzi: 92.703 righe, 5 colonne.


## Com'è fatto il file
- **Separatore:** Carattere pipe (`|`).
- **Intestazione:** La prima riga contiene la dicitura "Estrazione del...", seguita dalla vera riga di intestazione delle colonne.
- **Colonne utilizzate:** 
  - Anagrafica (`idImpianto`, `Bandiera`, `Comune`, `Provincia`).
  - Prezzi (`idImpianto`, `descCarburante`, `prezzo`, `isSelf`).
- **Valori mancanti o anomali:** Presenza di righe con formattazione particolare o campi irregolari. Nel file anagrafica è stata riscontrata una virgoletta non chiusa che richiedeva l'uso di `QUOTE_NONE` per evitare la corruzione del parsing.


## Dati scartati
- **Righe scartate:** Durante il caricamento, le righe con colonne insufficienti o con valori di prezzo non convertibili in formato numerico (`ValueError`) sono state scartate e conteggiate dal programma.


## Risposte
1. **Statistiche generali:** Il dataset comprende 23.929 distributori distinti in anagrafica, 51.118 rilevazioni in modalità self-service e 41.585 in modalità servito, con un totale di 59 tipologie di carburante censite.
2. **Benzina self-service in Italia:** Prezzo minimo di **1.206 €/L** (registrato a Livigno per regime di zona franca), prezzo massimo di **2.869 €/L** (rilevato a Milano, probabilmente un'anomalia di inserimento), e un prezzo medio nazionale di **2.035 €/L**.
3. **Prezzo medio per provincia:** La classifica completa con le medie provinciali e il numero di rilevazioni è stata scritta correttamente nel file `risultati.csv`.


## La nostra domanda
- **Quesito:** Qual è la differenza media di prezzo (in centesimi al litro) tra la modalità servito e la modalità self-service per la benzina in Italia?
- **Risultato:** La differenza media registrata è di **+0.139 €/L** (pari a circa **13.9 centesimi al litro** in più per il servito rispetto al self).
- **Commento:** Il dato conferma il risparmio concreto garantito dalla modalità self-service per gli automobilisti su scala nazionale.


## Come si lancia
Mettere i file del dataset nella cartella `dati/` e lanciare da terminale:
```bash
python analisi.py
