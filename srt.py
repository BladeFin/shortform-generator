import whisper
import pronouncing

def mp3_to_srt(mp3_file, srt_file):
    model = whisper.load_model("small.en")
    result = model.transcribe(mp3_file)

    #result["segments"] is a list of dict
    output = open("sub.srt", "w")


    # Process the result segments
    caption_id = 1
    for segment in result["segments"]:
        words = segment["text"].strip().split()  # Split text into words
        start_time = segment["start"]

        # Iterate through the words, creating smaller segments
        for i in range(0, len(words), 1): #replace 5 w/ max_words
            chunk = words[i:i + 1]  # Get up to max_words per caption #replace 5 w/ max_words
            end_time = start_time + (segment["end"] - segment["start"]) * (countSyllables(chunk) / countSyllables(words))

            # Write the SRT entry
            output.write(f"{caption_id}\n")
            output.write(f"{formatTimestamp(start_time)} --> {formatTimestamp(end_time)}\n")
            output.write(f"{' '.join(chunk)}\n\n")

            start_time = end_time  # Update start time for the next chunk
            caption_id += 1
    
    output.close()
    
def countSyllables(lst):
    fin = 0
    for val in lst:
        try:
            fin += pronouncing.syllable_count(pronouncing.phones_for_word(val)[0])
        except:
            fin += len(val)/3
    return fin

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


#if __name__ == "__main__":
#    mp3_file = "your_audio_file.mp3"
#    srt_file = "output_subtitles.srt"
#    mp3_to_srt(mp3_file, srt_file)
"""
mp3_to_srt("test_audio.mp3","output.srt")