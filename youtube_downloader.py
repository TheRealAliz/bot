import yt_dlp
import sys
import glob

def download_video_simple(url):
    """Download video to current directory"""
    
    ydl_opts = {
        'format': 'best[height<=720]',
        'outtmpl': '%(title)s.%(ext)s',  # Save in current directory
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
            
            # Find downloaded files
            video_files = glob.glob('*.mp4') + glob.glob('*.webm') + glob.glob('*.mkv')
            if video_files:
                print(f"✅ Downloaded: {video_files[0]}")
                return True
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        download_video_simple(sys.argv[1])
