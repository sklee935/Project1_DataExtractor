import yt_dlp
import json
import os

def download_video_and_metadata(video_url, output_path):
    # Configuration options for yt-dlp
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Save the file with the video title
        'writeinfojson': True,  # Save metadata as a .json file
    }
    
    # Use yt-dlp to download video and extract metadata
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    
    # Search for the .info.json file in the output directory after download
    for file in os.listdir(output_path):
        if file.endswith(".info.json"):
            metadata_file_path = os.path.join(output_path, file)
            with open(metadata_file_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                # Extract and print the required metadata fields
                print(f"Title: {metadata['title']}")
                print(f"Description: {metadata['description']}")
                print(f"Duration: {metadata['duration']}")
                print(f"Uploader: {metadata['uploader']}")
                print(f"Views: {metadata['view_count']}")
                print(f"Category: {metadata['categories'][0] if 'categories' in metadata else 'N/A'}")
                print(f"Tags: {', '.join(metadata['tags']) if 'tags' in metadata else 'N/A'}")

# Example usage
video_url = 'https://youtu.be/gWdr7LcSCto?si=7Ex64kEw3Xf9ZkC6'  # Replace with the actual video URL
output_path = 'C:\\Users\\slee\\OneDrive - SBP\\Desktop\\sungkeun\\Vosyn\\Download Youtube'  # Specify your desired output directory
download_video_and_metadata(video_url, output_path)
