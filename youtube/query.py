import os

from googleapiclient.discovery import build

from youtube.models.video import YoutubeVideo, YoutubeVideos

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


class YoutubeQuery:
    def __init__(self):
        self.yt = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    def get_videos(self, query: str, max_results: int) -> YoutubeVideos:
        request = self.yt.search().list(
            part="id,snippet",
            type="video",
            q=query,
            maxResults=max_results,
        )
        response = request.execute()
        return [YoutubeVideo(item) for item in response.get("items")]
