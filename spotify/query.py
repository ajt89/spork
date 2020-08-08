from typing import List

from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

from spotify.models.track import SpotifyTrack

SpotifyTracks = List[SpotifyTrack]


class SpotifyQuery:
    def __init__(self):
        self.sp = Spotify(auth_manager=SpotifyClientCredentials())

    def get_playlist_tracks(self, spotify_id: str) -> SpotifyTracks:
        playlist_tracks = self.sp.playlist_tracks(spotify_id)
        return [SpotifyTrack(item.get("track")) for item in playlist_tracks.get("items")]

    def get_album_tracks(self, spotify_id: str) -> SpotifyTracks:
        album_tracks = self.sp.album_tracks(spotify_id)
        return [SpotifyTrack(item) for item in album_tracks.get("items")]

    def get_track(self, spotify_id: str) -> SpotifyTrack:
        track = self.sp.track(spotify_id)
        return SpotifyTrack(track)
