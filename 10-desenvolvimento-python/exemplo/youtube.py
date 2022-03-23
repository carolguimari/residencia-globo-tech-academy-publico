from pytube import YouTube

# where to save
SAVE_PATH = "E:/"  # to_do

# link of the video to be downloaded
link = ["https://www.youtube.com/watch?v=azSurpQopOk",
        "https://www.youtube.com/watch?v=Cfl0zh-LjvM"]

for i in link:
    try:
        yt = YouTube(i)
    except:
        print("Connection Error")

    # filters out all the files with "mp4" extension
    streams = yt.streams.filter(mime_type='video/mp4').get_highest_resolution()
    #streams = yt.filter('mp4')

    print(streams)

    # streams.get_highest_resolution()

    # get the video with the extension and
    # resolution passed in the get() function
    #d_video = yt.get(streams.first())

    try:
        # downloading the video
        # d_video.download(SAVE_PATH)
        streams.download()
        pass
    except:
        print("Some Error!")
print('Task Completed!')
