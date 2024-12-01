from tts import generateTTS
from srt import mp3_to_srt
from combine import createVideo
import os

def generateViralVideo(script, temp_audio_output, temp_srt_output, source_video_path, video_output_path, randomize=False, karaoke=True, lang='en', tld='com', flush=True):
    #generateTTS(script, temp_audio_output, lang=lang, tld=tld)
    #mp3_to_srt(temp_audio_output, temp_srt_output, karaoke=karaoke)
    createVideo(source_video_path, temp_audio_output, temp_srt_output, video_output_path, randomize=randomize)
    if (flush):
        try:
            os.remove(temp_audio_output)
        except (...):
            print(f"Odd, {temp_audio_output} couldn't be deleted or wasn't found...")
        try:
            os.remove(temp_srt_output)
        except (...):
            print(f"Odd, {temp_srt_output} couldn't be deleted or wasn't found...")

if (__name__ == "__main__"):
    script = """
    What is the scariest thing that's ever happened to you?

    So, I’m sitting at home last night, scrolling through my phone like usual, when I get a random text invite to a group chat. I don’t recognize the number, but curiosity gets the best of me, so I join.

    The first message I see? “Make sure there’s no blood left in the trunk.”

    I froze. At first, I thought it was some stupid prank or maybe someone trolling, but then the next message comes in: “We need to dump it before sunrise. No mistakes this time.”

    THIS TIME? Excuse me? My first instinct was to leave the chat, but I didn’t want to seem suspicious. Then someone else in the group says, “Where’s the drop point?”

    At this point, I’m sweating. I look around my room like I’m about to get sniped through the window. Then I decide to type the most nonchalant thing I could think of to blend in: “Yeah, where are we meeting again?”

    Bad idea. Because the next thing I know, someone replies with, “Wait, who the f* is this?”**

    I’m panicking. My thumb is hovering over the “Leave Chat” button when another message comes through: “Did we get hacked?!” And then: “If they know, we’re screwed.”

    SCREWED? WHO’S SCREWED? I’m breathing like I just ran a marathon, trying to think of an excuse when one of the names in the group starts typing. But before they can send whatever terrifying thing they’re writing, I just leave the chat.

    Now I’m lying in bed, staring at the ceiling, convinced I’ve stumbled into some mob operation. I thought about calling the cops, but what do I say? “Hi, I think I just accidentally joined a murder group chat”? They’d laugh me off the phone!

    Anyway, if I disappear after posting this, you know why. Check my trunk.
    """

    temp_audio_output = "temp_audio_output.mp3"
    temp_srt_output = "temp_subs.srt"
    source_video_path = "inputs/formatted_spiral_parkour.mp4"
    video_output_path = "outputs/output.mp4"
    generateViralVideo(script, temp_audio_output, temp_srt_output, source_video_path, video_output_path, randomize=True, karaoke=True, lang='en', tld='com.au', flush=False)

