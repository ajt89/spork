import json
from pathlib import Path
from unittest import TestCase, mock

from tests.spork_constants import YOUTUBE_ID, YOUTUBE_TITLE, YOUTUBE_URL
from youtube.models.video import YoutubeVideo


class TestYoutubeQuery(TestCase):
    @classmethod
    def setUpClass(cls):
        youtube_fixtures_folder = Path("tests/fixtures/youtube/")

        with open(youtube_fixtures_folder / "single_video.json") as json_file:
            youtube_single_video_response = json.load(json_file)

        item = youtube_single_video_response.get("items")[0]
        cls.youtube_video = YoutubeVideo(item)

    def test_init(self):
        self.assertEqual(YOUTUBE_TITLE, self.youtube_video.name)
        self.assertEqual(YOUTUBE_ID, self.youtube_video.id)
        self.assertEqual(YOUTUBE_URL, self.youtube_video.url)

    @mock.patch("youtube.models.video.requests.get")
    def test_validate_url_valid(self, mock_get):
        mock_get.return_value.text = "ok"

        self.assertTrue(self.youtube_video.validate_url())

    @mock.patch("youtube.models.video.requests.get")
    def test_validate_url_invalid(self, mock_get):
        mock_get.return_value.text = "This video isn't available anymore"

        self.assertFalse(self.youtube_video.validate_url())
