import yt_dlp
import os
import sys

def download_video(url, output_path='downloads'):
    """Download YouTube video using yt-dlp"""
    
    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    # Options for yt-dlp
    ydl_opts = {
        'format': 'best[height<=720]',  # Max 720p quality
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            print(f"✅ Downloaded: {filename}")
            return filename
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        download_video(url)
    else:
        print("Usage: python youtube_downloader.py <youtube_url>")
