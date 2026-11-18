import csv

def load_song(filepath: str) -> list[dict]:
    with open(
        filepath,
        "r",
        encoding="latin-1",
        newline=""
    ) as file:
        return list(csv.DictReader(file))

def show_songs(songs: list[dict]) -> None:
    # print(songs[0].keys())
    for song in songs[:5]:
        print(f"Song: {song["track_name"]} | Artist: {song["artist(s)_name"]}")

def count_songs(songs: list[dict]) -> int:
    return len(songs)


def search_by_artist(
    songs: list[dict],
    artist: str
) -> list[dict]:

    artist_normalize = artist.strip().lower()
    return list(
        filter(
            lambda song: song["artist(s)_name"].strip().lower() == artist_normalize,
            songs
        )
    )


def main():
    songs = load_song("data/spotify-2023.csv")
    
    print("Total song:", count_songs(songs))
    
    show_songs(songs)
    result = search_by_artist(songs, " taylor SWIFT ")    
    
    print(result)
if __name__ == "__main__":
    main()