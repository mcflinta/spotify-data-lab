from main import search_by_artist


def test_search_exact_match():
    songs = [
        {"track_name": "Song A", "artist(s)_name": "Taylor Swift"},
        {"track_name": "Song B", "artist(s)_name": "The Weeknd"},
        {"track_name": "Song C", "artist(s)_name": "Taylor Swift"},
    ]

    result = search_by_artist(songs, "Taylor Swift")

    assert len(result) == 2
    assert result[0]["track_name"] == "Song A"
    assert result[1]["track_name"] == "Song C"


def test_case_insensitive():
    songs = [
        {"track_name": "Song A", "artist(s)_name": "Taylor Swift"}
    ]

    result = search_by_artist(songs, "TAYLOR SWIFT")

    assert len(result) == 1


def test_strip_whitespace():
    songs = [
        {"track_name": "Song A", "artist(s)_name": "Taylor Swift"}
    ]

    result = search_by_artist(songs, "  Taylor Swift  ")

    assert len(result) == 1


def test_artist_not_found():
    songs = [
        {"track_name": "Song A", "artist(s)_name": "Taylor Swift"}
    ]

    result = search_by_artist(songs, "Adele")

    assert result == []


def test_empty_songs():
    assert search_by_artist([], "Taylor Swift") == []