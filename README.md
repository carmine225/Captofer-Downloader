# 🎥 Captofer
**Ex Flumine ad Arcam** - *Un downloader YouTube elegante, potente e pronto all'uso con Docker.*

---

## 📝 Cos'è Captofer?
Captofer è una **TUI (Terminal User Interface)** progettata per scaricare video (fino a 4K) e audio (MP3) da YouTube senza complicazioni. Gestisce automaticamente la pulizia dei nomi dei file e organizza tutto nella cartella dedicata `downloads/`.

---

## 🚀 Avvio Rapido con Docker (Metodo Consigliato)
Docker è la scelta migliore perché include già **FFmpeg** e tutte le dipendenze necessarie in un ambiente isolato.

1. **Build dell'immagine:**
   docker build -t captofer .

2. **Esegui il programma:**
   *(I file scaricati appariranno nella cartella 'downloads/' del tuo progetto)*
   
   - **PowerShell:** docker run -it --rm -v "${PWD}:/app" captofer
   
   - **Prompt dei comandi (CMD):** docker run -it --rm -v "%cd%:/app" captofer
   
   - **Linux/macOS:** docker run -it --rm -v "$(pwd):/app" captofer

---

## 🛠️ Installazione Manuale
Se preferisci non usare Docker, assicurati di avere **FFmpeg** installato e configurato nel PATH del tuo sistema.

### 1. Requisiti
* **Python 3.7+**
* **FFmpeg** (Necessario per il merging di audio e video HD)

### 2. Setup
# Installa le dipendenze
pip install -r requirements.txt

# Avvia l'applicazione
python Captofer.py

---

## ✨ Caratteristiche Principali
* 🎬 **Qualità Adattiva:** Scegli tra diverse risoluzioni (720p, 1080p, 4K).
* 🎵 **Audio Crystal Clear:** Estrazione diretta in MP3 a 192kbps.
* 📂 **Smart Storage:** Creazione automatica della cartella 'downloads/'.
* 🛡️ **File Safety:** Pulizia automatica dei caratteri proibiti (\ / : * ? " < > |).
* 🎨 **Interfaccia ANSI:** Banner e output colorati per una migliore usabilità.

---

## 📂 Struttura del Progetto
Captofer/
├── src/
│   ├── download.py        # Logica di scaricamento (yt-dlp)
│   └── gestore_tui.py     # Interfaccia terminale e gestione percorsi
├── downloads/             # Destinazione automatica dei download (esclusa da Git)
├── Captofer.py            # Entry point dell'applicazione
├── Dockerfile             # Configurazione ambiente Docker
├── .gitignore             # File per escludere file temporanei e download
└── requirements.txt       # Librerie Python necessarie

---

## 📜 Licenza
Questo progetto è rilasciato sotto **Licenza MIT**. Consultare il file LICENSE per i dettagli.

---
**⚖️ Disclaimer**: *Questo tool è creato a scopo educativo. Si prega di rispettare i termini di servizio di YouTube e i diritti d'autore dei contenuti.*