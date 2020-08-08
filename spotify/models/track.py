class SpotifyTrack:
    def __init__(self, track_data):
        self.artists = [artist.get("name") for artist in track_data.get("artists")]
        self.name = track_data.get("name")
        self.length = track_data.get("duration_ms")
        self.id = track_data.get("id")

    def get_query_statement(self):
        return f"{self.name} {' '.join(artists)}"
