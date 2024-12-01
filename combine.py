from moviepy.editor import *
import ffmpeg
#crop video
#add audio to video
#add srt subs to video

def createVideo(videoPath, audioPath, srtPath):
    #load video and audio
    video = VideoFileClip(videoPath)
    audio = AudioFileClip(audioPath)
    print(type(audio))

    video = trimVideoToAudio(video, audio)
    video = addAudioToVideo(video, audio)
    video = saveTempVidFile(video)
    #get audio length
    """
    srt = open(srtPath, "r")
    lines = [line for line in srt]
    final_codes = lines[len(lines)-4]
    final_code = final_codes[len(final_codes)-12]
    audio_length = final_code[:2]*360 + final_code[3:5]*60 + final_code[6:8] + final_code[9:]*.001
    """

    pass

#takes videoClip and audioClip, cuts videoClip to be only as long as audio clip
def trimVideoToAudio(video, audio):
    print(type(audio))
    trimmed_video = video.subclip(0, audio.duration)
    return trimmed_video

#takes videoClip and audioClip, adds audio t ovideo
def addAudioToVideo(video, audio):
    video = video.set_audio(audio)
    return video

def saveTempVidFile(video):
    video.write_videofile("temp_putput.mp4")

videoPath = "videoplayback.mp4"
audioPath = "test_audio.mp3"
srtPath = "sub.srt"

createVideo(videoPath, audioPath, srtPath)