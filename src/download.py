import yt_dlp


def download_video(url, output_path):
    '''Scarica il video in formato MP4 unendo audio e video (Richiede FFmpeg).'''
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'quiet': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_audio(url, output_path):
    '''Scarica l\'audio e lo converte in MP3 (Richiede FFmpeg).'''
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'bestaudio/best',
        'quiet': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def verifica_e_analizza(url):
    '''Verifica l\'URL e filtra formati Solo Audio o Video >= 720p.'''
    ydl_opts = {
        'quiet': True, 
        'no_warnings': True,
        'noplaylist': True
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            formati = []
            visti = set()

            for f in info.get('formats', []):
                res_val = f.get('height')
                ext = f.get('ext')
                acodec = f.get('acodec')
                vcodec = f.get('vcodec')

                is_audio = vcodec == 'none' and acodec != 'none'
                is_video_hd = res_val is not None and isinstance(res_val, int) and res_val >= 720

                if (is_audio or is_video_hd) and ext != 'mhtml':
                    etichetta_res = f'{res_val}p' if not is_audio else 'Solo Audio'
                    
                    identificatore = f'{etichetta_res}_{ext}'
                    
                    if identificatore not in visti:
                        formati.append({
                            'id': f['format_id'],
                            'ext': ext,
                            'res': etichetta_res,
                            'res_num': res_val if res_val else 0,
                            'note': f.get('format_note', 'N/D')
                        })
                        visti.add(identificatore)
            
            formati.sort(key=lambda x: (1 if x['res'] != 'Solo Audio' else 0, x['res_num']))
            
            return {'status': 'ok', 'title': info.get('title'), 'formats': formati}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}