#!/usr/bin/env python
from os import urandom
from base64 import urlsafe_b64encode
import youtube_dl
from youtube_dl.utils import DownloadError
import threading
import time

LEARNING_TO_LIVE = "https://www.youtube.com/watch?v=1VigPPJ6j40"

def get_random_video_url():

    URL_FORMAT = 'https://youtube.com/watch?v={}'
    target = urlsafe_b64encode(urandom(8)).decode('utf-8').rstrip('=')
    return URL_FORMAT.format(target)

def verify_if_valid(url):
  
    params = {'skip_download':True, 'quiet':True}
    downloader = youtube_dl.YoutubeDL(params)

    try:
        downloader.download([url])
    except DownloadError:
        return False
  
    return True

def try_download():
    
    url = get_random_video_url()

    if verify_if_valid(url):

        print("Found! {}".format(url))
        youtube_dl.YoutubeDL().download([url])

def launch_threads():

    for i in range(10):
        threading.Thread(target=try_download).start()



if __name__ == "__main__":

    while [1]:
        launch_threads()
        time.sleep(1)

#    assert(verify_if_valid(get_random_video_url()) is False)
#    assert(verify_if_valid(LEARNING_TO_LIVE) is True)
