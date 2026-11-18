from main import count_songs


def test_count_songs():
    songs = [
        {"track_name": "Song A"},
        {"track_name": "Song B"},
        {"track_name": "Song C"},
    ]

    assert count_songs(songs) == 3


def test_empty_songs():
    assert count_songs([]) == 0


def test_single_song():
    songs = [{"track_name": "Song A"}]

    assert count_songs(songs) == 1