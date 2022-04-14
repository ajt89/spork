from typing import List

import requests


class YoutubeVideo:
    def __init__(self, video_data) -> None:
        self.name = video_data.get("snippet").get("title")
        self.id = video_data.get("id").get("videoId")
        self.url = f"https://www.youtube.com/watch?v={self.id}"

    def validate_url(self) -> bool:
        response = requests.get(self.url)
        return bool("This video isn't available anymore" not in response.text)


YoutubeVideos = List[YoutubeVideo]
