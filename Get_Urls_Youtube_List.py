def get_video_urls_from_playlist(the_playlist):
    from pytube import Playlist

    playlist = Playlist(the_playlist)

    list_of_video_urls = []
    for video in playlist:
        list_of_video_urls.append(video)

    return list_of_video_urls


if __name__ == "__main__":
    a_playlist = input("Insert the playlist link: ")
    get_video_urls_from_playlist(a_playlist)
