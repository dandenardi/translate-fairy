import os
from utils.whisper_utils import transcribe
from utils.google_translate import translate_srt
from utils.srt_utils import save_srt, zip_files
import yt_dlp

def process_video(url: str, job_id: str) -> str:
    output_dir = f"static/{job_id}"
    os.makedirs(output_dir, exist_ok=True)

    video_path = f"{output_dir}/video.mp4"

    # 1. Baixar vídeo
    ydl_opts = {
        'outtmpl': video_path,
        'format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # 2. Transcrever
    original_srt = transcribe(video_path, output_dir)

    # 3. Traduzir
    translated_srt = translate_srt(original_srt)

    # 4. Salvar arquivos
    save_srt(original_srt, f"{output_dir}/original.srt")
    save_srt(translated_srt, f"{output_dir}/translated.srt")

    # 5. Zipar
    zip_path = f"{output_dir}/output.zip"
    zip_files([video_path, f"{output_dir}/original.srt", f"{output_dir}/translated.srt"], zip_path)

    return zip_path