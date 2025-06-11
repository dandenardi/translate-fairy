import os
import srt
from datetime import timedelta
import zipfile

def save_srt(data: list, path: str):
    subtitles = []
    for item in data:
        subtitle = srt.Subtitle(
            index=item["index"],
            start=timedelta(seconds=item["start"]),
            end=timedelta(seconds=item["end"]),
            content=item["text"]
        )
        subtitles.append(subtitle)
    
    srt_content = srt.compose(subtitles)
    with open(path, "w", encoding="utf-8") as f:
        f.write(srt_content)

def zip_files(file_paths: list, output_zip: str):
    with zipfile.ZipFile(output_zip, "w") as zipf:
        for file_path in file_paths:
            zipf.write(file_path, arcname=os.path.basename(file_path))
