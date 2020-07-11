import pafy
import youtube_dl
import os
import ffmpeg
import vlc


x = input("Link:")
vid = pafy.new(x)
print(vid.title)
y = input("Is the video correct(y/n):")
if y == "n":
        exit()
t = input("Video or Audio(a/v):")
if t == "v":
        z = input("Stream or download(s/d):")
        if z == "s":
                best = vid.getbest()
                playurl = best.url
                ins = vlc.Instance()
                player = ins.media_player_new()
                Media = ins.media_new(playurl)
                Media.get_mrl()
                player.set_media(Media)
                player.play()
        elif z == "d":
                best = vid.getbest()
                best.download()
        
if t == "a":
        r = input("Stream or download(s/d):")
        if r == "s":
                bestaudio = vid.getbestaudio()
                playurl = bestaudio.url
                ins = vlc.Instance()
                player = ins.media_player_new()
                Media = ins.media_new(playurl)
                Media.get_mrl()
                player.set_media(Media)
                player.play()
        elif r =="d":
                l = input("Mp3 or Webm(m/w):")
                if l == "m":
                        ydl_opts = {
                                'format': 'bestaudio/best',
                                'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '320',}],
                            }
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                ydl.download([x])

                elif l == "w":
                        bestaudio = vid.getbestaudio()
                        bestaudio.download()

                
                





