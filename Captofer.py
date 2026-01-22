import src.gestore_tui as gt


def baner():
    banner=r'''
   ______            __        ____              
  / ____/___  ____  / / ____  / __/__  _____ 
 / /   / __ `/ __ \/ __/ __ \/ /_/ _ \/ ___/ 
/ /___/ /_/ / /_/ / /_/ /_/ / __/  __/ /     
\____/\__,_/ .___/\__/\____/_/  \___/_/      
          /_/                                

        --Ex Flumine ad Arcam--
'''
    gt.clear_console()
    print(banner)
    
def main():
    '''Funzione principale per l'interfaccia TUI.'''
    while True:
        print(f'{gt.Colori.MAGENTA}=== Gestore di Download Video/Audio ==={gt.Colori.RESET}\n')
        print('1. Scarica Video/Audio')
        print('2. Esci\n')
        
        scelta = input(f'{gt.Colori.GIALLO}Seleziona un\'opzione (1-2): {gt.Colori.RESET}')
        
        if scelta == '1':
            gt.get_url() 
            baner()  
        elif scelta == '2':
            print(f'{gt.Colori.CIANO}Uscita in corso...{gt.Colori.RESET}')
            break
        else:
            print(f'{gt.Colori.ROSSO}❌ Scelta non valida. Riprova.{gt.Colori.RESET}')
            input(f'\n{gt.Colori.GIALLO}Premi Invio per continuare...{gt.Colori.RESET}')
if __name__ == "__main__":
    baner()
    main()
