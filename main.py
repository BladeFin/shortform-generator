from tts import generateTTS
from srt import mp3_to_srt
from combine import createVideo
from segment import segmentVideo
import os

def generateViralVideo(script_path, temp_audio_output, temp_srt_output, source_video_path, video_output_path, randomize=False, karaoke=True, lang='en', tld='com', flush=True):
    checkExistence([script_path, source_video_path])
    script = readFileAsString(script_path)
    generateTTS(script, temp_audio_output, lang=lang, tld=tld)
    mp3_to_srt(temp_audio_output, temp_srt_output, karaoke=karaoke)
    createVideo(source_video_path, temp_audio_output, temp_srt_output, video_output_path, randomize=randomize)
    if (flush):
        flushTempFiles([temp_audio_output, temp_srt_output])
    segmentVideo(video_output_path)
    

#Checks if all of the files in path_list exist, raising an error if any are missing
def checkExistence(path_list):
    for path in path_list:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Error: The file '{path}' does not exist.  Generation halted.")

#returns the contents of a text file as a strings
def readFileAsString(text_file_path):

    with open(text_file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    return file_content

#Deletes all files in path_list
def flushTempFiles(path_list):
    for path in path_list:
        try:
            os.remove(path)
        except (...):
            print(f"Odd, {path} couldn't be deleted or wasn't found...")

if (__name__ == "__main__"):
    script_path = "scripts/protective_ex"
    temp_audio_output = "temp_audio_output.mp3"
    temp_srt_output = "temp_subs.srt"
    source_video_path = "inputs/parkour_recording_trimmed.mkv"
    video_output_path = f"outputs/{script_path[:8]}.mp4"
    generateViralVideo(script_path, temp_audio_output, temp_srt_output, source_video_path, video_output_path, randomize=True, karaoke=True, lang='en', tld='com.au', flush=True)

