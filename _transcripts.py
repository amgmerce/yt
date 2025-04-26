from youtube_transcript_api import YouTubeTranscriptApi

def fetch_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = "\n".join([entry['text'] for entry in transcript_list])
        return full_text
    except Exception as e:
        raise Exception(f"Error fetching transcript: {str(e)}")
