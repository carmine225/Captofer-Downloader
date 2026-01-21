# 🎥 Captofer

**Ex Flumine ad Arcam** - Un downloader minimalista per video e audio da YouTube.

> ⚡ Veloce • 🎨 Elegante • 🎯 Semplice • 🖥️ **Cross-Platform** (Windows • Linux • macOS)

## 📝 Descrizione

Captofer è uno strumento da terminale che consente di scaricare video e audio da YouTube con un'interfaccia intuitiva e colorata. Permette di selezionare tra diverse qualità:
- 🎬 Video: 720p, 1080p, 4K e superiore
- 🎵 Audio: MP3 ad alta qualità

## ⚠️ ATTENZIONE - FFmpeg Obbligatorio

> **FFmpeg DEVE essere installato separatamente nel tuo sistema prima di utilizzare Captofer!**
> 
> Questo programma non installa automaticamente FFmpeg. È responsabilità dell'utente scaricarlo e configurarlo.

### 📥 Installazione di FFmpeg

**🪟 Windows:**
1. Scarica da: https://ffmpeg.org/download.html
2. Aggiungi FFmpeg al PATH di sistema ([Guida](https://www.architectryan.com/add-to-the-path-on-windows-10/))
3. Verifica con `ffmpeg -version` nel terminale

**🐧 Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**🍎 macOS:**
```bash
brew install ffmpeg
```

## 📦 Requisiti

- **Python 3.7+**
- **FFmpeg** ⚠️ (OBBLIGATORIO - vedi sezione sopra)
- **Dipendenze Python**: `yt-dlp`

## 🚀 Installazione Veloce

```bash
# 1. Installa le dipendenze Python
pip install -r requirements.txt

# 2. Verifica FFmpeg (FONDAMENTALE!)
ffmpeg -version

# 3. Esegui il programma
python Captofer.py
```

## 💻 Utilizzo

```bash
python Captofer.py
```

**Segui questi passaggi:**
1. Incolla l'URL del video YouTube
2. Seleziona il formato desiderato (audio MP3 o video MP4)
3. Attendi il completamento del download

## ✨ Features

| Feature | Descrizione |
|---------|------------|
| 🎬 **Download Video** | Scarica video in MP4 (720p, 1080p, 4K+) |
| 🎵 **Download Audio** | Estrai audio in MP3 (192kbps) |
| 🎨 **Interfaccia Colorata** | Output facile da leggere nel terminale |
| ✅ **Controllo FFmpeg** | Verifica automatica della presenza di FFmpeg |
| 🏷️ **Pulizia Nomi** | Rimuove caratteri invalidi dai nomi file |
| 📊 **Formato Intelligente** | Ordina i formati per facilità d'uso |

## 📂 Struttura Progetto

```
Captofer/
├── Captofer.py           # 🎯 Entry point principale
├── requirements.txt      # 📦 Dipendenze Python
├── README.md             # 📖 Documentazione
└── src/
    ├── __init__.py       # Package marker
    ├── gestore_tui.py    # 🖥️ Gestione interfaccia terminale
    └── download.py       # ⬇️ Logica di download con yt-dlp
```

## ⚙️ Configurazione Avanzata

### 🎬 Cambiare Qualità Minima dei Video

Modifica in `src/download.py`, nella funzione `verifica_e_analizza()`:
```python
is_video_hd = res_val is not None and isinstance(res_val, int) and res_val >= 720
```

Cambia `720` con la risoluzione desiderata (es: `1080` per 1080p+, `2160` per 4K+).

### 🎵 Cambiare Qualità MP3

Modifica in `src/download.py`, nella funzione `download_audio()`:
```python
'preferredquality': '192',  # Opzioni: 128, 192, 256, 320
```

## 🆘 Risoluzione Problemi

| Errore | Soluzione |
|--------|----------|
| **"FFmpeg non è installato"** | Scarica FFmpeg da https://ffmpeg.org/download.html e aggiungilo al PATH |
| **"ModuleNotFoundError: yt_dlp"** | Esegui: `pip install -r requirements.txt` |
| **Il video non scarica** | Verifica che l'URL sia valido, pubblico e che la connessione funzioni |
| **Nomi file corrotti** | Il programma pulisce automaticamente i caratteri, ma alcuni potrebbero non essere supportati |

## 📜 Licenza

Uso personale - Non per scopi commerciali o pirateria di contenuti protetti.

---

**⚖️ Nota Importante**: Rispetta i diritti d'autore e i termini di servizio di YouTube.

**🔗 Link Utili:**
- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg Official](https://ffmpeg.org/)
- [YouTube Terms of Service](https://www.youtube.com/static?template=terms)
