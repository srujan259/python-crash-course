def make_album(artist_name, album, no_of_songs=None):
    """ Dictionary of artists and songs """
    artist_details = {'artist_name':artist_name, 'album': album}
    if no_of_songs:
        artist_details['no_of_songs'] = no_of_songs
    return artist_details

while True:
    print('Enter details of artists')
    print('(Press q to quit at any time)\n')
    a_name = input("Artist Name:")
    if a_name == 'q':
        break
    album = input("Album:")
    if album == 'q':
        break
    no_of_songs = input("No of songs(optional)")
    if no_of_songs == 'q':
        break
    artist = make_album(a_name, album, no_of_songs)
    print(artist)