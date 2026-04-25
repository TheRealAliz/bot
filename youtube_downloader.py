import yt_dlp
import os
import sys

def download_video(url):
    """Download YouTube video"""
    
    # Create downloads directory in current working directory
    output_dir = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"📁 Saving to: {output_dir}")
    
    ydl_opts = {
        'format': 'best[height<=720]',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"🎬 Downloading: {url}")
            info = ydl.extract_info(url, download=True)
            
            # Get the actual filename that was saved
            filename = ydl.prepare_filename(info)
            
            # Check if file exists
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                print(f"✅ Downloaded: {filename}")
                print(f"📊 File size: {file_size} bytes")
                return True
            else:
                print(f"❌ File not found: {filename}")
                return False
                
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        success = download_video(url)
        sys.exit(0 if success else 1)
    else:
        print("Usage: python youtube_downloader.py <youtube_url>")
        sys.exit(1)
