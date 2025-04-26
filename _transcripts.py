import requests
import re

def fetch_transcript(video_id):
    try:
        captions_url = f"https://video.google.com/timedtext?lang=en&v={video_id}"
        response = requests.get(captions_url)
        if response.status_code != 200 or not response.text:
            raise Exception("No transcript available or invalid video ID.")

        text_lines = re.findall(r'>([^<]+)<', response.text)
        if not text_lines:
            raise Exception("Transcript data not found.")

        full_text = "\n".join(text_lines)
        return full_text

    except Exception as e:
        raise Exception(f"Error fetching transcript: {str(e)}")