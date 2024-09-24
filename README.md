
# pYThumb

This script reads a text file containing YouTube video URLs, downloads the thumbnail for each video (in HD if available, otherwise in SD), and saves it as `VIDEO_ID.jpg`. Along with downloading thumbnails, it also generates a JSON file with details of the processed videos, including:
- The original URL
- The video title
- The name of the downloaded image

Additionally, the script can download all video thumbnails from a specific YouTube channel by using the YouTube Data API v3.

## Features
- Downloads YouTube video thumbnails in HD or SD.
- Saves thumbnails with the YouTube video ID as the filename.
- Generates a JSON file with information about the processed videos.
- Downloads all video thumbnails from a YouTube channel using the YouTube Data API v3.

## Requirements

The following Python packages are required:
- `pytube`: To fetch video details (e.g., video title, video ID).
- `requests`: To download the thumbnail image.

You'll also need an API key from YouTube Data API v3 to fetch video URLs from a channel.

### Steps to Obtain YouTube Data API Key:
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (if you don't have one).
3. Navigate to the [API library](https://console.cloud.google.com/apis/library) and search for "YouTube Data API v3".
4. Enable the API.
5. Go to the [Credentials section](https://console.cloud.google.com/apis/credentials) and create an API key.
6. Copy the API key for later use.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sebbourgeois/pYThumb.git
   cd pYThumb
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your YouTube Data API key in the script:
   Replace `YOUR_YOUTUBE_DATA_API_KEY` in `script.py` with the API key obtained from the Google Cloud Console.

## How to Use

1. **Downloading thumbnails from a file (default behavior)**:
   - Create a text file (e.g., `youtube_urls.txt`) with one YouTube URL per line:
     ```
     https://www.youtube.com/watch?v=S0MZ6cXmYKo
     https://www.youtube.com/watch?v=dQw4w9WgXcQ
     ```

   - Run the script:
     ```bash
     python script.py
     ```

   - The script will:
     - Download the thumbnails for each YouTube URL.
     - Save the images in the current directory as `VIDEO_ID.jpg` (e.g., `S0MZ6cXmYKo.jpg`).
     - Generate a `processed_videos.json` file containing details about the downloaded videos.

2. **Downloading all thumbnails from a YouTube channel**:
   - Run the script with the `-c` or `--channel` flag:
     ```bash
     python script.py -c Amixem
     ```

   - This will download all thumbnails from the specified channel (`Amixem`) and store them in a folder named after the channel. The script will also generate a JSON file (`processed_videos.json`) in the same folder with details about the downloaded videos.

3. **Specify a custom file and output**:
   - To specify a custom file with URLs or a custom output JSON file:
     ```bash
     python script.py -f custom_urls.txt -o custom_output.json
     ```

## Example Output

### `processed_videos.json`
```json
[
    {
        "url": "https://www.youtube.com/watch?v=S0MZ6cXmYKo",
        "title": "Sample Video Title",
        "image_name": "S0MZ6cXmYKo.jpg"
    },
    {
        "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "title": "Rick Astley - Never Gonna Give You Up",
        "image_name": "dQw4w9WgXcQ.jpg"
    }
]
```

### Thumbnail Image
The thumbnail for each video is saved as `VIDEO_ID.jpg`, where `VIDEO_ID` is the unique identifier from the YouTube video URL.

For example, for the URL `https://www.youtube.com/watch?v=S0MZ6cXmYKo`, the thumbnail image will be saved as `S0MZ6cXmYKo.jpg`.

## Contributions

Feel free to open issues or submit pull requests if you have any improvements or features to add.

---

Happy coding!
