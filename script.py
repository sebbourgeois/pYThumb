import os
import json
import requests
import argparse
from pytube import YouTube, Channel

# Function to download thumbnail from YouTube URL
def download_thumbnail(video_url, folder=""):
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
            image_path = os.path.join(folder, image_name) if folder else image_name
            with open(image_path, 'wb') as file:
                file.write(response.content)
            return {"url": video_url, "title": title, "image_name": image_name}
        else:
            print(f"Error: Could not download thumbnail for {video_url}")
            return None
    except Exception as e:
        print(f"Error processing {video_url}: {str(e)}")
        return None

# Function to read URLs from txt file and process thumbnails
def process_videos_from_file(file_path, output_json, folder=""):
    processed_videos = []
    
    with open(file_path, 'r') as file:
        urls = file.readlines()
    
    for url in urls:
        url = url.strip()  # Remove any trailing spaces or newlines
        if url:
            data = download_thumbnail(url, folder)
            if data:
                processed_videos.append(data)
    
    # Save to a JSON file
    with open(output_json, 'w') as json_file:
        json.dump(processed_videos, json_file, indent=4)
    
    print(f"Processed {len(processed_videos)} videos. Data saved to {output_json}")

# Function to download all thumbnails from a YouTube channel
def download_thumbnails_from_channel(channel_name, output_json):
    channel_url = f"https://www.youtube.com/c/{channel_name}"
    try:
        channel = Channel(channel_url)
        folder = channel_name
        os.makedirs(folder, exist_ok=True)

        processed_videos = []

        for video_url in channel.video_urls:
            data = download_thumbnail(video_url, folder)
            if data:
                processed_videos.append(data)

        # Save to a JSON file in the channel folder
        output_json_path = os.path.join(folder, output_json)
        with open(output_json_path, 'w') as json_file:
            json.dump(processed_videos, json_file, indent=4)

        print(f"Processed {len(processed_videos)} videos from the channel '{channel_name}'. Data saved to {output_json_path}")
    except Exception as e:
        print(f"Error processing channel '{channel_name}': {str(e)}")

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="YouTube Thumbnail Downloader")
    parser.add_argument("-f", "--file", help="Path to the text file containing YouTube URLs", default="youtube_urls.txt")
    parser.add_argument("-o", "--output", help="Name of the output JSON file", default="processed_videos.json")
    parser.add_argument("-c", "--channel", help="Download all thumbnails from a specific YouTube channel")
    
    args = parser.parse_args()

    if args.channel:
        # Download thumbnails from the specified channel
        download_thumbnails_from_channel(args.channel, args.output)
    else:
        # Process videos from the text file by default
        process_videos_from_file(args.file, args.output)

if __name__ == "__main__":
    main()
