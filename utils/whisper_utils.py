import subprocess
import os
import srt
from datetime import timedelta

def transcribe(video_path: str, output_dir: str) -> list:
    srt_path = os.path.join(output_dir, "video.srt")

    command = [
        "whisper",
        video_path,
        "--model", "small",
        "--language", "en",
        "--output_format", "srt",
        "--output_dir", output_dir
    ]

    subprocess.run(command, check=True)

    # Lê o arquivo SRT gerado
    with open(srt_path, "r", encoding="utf-8") as f:
        srt_text = f.read()

    subtitles = list(srt.parse(srt_text))
    
    srt_data = []
    for sub in subtitles:
        srt_data.append({
            "index": sub.index,
            "start": sub.start.total_seconds(),
            "end": sub.end.total_seconds(),
            "text": sub.content
        })
    
    return srt_data
