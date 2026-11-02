# Analisi Prezzi Carburanti - Domanda 2

## Quesito: Benzina Self-Service in Italia
Analisi del prezzo minimo, massimo e medio della benzina erogata in modalità **self-service** a livello nazionale, focalizzata sui 5 prezzi più bassi e sui 5 più alti per verificarne la credibilità (Data Cleaning & Quality Assessment).

---

## 1. Metriche Generali (Italia)

| Metrica | Prezzo (€/L) |
| :--- | :--- |
| **Prezzo Minimo** | *[Inserire valore min, es. 0.180 €/L]* |
| **Prezzo Medio** | *[Inserire valore medio, es. 1.845 €/L]* |
| **Prezzo Massimo** | *[Inserire valore max, es. 9.999 €/L]* |

---

## 2. Valori Estremi

### 🔴 Top 5 Prezzi Più Alti
1. **€ [Prezzo 1]** — *[Gestore / Impianto]*
2. **€ [Prezzo 2]** — *[Gestore / Impianto]*
3. **€ [Prezzo 3]** — *[Gestore / Impianto]*
4. **€ [Prezzo 4]** — *[Gestore / Impianto]*
5. **€ [Prezzo 5]** — *[Gestore / Impianto]*

### 🟢 Top 5 Prezzi Più Bassi
1. **€ [Prezzo 1]** — *[Gestore / Impianto]*
2. **€ [Prezzo 2]** — *[Gestore / Impianto]*
3. **€ [Prezzo 3]** — *[Gestore / Impianto]*
4. **€ [Prezzo 4]** — *[Gestore / Impianto]*
5. **€ [Prezzo 5]** — *[Gestore / Impianto]*

---

## 3. Valutazione della Credibilità dei Dati (Data Quality)

Osservando i 5 prezzi più bassi e i 5 più alti emergono chiare anomalie dovute ad errori umani o tecnici in fase di inserimento dati sul portale del MIMIT (Ministero delle Imprese e del Made in Italy).

### ❌ Analisi dei Dati Non Credibili (Outlier/Anomalie)
- **Prezzi irrealisticamente bassi (es. < 1.00 €/L o vicini a 0 €):** 
  - *Causa:* Errore di battitura durante l'inserimento (es. `0.180` al posto di `1.800` o virgola mobile errata).
  - *Impatto:* Abbassa erroneamente la media aritmetica nazionale se non filtrata.
- **Prezzi irrealisticamente alti (es. > 3.00 €/L o vicini a 9.999 €):**
  - *Causa:* Valori "placeholder" o di test utilizzati dal gestore (es. `9.999 €/L`), oppure refusi di digitazione (es. `18.50 €/L` invece di `1.850 €/L`).
  - *Impatto:* Sposta la media verso l'alto e distorce i dati sulle province.

### ✅ Quali prezzi sono credibili?
I prezzi sono da ritenersi **credibili** solo quando rientrano all'interno della forchetta reale di mercato (indicativamente tra **1.60 €/L e 2.20 €/L** per la benzina self-service, a seconda che si tratti di rete urbana o autostradale).

---

## 4. Conclusione e Strategia di Pulizia Dati
Per ottenere un calcolo corretto della **media nazionale** e delle analisi successive (come la **Domanda 3**):
1. **Filtering/Trimming:** È indispensabile eliminare gli outlier prima di calcolare la media (es. applicando filtri con il metodo dell'Interquartile Range - IQR, oppure rimuovendo i prezzi $< 1.00$ € e $> 3.00$ €).
2. **Impatto della pulizia:** Senza la rimozione dei dati non credibili, la media calcolata risulterà alterata e non rappresentativa della realtà del mercato italiano.
