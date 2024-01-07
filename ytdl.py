import subprocess
import os

def download_video(url, extension, t0, t1):
    print("Téléchargement en cours avec l'extension {}:\n".format(extension), url, t0, t1)
    if (t0 != "\n") and (t1 != "\n") :
        download_part(url, extension, t0, t1)
    else:
        download_full(url, extension)

def download_part(url, extension, t0, t1,):
    video_name = url.split('=')[1]
    output_path = r"C:\Users\Florian\Desktop\projets_random\ytdownload\media"
    pass

def download_full(url, extension):
    video_name = url.split('=')[1]
    output_path = r"C:\Users\Florian\Desktop\projets_random\ytdownload\media"
    os.chdir(output_path)
    # print(subprocess.run("dir", shell=True, capture_output=True, text=True))

    print("Downloading the entire video.. ")

    webm_dl = 'yt-dlp "'+ url +'" -o ' + video_name +'.webm'
    webm_suppr = 'del '+ video_name+ '.webm'

    if (extension == ".mp4") :
        webm_convert = 'ffmpeg -i '+video_name+'.webm -c copy '+video_name+extension
        print("selected type:mp4")
    else :
        webm_convert = 'ffmpeg -i '+video_name+'.webm -q:a 0 -map a '+video_name+extension
        print("selected type:mp3")

    webm_dl =webm_dl.replace("\n", "")
    webm_convert = webm_convert.replace("\n", "")
    webm_suppr = webm_suppr.replace("\n", "")

    # print(webm_dl)
    # print(webm_convert)
    # print(webm_suppr)


    subprocess.run(webm_dl, shell=True)
    subprocess.run(webm_convert, shell=True)
    subprocess.run(webm_suppr, shell=True)
    print("Download complete")
