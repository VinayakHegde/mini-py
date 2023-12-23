from pytube import YouTube
import ssl

def download_video(video_url, output_path='.'):
  # Disable SSL verification
  ssl._create_default_https_context = ssl._create_unverified_context

  try:
    # Create a YouTube object
    yt = YouTube(video_url)

    # Get the highest resolution stream
    video_stream = yt.streams.get_highest_resolution()

    # Download the video
    print(f"Downloading: {yt.title}")
    video_stream.download(output_path)
    print("Download complete!")

  except Exception as e:
    print(f"An error occurred: {e}")