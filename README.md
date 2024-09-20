# pYThumb

This script reads a text file containing YouTube video URLs, downloads the thumbnail for each video (in HD if available, otherwise in SD), and saves it as `VIDEO_ID.jpg`. Along with downloading thumbnails, it also generates a JSON file with details of the processed videos, including:
- The original URL
- The video title
- The name of the downloaded image

## Features
- Downloads YouTube video thumbnails in HD or SD.
- Saves thumbnails with the YouTube video ID as the filename.
- Generates a JSON file with information about the processed videos.

## Requirements

The following Python packages are required:
- `pytube`: To fetch video details (e.g., video title, video ID).
- `requests`: To download the thumbnail image.

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

## How to Use

1. Create a text file (e.g., `youtube_urls.txt`) with one YouTube URL per line:
   ```
   https://www.youtube.com/watch?v=dQw4w9WgXcQ
   https://www.youtube.com/watch?v=XqZsoesa55w
   ```

2. Run the script:
   ```bash
   python script.py
   ```

   The script will:
   - Download the thumbnails for each YouTube URL.
   - Save the images in the current directory as `VIDEO_ID.jpg` (e.g., `S0MZ6cXmYKo.jpg`).
   - Generate a `processed_videos.json` file containing details about the downloaded videos.

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
