from unittest import TestCase, mock

<<<<<<< HEAD
from spotify.query import SpotifyQuery, SpotifyTrack, SpotifyTracks
from tests.spork_constants import (SPORK_ALBUM_ID, SPORK_ALBUM_LENGTH,
                                   SPORK_PLAYLIST_ID, SPORK_PLAYLIST_LENGTH,
                                   SPORK_TRACK_ARTISTS, SPORK_TRACK_ID,
                                   SPORK_TRACK_LENGTH, SPORK_TRACK_NAME,
                                   SpotifyQuery, SpotifyTrack, SpotifyTracks,
                                   7531f710fef324ce56de2f920632f623d3f27f03,
                                   =======, >>>>>>>, from, import,
                                   spotify.query, tests.spork_constants)


class TestSpotifyQuery(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spotify_query = SpotifyQuery()

    def test_query_spotify_playlist(self):
        spotify_tracks = self.spotify_query.get_playlist_tracks(SPORK_PLAYLIST_ID)
        spotify_track = spotify_tracks[0]

        self.assertTrue(spotify_tracks)
        self.assertEqual(SPORK_PLAYLIST_LENGTH, len(spotify_tracks))
        self.assertEqual(SPORK_TRACK_ARTISTS, spotify_track.artists)
        self.assertEqual(SPORK_TRACK_NAME, spotify_track.name)
        self.assertEqual(SPORK_TRACK_LENGTH, spotify_track.length)
        self.assertEqual(SPORK_TRACK_ID, spotify_track.id)

    def test_query_spotify_album(self):
        spotify_tracks = self.spotify_query.get_album_tracks(SPORK_ALBUM_ID)
        spotify_track = spotify_tracks[0]

        self.assertTrue(spotify_tracks)
        self.assertEqual(SPORK_ALBUM_LENGTH, len(spotify_tracks))
        self.assertEqual(SPORK_TRACK_ARTISTS, spotify_track.artists)
        self.assertEqual(SPORK_TRACK_NAME, spotify_track.name)
        self.assertEqual(SPORK_TRACK_LENGTH, spotify_track.length)
        self.assertEqual(SPORK_TRACK_ID, spotify_track.id)

    def test_query_spotify_track(self):
        spotify_track = self.spotify_query.get_track(SPORK_TRACK_ID)

        self.assertTrue(spotify_track)
        self.assertEqual(SPORK_TRACK_ARTISTS, spotify_track.artists)
        self.assertEqual(SPORK_TRACK_NAME, spotify_track.name)
        self.assertEqual(SPORK_TRACK_LENGTH, spotify_track.length)
        self.assertEqual(SPORK_TRACK_ID, spotify_track.id)
