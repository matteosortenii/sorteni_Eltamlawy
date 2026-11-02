# Analisi Prezzi Carburanti - Domanda 2

## Quesito: Benzina Self-Service in Italia
Analisi del prezzo minimo, massimo e medio della benzina erogata in modalità **self-service** a livello nazionale, focalizzata sui 5 prezzi più bassi e sui 5 più alti per verificarne la credibilità (Data Cleaning & Quality Assessment).

---

## 1. Metriche Generali (Italia)

| Metrica | Prezzo (€/L) |
| :--- | :--- |
| **Prezzo Minimo** | 1.206 €/L |
| **Prezzo Medio** | 2.035 €/L |
| **Prezzo Massimo** | 2.869 €/L |

---

## 2. Valori Estremi

### 🔴 Top 5 Prezzi Più Alti
1. **€ 2.869** — *Api-Ip / Milano (MI)*
2. **€ 2.763** — *Pompe Bianche / Capraia Isola (LI)*
3. **€ 2.699** — *San Marco Petroli / Bolzano Vicentino (VI) - Autostrada A31*
4. **€ 2.699** — *Pompe Bianche / Lampedusa e Linosa (AG)*
5. **€ 2.699** — *San Marco Petroli / Bolzano Vicentino (VI) - Autostrada A31*

### 🟢 Top 5 Prezzi Più Bassi
1. **€ 1.206** — *Agip Eni / Livigno (SO)*
2. **€ 1.206** — *Agip Eni / Livigno (SO)*
3. **€ 1.249** — *Q8 / Gravina di Catania (CT)*
4. **€ 1.558** — *Pompe Bianche / Rieti (RI)*
5. **€ 1.564** — *Pompe Bianche / Viterbo (VT)*

---

## 3. Valutazione della Credibilità dei Dati (Data Quality)

Osservando i 5 prezzi più bassi e i 5 più alti emergono chiare specificità geografiche e potenziali anomalie dovute a particolari regimi fiscali o ad errori di inserimento dati sul portale del MIMIT (Ministero delle Imprese e del Made in Italy).

### ❌ Analisi dei Dati Particolari / Non Credibili (Outlier/Anomalie)
- **Prezzi eccezionalmente bassi (~1.20 €/L):** 
  - *Causa:* Nel caso specifico di **Livigno**, i prezzi così bassi sono reali e dovuti allo status di **zona franca** (esenzione da IVA e accise sui carburanti). Altri sconti forti (es. 1.24 €/L) possono derivare da promozioni aggressive o errori di digitazione.
- **Prezzi elevati (~2.70 - 2.80 €/L):**
  - *Causa:* Rilevati su **isole minori** (es. Capraia, Lampedusa), dove i costi di trasporto marittimo pesano notevolmente, oppure in tratte **autostradali** ad alto margine. Il valore massimo assoluto di 2.869 €/L a Milano, trattandosi di self-service urbano, è verosimilmente un **errore di inserimento** del gestore (scambio tra prezzo servito e self).

### ✅ Quali prezzi sono credibili?
I prezzi sono da ritenersi **credibili** quando rientrano nella forchetta reale di mercato italiano (indicativamente tra **1.60 €/L e 2.20 €/L** per la benzina self-service ordinaria).

---

## 4. Conclusione e Strategia di Pulizia Dati
Per ottenere un calcolo corretto della **media nazionale** e delle analisi successive (come la **Domanda 3**):
1. **Filtering/Trimming:** È opportuno valutare la rimozione o la gestione degli outlier estremi (es. valori palesemente errati dovuti a refusi di battitura) per evitare distorsioni statistiche.
2. **Impatto della pulizia:** Tenere conto dei regimi fiscali particolari (come Livigno) è essenziale per non falsare le valutazioni territoriali su base provinciale.
