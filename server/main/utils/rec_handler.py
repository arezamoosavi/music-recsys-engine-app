from utils.data_handler import *

def similarty(s1,s2):
    
    score_diff = 10000 * abs(float(s1['score'])-float(s2['score']))
    acous_diff = 1000 * abs(float(s1['acousticness'])-float(s2['acousticness']))
    dancb_diff = 100 * abs(float(s1['danceability'])-float(s2['danceability']))
    energ_diff = 30 * abs(float(s1['energy'])-float(s2['energy']))
    liven_diff = 100 * abs(float(s1['liveness'])-float(s2['liveness']))
    loudn_diff = 10 * abs(float(s1['loudness'])-float(s2['loudness']))
    spech_diff = 100 * abs(float(s1['speechiness'])-float(s2['speechiness']))
    tempo_diff = 0.1 * abs(float(s1['tempo'])-float(s2['tempo']))
    valnc_diff = 10 * abs(float(s1['valence'])-float(s2['valence']))
    
    difference = score_diff + acous_diff + dancb_diff**2 + energ_diff**2 \
    + liven_diff**2 + loudn_diff**2 + spech_diff**2 + tempo_diff + valnc_diff**2
    
    return difference

def getMusic(song, artist=None, k=6):
    id = getSongId(song=song, artist=artist)
    if id:
        list_of_score = []
        for songid in range(music_df.shape[0]):
            list_of_score.append(similarty(music_df.iloc[id],
                                           music_df.iloc[songid]))            
        
        list_of_musicid = getKMusic(list_of_score, id, k)
        
        return getDictResult(list_of_musicid)
        
    else:
        return None