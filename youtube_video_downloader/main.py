from video import download_video

if __name__ == "__main__":
  # Replace 'YOUR_YOUTUBE_VIDEO_URL' with the actual YouTube video URL
  video_url = input("Enter the YouTube video URL: ")

  # Replace 'YOUR_OUTPUT_PATH' with the desired output path
  output_path = input("Enter the output path (default is current directory): ") or '.'

  download_video(video_url, output_path)
