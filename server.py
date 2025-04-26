from flask import Flask, request, jsonify
from _transcripts import TranscriptListFetcher

app = Flask(__name__)

@app.route('/transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('videoId')
    if not video_id:
        return jsonify({'error': 'Missing video ID'}), 400

    try:
        fetcher = TranscriptListFetcher(video_id)
        transcript_list = fetcher.get_transcript()
        full_text = "\n".join([entry['text'] for entry in transcript_list])
        return jsonify({'video_id': video_id, 'transcript': full_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)