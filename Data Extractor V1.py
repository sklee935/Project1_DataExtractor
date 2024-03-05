import yt_dlp
import json
import os

def download_video_and_metadata(video_url, output_path):
    # yt-dlp 옵션 설정
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # 비디오 제목으로 파일 저장
        'writeinfojson': True,  # 메타데이터를 .json 파일로 저장
    }
    
    # yt-dlp를 사용하여 비디오 다운로드 및 메타데이터 추출
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    
    # 다운로드 후 출력 디렉토리에서 .info.json 파일 검색
    for file in os.listdir(output_path):
        if file.endswith(".info.json"):
            metadata_file_path = os.path.join(output_path, file)
            with open(metadata_file_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
                # 필요한 메타데이터 필드 추출 및 출력
                print(f"Title: {metadata['title']}")
                print(f"Description: {metadata['description']}")
                print(f"Duration: {metadata['duration']}")
                print(f"Uploader: {metadata['uploader']}")
                print(f"Views: {metadata['view_count']}")
                print(f"Category: {metadata['categories'][0] if 'categories' in metadata else 'N/A'}")
                print(f"Tags: {', '.join(metadata['tags']) if 'tags' in metadata else 'N/A'}")

# 사용 예시
video_url = 'https://youtu.be/gWdr7LcSCto?si=7Ex64kEw3Xf9ZkC6'  # 실제 비디오 URL로 교체
output_path = 'C:\\Users\\slee\\OneDrive - SBP\\Desktop\\sungkeun\\Vosyn\\Download Youtube'  # 원하는 출력 디렉토리 지정
download_video_and_metadata(video_url, output_path)
