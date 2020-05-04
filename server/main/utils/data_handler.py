def load_data():
    import pandas as pd
    return pd.read_csv('utils/spotify_data.csv')

music_df = load_data()

def look_for_song(df, name):
    return df[df.song.str.contains(name.lower(), na=False)]

def look_for_artist(df, name):
    return df[df.artist.str.contains(name.lower(), na=False)]

def getSongId(song, artist=None):
    song_df = look_for_song(music_df, name=song)
    
    if song_df.empty:
        return None
    elif song_df.shape[0] >= 1 and not artist:
        return song_df.index.values[0]
    elif song_df.shape[0] > 1 and artist:
        artist_df = look_for_artist(song_df, name=artist)
        if artist_df.empty:
            return song_df.index.values[0]
        else:
            return artist_df.index.values[0]
    else:
        return None

def getKMusic(scores, id, k):
    sorted_scores = sorted(((value, index) for index, value in enumerate(scores) if index!=id), reverse=False)
    return [sorted_scores[i][1] for i in range(k)]

def getDictResult(musics):
    res = []
    for i in range(len(musics)):
        x = musics[i]
        d = {i+1: {'song' : music_df.song.iloc[x], 'artist' : music_df.artist.iloc[x],
             'spotify_url' : 'https://open.spotify.com/track/{}'.format(music_df.spotify_id.iloc[x])}} 
        res.append(d)
    return res

