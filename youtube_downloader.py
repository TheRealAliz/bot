import yt_dlp
import sys
import os
import glob

def download_video(url):
    print(f"Attempting to download: {url}")
    
    # Download to current directory
    ydl_opts = {
        'format': 'best[height<=480]',  # Lower quality is more reliable
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': False,
        'ignoreerrors': True,  # Don't crash on age-restricted videos
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # First, extract info to see if we can access the video
            info = ydl.extract_info(url, download=False)
            if info is None:
                print("❌ Cannot access video info. Video might be private or age-restricted.")
                return False
                
            print(f"✅ Found video: {info.get('title', 'Unknown')}")
            
            # Now download
            ydl.download([url])
            
            # Check for downloaded files
            files = glob.glob('*.mp4') + glob.glob('*.webm') + glob.glob('*.mkv')
            if files:
                print(f"✅ Success! Downloaded: {files[0]}")
                return True
            else:
                print("❌ Download completed but no video file found.")
                return False
                
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python youtube_downloader.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1]
    success = download_video(url)
    sys.exit(0 if success else 1)
