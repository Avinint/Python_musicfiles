import os
import fnmatch
import id3reader_p3 as id3reader

def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        caps_name = artist_name.upper()
        # for artist in fnmatch.filter(directories, artist_name):
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            print (subdir)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album

def find_songs(albums):
    for album in albums:
        print("album:", album[0])
        for song in os.listdir(album[0]):
            yield song

def get_files(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, f'*.{extension}'):
            print(file)
            file = os.path.join(os.path.abspath(path), file)
            yield  file


def file_from_two_folders(folder1, folder2):
    for path, directories, files in os.walk(folder1):

        if folder2 in path:
            for file in files:
                yield os.path.join(path, file)


# album_list = find_albums("d:\music", "Black*")
# song_list = find_songs(album_list)
# for a in album_list:
#     print(a)

# for s in song_list:
#     print(s)

error_list = []

for f in get_files("music", "emp3"):
    try:
        id3r = id3reader.Reader(f)
        print(f"Artist: {id3r.get_value('performer')} Album: {id3r.get_value('album')} Track: {id3r.get_value('track')} Song: {id3r.get_value('title')}")
    except:
        error_list.append(f)

for e in error_list:
    print(e)





# for f in file_from_two_folders('d:\music', 'Black Sabbath'):
#     print(f)
