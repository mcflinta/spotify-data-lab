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


def main():
    songs = load_song("data/spotify-2023.csv")
    
    print("Total song:", count_songs(songs))
    
    show_songs(songs)
    
if __name__ == "__main__":
    main()