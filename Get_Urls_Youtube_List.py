import re


def get_video_urls_from_playlist(the_playlist):
    from pytube import Playlist

    playlist = Playlist(the_playlist)

    list_of_video_urls = []
    for video in playlist:
        list_of_video_urls.append(video)

    # print(list_of_video_urls)
    return list_of_video_urls


if __name__ == "__main__":
    print(
        """
          It must be a public Playlist
          """
    )
    a_playlist = input("Insert the playlist link: ")
    get_video_urls_from_playlist(a_playlist)
