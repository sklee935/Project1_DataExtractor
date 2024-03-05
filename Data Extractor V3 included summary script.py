import yt_dlp
import json
import os
from transformers import pipeline

def download_video_metadata_transcript(video_url, output_path):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'writeinfojson': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        video_title = info_dict.get('title', None)

    subtitle_file_path = os.path.join(output_path, f"{video_title}.en.vtt")
    
    try:
        summarizer = pipeline("summarization")
        if os.path.exists(subtitle_file_path):
            with open(subtitle_file_path, 'r', encoding='utf-8') as file:
                transcript = file.read()
            summarized_text = summarizer(transcript, max_length=130, min_length=30, do_sample=False)
            summary = summarized_text[0]['summary_text']
            print(f"Transcript summary for '{video_title}':\n{summary}")
        else:
            print("No transcript file found.")
    except Exception as e:
        print(f"An error occurred while summarizing the transcript: {e}")

        
## Example usage
video_url = 'https://youtu.be/KfAHEp-56RQ?si=Go9UCnLuoKFoIbR8'  # Replace with the actual video URL
output_path = 'C:\\Users\\slee\\OneDrive - SBP\\Desktop\\sungkeun\\Vosyn\\Download Youtube'  # Specify your desired output directory
download_video_metadata_transcript(video_url, output_path)
