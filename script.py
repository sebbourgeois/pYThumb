import os
import json
import requests
from pytube import YouTube

# Function to download thumbnail from YouTube URL
def download_thumbnail(video_url):
    try:
        yt = YouTube(video_url)
        video_id = yt.video_id
        title = yt.title
        # Try to get the HD thumbnail
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        response = requests.get(thumbnail_url)

        # If HD thumbnail not available, fall back to SD
        if response.status_code != 200:
            thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
            response = requests.get(thumbnail_url)

        if response.status_code == 200:
            image_name = f"{video_id}.jpg"
            with open(image_name, 'wb') as file:
                file.write(response.content)
            return {"url": video_url, "title": title, "image_name": image_name}
        else:
            print(f"Error: Could not download thumbnail for {video_url}")
            return None
    except Exception as e:
        print(f"Error processing {video_url}: {str(e)}")
        return None

# Function to read URLs from txt file and process thumbnails
def process_videos(file_path, output_json):
    processed_videos = []
    
    with open(file_path, 'r') as file:
        urls = file.readlines()
    
    for url in urls:
        url = url.strip()  # Remove any trailing spaces or newlines
        if url:
            data = download_thumbnail(url)
            if data:
                processed_videos.append(data)
    
    # Save to a JSON file
    with open(output_json, 'w') as json_file:
        json.dump(processed_videos, json_file, indent=4)
    
    print(f"Processed {len(processed_videos)} videos. Data saved to {output_json}")

# Example usage:
input_file = "youtube_urls.txt"  # File containing YouTube URLs (one per line)
output_json = "processed_videos.json"  # Output JSON file
process_videos(input_file, output_json)
