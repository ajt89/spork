import json
from pathlib import Path
from unittest import TestCase

from spotify.models.track import SpotifyTrack
from tests.spork_constants import (
    SPORK_TRACK_ARTISTS,
    SPORK_TRACK_ID,
    SPORK_TRACK_LENGTH,
    SPORK_TRACK_NAME,
    YOUTUBE_QUERY,
)


class TestYoutubeQuery(TestCase):
    @classmethod
    def setUpClass(cls):
        spotify_track_response = {}

        spotify_fixtures_folder = Path("tests/fixtures/spotify/")

        with open(spotify_fixtures_folder / "track.json") as json_file:
            spotify_track_response = json.load(json_file)
        cls.spotify_track = SpotifyTrack(spotify_track_response)

    def test_init(self):
        self.assertEqual(SPORK_TRACK_ARTISTS, self.spotify_track.artists)
        self.assertEqual(SPORK_TRACK_NAME, self.spotify_track.name)
        self.assertEqual(SPORK_TRACK_LENGTH, self.spotify_track.length)
        self.assertEqual(SPORK_TRACK_ID, self.spotify_track.id)

    def test_get_query_statement(self):
        query_statement = self.spotify_track.get_query_statement()

        self.assertEqual(YOUTUBE_QUERY, query_statement)
