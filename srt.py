import whisper

def mp3_to_srt(mp3_file, srt_file, karaoke=True):
    print("Processing audio...")
    model = whisper.load_model("small.en")
    result = model.transcribe(mp3_file, word_timestamps=karaoke)

    #result["segments"] is a list of dict
    print("Audio processed!  Creating srt...")
    output = open(srt_file, "w")

    #result["segments"][3][words][first_word (I have to know the words)]

    #create and write the srt file
    if (karaoke):
        for segment in result["segments"]:
            curr_id = 0
            for i in range(len(segment["words"])):
                fin = ""
                for word in segment["words"]:
                    if (segment["words"][i]["word"] != word["word"]):
                        fin += word["word"]
                    else:
                        fin += f"<font color=\"#fbff1c\">{word['word']}</font>"
                output.write(f"{curr_id}\n")
                curr_id += 1
                if (i != len(segment["words"])-1):
                    output.write(f"{formatTimestamp(segment['words'][i]['start'])} --> {formatTimestamp(segment['words'][i+1]['start'])}\n")
                else:
                    output.write(f"{formatTimestamp(segment['words'][i]['start'])} --> {formatTimestamp(word['end'])}\n")
                output.write(f"{fin.strip()}\n\n")
    else:
        for segment in result["segments"]:
            output.write(f"{segment['id']}\n")
            output.write(f"{formatTimestamp(segment['start'])} --> {formatTimestamp(segment['end'])}\n")
            output.write(f"{segment['text'].strip()}\n\n") #strip avoids leading spaces i.e. "hello world" instead of " hello world"
        output.close()
    

#takes a timestamp in seconds.seconds (its a float) and outputs it as a string of "hours:seconds:minutes,milliseconds" - that is, "00:00:00,000"
def formatTimestamp(timestamp):
    #calculate timestamps
    hour = int(timestamp // 360) #360 seconds in an hour
    minute = int(timestamp % 360 // 60) 
    second = int(timestamp % 60)
    millisecond = int(timestamp*1000 % 1000)

    #pad timestamps with 0's if needed
    if (hour < 10):
        hour = f"0{hour}"

    if (minute < 10):
        minute = f"0{minute}"

    if (second < 10):
        second = f"0{second}"

    if (millisecond < 10):
        millisecond = f"00{millisecond}"
    elif (millisecond < 100):
        millisecond = f"0{millisecond}"

    #return formatted result
    return f"{hour}:{minute}:{second},{millisecond}"
"""
    for i, segment in enumerate(result["segments"]):
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        subtitles.append(srt.Subtitle(
            index = i+1,
            start = srt.timedelta(seconds=start),
            end = srt.timedelta(seconds=end),
            content = text
        ))

    with open(srt_file, "w") as f:
        f.write(srt.compose(subtitles))
"""

if __name__ == "__main__":
    mp3_file = "your_audio_file.mp3"
    srt_file = "output_subtitles.srt"
    mp3_to_srt(mp3_file, srt_file)

#mp3_to_srt("test_audio.mp3","output.srt")