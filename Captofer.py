import src.gestore_tui as gt

if __name__ == "__main__":
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
    gt.get_url()