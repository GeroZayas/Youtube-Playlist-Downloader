# YouTube Downloader

# -----------------------------------------------------------------------

from pytube import YouTube
from pytube import Stream
from tqdm import tqdm
from rich import print
from Get_Urls_Youtube_List import get_video_urls_from_playlist

# we import playsound to be use sound markers after some tasks are completed
# or run
# from playsound import playsound as play

# We import datetime to print the date of
# downloaded videos later
import datetime

date_time = datetime.datetime.now()

the_date = date_time.strftime("%B %d %Y - %I %M %p")


def progress_callback(
    the_stream: Stream, data_chunk: bytes, bytes_remaining: int
) -> None:
    pbar.update(len(data_chunk))


# ---------- PRINT TITLE ---------------

print(
    """
                        [bold yellow]+-+-+-+-+-+-+        
                        | G e r o ' s |        
                            +-+-+[/bold yellow][bold red]-+-+-+-+-+     
                            | Y o u T u b e |      
                            +-+-+-+-+-+-+-+[/bold red][bold blue]-+-+-+
                                    [bold blue]| D o w n l o a d e r |
                                    +-+-+-+-+-+-+-+-+-+-+[/bold blue]
      """
)

# ---------- END OF PRINT TITLE ---------------


# We create a list of links to save them and be able to iterate over them later
list_of_links = []

# we create a boolean value 'running' to set program to be running or not
running = True

while running:
    print("If you want to add [bold red]Link by Link[/bold red] insert '1'")
    print()  # ADD SOME SPACE
    print("If you want to add a [bold red]Playlist[/bold red] link insert '2'")
    print()  # ADD SOME SPACE
    user_answer_link_or_playlist = input(">>> ")

    # In case of LINK BY LINK:
    if user_answer_link_or_playlist == "1":
        print("[bold yellow]Insert Link[/bold yellow]")
        new_link = input("HERE: ")
        list_of_links.append(new_link)

        user_answer = input(
            """
            Another link? 
            
            Press 'y' or 'n'
            
            """
        )

        print()  # add a line break

        if user_answer in ["n", "N"]:
            break
        elif user_answer in ["y", "Y"]:
            continue
        else:
            print("WRONG INPUT\n")
            continue

    elif user_answer_link_or_playlist == "2":
        a_playlist = input("Insert the playlist link: ")
        list_of_links = get_video_urls_from_playlist(a_playlist)
        break


# ---------------------------------------------------------------------

# We create a counter to number the elements being downloaded
counter = 0
for link in list_of_links:
    print("[bold yellow]--[/bold yellow]" * 30)

    counter += 1

    # We check if the input link is valid, only true if it starts with 'https'
    if link[0:5] == "https":
        url = link
        # Added -> use_oauth=True, allow_oauth_cache=True <- to make it work
        # it forces the user to connect to a google account
        # this is a temporary fix
        yt = YouTube(
            url,
            on_progress_callback=progress_callback,
            use_oauth=True,
            allow_oauth_cache=True,
        )
        stream = yt.streams.get_highest_resolution()
        print(f"[bold yellow]downloading....[/bold yellow] {counter} =>\n")

        print(
            f"[bold blue]Downloading video [/bold blue] '[bold yellow]{stream.default_filename}[/bold yellow]' "
        )

        # Here we want to know how big the file is and we let the user know
        video_size_bytes = stream.filesize

        # we convert bytes to megabytes to make more readable
        video_size_mb = f"{video_size_bytes / 1048576:.2f} MB"
        print("[bold blue]This is the video's size ->[/bold blue]", video_size_mb, "\n")

        path_to_download_folder = "/home/gero/Videos/"

        try:
            # video.download(path_to_download_folder)
            pbar = tqdm(total=stream.filesize, colour="green")
            path = stream.download(path_to_download_folder)
            pbar.close()

            print()  # add a line break
            print(
                f"[bold red]Downloaded! :) here => [/bold red] {path_to_download_folder} "
            )

            # ----------- SAVE TXT FILE WITH DATA FROM PROGRAM --------

            try:
                with open(
                    f"{path_to_download_folder}Downloaded Videos.txt", "a"
                ) as file:
                    file.write(
                        f"""
{stream.default_filename} -> {the_date}
                               """
                    )
            except Exception:
                pass

            # we play the sound of successful download
            try:
                play("./sounds/video_dowloaded.mp3")
            except Exception:
                pass

        except Exception:
            print(
                f"\n[bold yellow]Video ->[/bold yellow] {stream.default_filename} not downloaded -> SOME PROBLEM TOOK PLACE\n"
            )
            # play("./sounds/some_video_did't_work (enhanced).wav")
            continue

    else:
        print("video url incorrect")

# --------------------- PROGRAM COMPLETED ------------------------------

print(
    """

      [bold green]ALL DONE BABY!!![/bold green]

      """
)

try:
    play("./sounds/all_dowloads_completed.mp3")
except Exception:
    pass
