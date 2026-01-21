import os
import re
import subprocess
from . import download as dl


class Colori:
    '''Codici ANSI per colori nel terminale'''
    RESET = '\033[0m'
    ROSSO = '\033[91m'
    VERDE = '\033[92m'
    GIALLO = '\033[93m'
    BLU = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    BIANCO = '\033[97m'


def controlla_ffmpeg():
    '''Controlla se FFmpeg è installato nel sistema.'''
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False


def pulisci_nome(nome):
    '''Rimuove caratteri non validi per i file Windows: \ / : * ? " < > |'''
    return re.sub(r'[\\/*?:"<>|]', '', nome)


def clear_console():
    '''Pulisce la console. Windows: cls, Linux/macOS: clear'''
    os.system('cls' if os.name == 'nt' else 'clear')


def get_url():
    '''Acquisisce URL e gestisce il download del video/audio.'''
    url = input('Inserisci l\'URL del video/audio da scaricare: ')
    
    # Controlla FFmpeg all'inizio
    if not controlla_ffmpeg():
        print(f'{Colori.ROSSO}❌ ERRORE: FFmpeg non è installato!{Colori.RESET}')
        print(f'''{Colori.GIALLO}Scaricalo da: https://ffmpeg.org/download.html
oppure usa il bash: winget install ffmpeg{Colori.RESET}''')
        return
    
    result = dl.verifica_e_analizza(url)
    
    if result['status'] == 'ok':
        titolo_pulito = pulisci_nome(result['title'])
        
        print(f'\n{Colori.VERDE}✅ Titolo: {titolo_pulito}{Colori.RESET}')
        print(f'{Colori.BLU}{"─" * 60}{Colori.RESET}')
        
        for i, f in enumerate(result['formats']):
            print(f'{Colori.CIANO}[{i}]{Colori.RESET} Risoluzione: {Colori.BIANCO}{f["res"]}{Colori.RESET} | Estensione: {Colori.MAGENTA}{f["ext"]}{Colori.RESET} ({f["note"]})')
        
        print(f'{Colori.BLU}{"─" * 60}{Colori.RESET}')
        scelta = input(f'{Colori.GIALLO}Seleziona il formato da scaricare (numero): {Colori.RESET}')
        
        try:
            index = int(scelta)
            f_scelto = result['formats'][index]
            
            is_audio = f_scelto['res'] == 'Solo Audio'
            ext_finale = 'mp3' if is_audio else 'mp4'
            output_path = f'{titolo_pulito}.{ext_finale}'
            
            print(f'\n{Colori.GIALLO}⬇️  Scaricamento in corso: {Colori.BIANCO}{output_path}{Colori.GIALLO} ...{Colori.RESET}')
            
            if is_audio:
                dl.download_audio(url, output_path)
            else:
                dl.download_video(url, output_path)
                
            print(f'\n{Colori.VERDE}✅ Task complete. Asset secured.{Colori.RESET}')
        except (ValueError, IndexError):
            print(f'{Colori.ROSSO}❌ Scelta non valida.{Colori.RESET}')
    else:
        print(f'{Colori.ROSSO}❌ Errore: {result["message"]}{Colori.RESET}')