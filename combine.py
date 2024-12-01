import subprocess
#crop video
#add audio to video
#add srt subs to video

def createVideo(video_path, audio_path, srt_path):
    #get audio length
    audio_duration = getAudioDuration(srt_path)
    trimVideo(video_path, audio_duration)
    addSubsToVideo("temp_trimmed_video.mp4",srt_path)
    addAudioToVideo("temp_trimmed_subs_video.mp4", audio_path)
    
def getAudioDuration(srt_path):
    srt = open(srt_path, "r")
    lines = [line for line in srt]
    last_stamps = lines[len(lines)-3] #00:03:24,040 --> 00:03:25,960
    last_stamp = last_stamps[len(last_stamps) - len("00:00:00,000")-1:] #00:03:25,960
    print("LAST STAMP: " + last_stamp)
    duration = f"{last_stamp[:8]}.{last_stamp[9:-2]}" #00:03:25.960
    print("THE DURATION" + duration)
    return duration

def trimVideo(video_path, audio_duration):
    try:
        command = [
            "ffmpeg",
            "-y",
            "-i", video_path,
            "-ss", "00:00:00.000",
            "-to", audio_duration,
            "-c", "copy",
            "temp_trimmed_video.mp4"
            ]
        
        subprocess.run(command, check=True)
    
    except subprocess.CalledProcessError as e:
        print(f" Something went wrong while cutting the video: {e}")
    except FileNotFoundError:
        print("FFmpeg isn't around D:")

def addSubsToVideo(video_path, srt_path):
    try:
        command = [
            "ffmpeg",
            "-y",
            "-i", video_path,
            "-vf", f"subtitles={srt_path}:force_style='Alignment=6,MarginV=140'",
            "-c:a", "copy",
            "temp_trimmed_subs_video.mp4"

        ]

        subprocess.run(command, check=True)

    except subprocess.CalledProcessError as e:
        print(f" Something went wrong while cutting the video: {e}")
    except FileNotFoundError:
        print("FFmpeg isn't around D:")

def addAudioToVideo(video_path, audio_path):
    try:
        command = [
            "ffmpeg",
            "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c", "copy",
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-shortest",
            "output.mp4"
        ]
    
        subprocess.run(command, check=True)

    except subprocess.CalledProcessError as e:
        print(f" Something went wrong while cutting the video: {e}")
    except FileNotFoundError:
        print("FFmpeg isn't around D:")


    

video_path = "tinyplayback.mp4"
audio_path = "test_audio.mp3"
srt_path = "sub.srt"

createVideo(video_path, audio_path, srt_path)