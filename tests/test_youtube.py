import json
from pathlib import Path
from unittest import TestCase, mock

from tests.spork_constants import YOUTUBE_ID, YOUTUBE_QUERY, YOUTUBE_TITLE, YOUTUBE_VIDEOS_COUNT
from youtube.query import YoutubeQuery


class TestYoutubeQuery(TestCase):
    @classmethod
    @mock.patch("youtube.query.build")
    def setUpClass(cls, mock_youtube):
        cls.youtube_query = YoutubeQuery()
        cls.youtube_videos_response = {}

        youtube_fixtures_folder = Path("tests/fixtures/youtube/")

        with open(youtube_fixtures_folder / "single_video.json") as json_file:
            cls.youtube_single_video_response = json.load(json_file)

        with open(youtube_fixtures_folder / "multiple_videos.json") as json_file:
            cls.youtube_multiple_videos_response = json.load(json_file)

    def test_query_single_video_youtube(self):
        self.youtube_query.yt.search.return_value.list.return_value.execute.return_value = (
            self.youtube_single_video_response
        )

        youtube_videos = self.youtube_query.get_videos(YOUTUBE_QUERY, 1)
        youtube_video = youtube_videos[0]

        self.assertTrue(youtube_videos)
        self.assertEqual(YOUTUBE_ID, youtube_video.id)
        self.assertEqual(YOUTUBE_TITLE, youtube_video.name)

    def test_query_multiple_videos_youtube(self):
        self.youtube_query.yt.search.return_value.list.return_value.execute.return_value = (
            self.youtube_multiple_videos_response
        )

        youtube_videos = self.youtube_query.get_videos(YOUTUBE_QUERY, 5)
        youtube_video = youtube_videos[0]

        self.assertTrue(youtube_videos)
        self.assertEqual(YOUTUBE_VIDEOS_COUNT, len(youtube_videos))
        self.assertEqual(YOUTUBE_ID, youtube_video.id)
        self.assertEqual(YOUTUBE_TITLE, youtube_video.name)
