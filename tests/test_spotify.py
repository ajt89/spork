import json
from pathlib import Path
from unittest import TestCase, mock

from spotify.query import SpotifyQuery, SpotifyTrack, SpotifyTracks

from tests.spork_constants import (
    SPORK_ALBUM_ID,
    SPORK_ALBUM_LENGTH,
    SPORK_PLAYLIST_ID,
    SPORK_PLAYLIST_LENGTH,
    SPORK_TRACK_ARTISTS,
    SPORK_TRACK_ID,
    SPORK_TRACK_LENGTH,
    SPORK_TRACK_NAME,
)


class TestSpotifyQuery(TestCase):
    @classmethod
    @mock.patch("spotify.query.Spotify")
    def setUpClass(cls, mock_spotify):
        cls.spotify_query = SpotifyQuery()
        cls.spotify_playlist_tracks_response = {}
        cls.spotify_album_tracks_response = {}
        cls.spotify_track_response = {}

        spotify_fixtures_folder = Path("tests/fixtures/spotify/")

        with open(spotify_fixtures_folder / "playlist.json") as json_file:
            cls.spotify_playlist_tracks_response = json.load(json_file)

        with open(spotify_fixtures_folder / "album.json") as json_file:
            cls.spotify_album_tracks_response = json.load(json_file)

        with open(spotify_fixtures_folder / "track.json") as json_file:
            cls.spotify_track_response = json.load(json_file)

    def test_query_spotify_playlist(self):
        self.spotify_query.sp.playlist_tracks.return_value = self.spotify_playlist_tracks_response

        spotify_tracks = self.spotify_query.get_playlist_tracks(SPORK_PLAYLIST_ID)
        spotify_track = spotify_tracks[0]

        self.assertTrue(spotify_tracks)
        self.assertEqual(SPORK_PLAYLIST_LENGTH, len(spotify_tracks))
        self.assertEqual(SPORK_TRACK_ARTISTS, spotify_track.artists)
        self.assertEqual(SPORK_TRACK_NAME, spotify_track.name)
        self.assertEqual(SPORK_TRACK_LENGTH, spotify_track.length)
        self.assertEqual(SPORK_TRACK_ID, spotify_track.id)

    def test_query_spotify_album(self):
        self.spotify_query.sp.album_tracks.return_value = self.spotify_album_tracks_response

        spotify_tracks = self.spotify_query.get_album_tracks(SPORK_ALBUM_ID)
        spotify_track = spotify_tracks[0]

        self.assertTrue(spotify_tracks)
        self.assertEqual(SPORK_ALBUM_LENGTH, len(spotify_tracks))
        self.assertEqual(SPORK_TRACK_ARTISTS, spotify_track.artists)
        self.assertEqual(SPORK_TRACK_NAME, spotify_track.name)
        self.assertEqual(SPORK_TRACK_LENGTH, spotify_track.length)
        self.assertEqual(SPORK_TRACK_ID, spotify_track.id)

    def test_query_spotify_track(self):
        self.spotify_query.sp.track.return_value = self.spotify_track_response

        spotify_track = self.spotify_query.get_track(SPORK_TRACK_ID)

        self.assertTrue(spotify_track)
        self.assertEqual(SPORK_TRACK_ARTISTS, spotify_track.artists)
        self.assertEqual(SPORK_TRACK_NAME, spotify_track.name)
        self.assertEqual(SPORK_TRACK_LENGTH, spotify_track.length)
        self.assertEqual(SPORK_TRACK_ID, spotify_track.id)
