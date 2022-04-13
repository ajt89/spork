from typing import List


class YoutubeVideo:
    def __init__(self, video_data) -> None:
        self.name = video_data.get("snippet").get("title")
        self.id = video_data.get("id").get("videoId")

    def get_url(self) -> str:
        return f"https://www.youtube.com/watch?v={self.id}"


YoutubeVideos = List[YoutubeVideo]
