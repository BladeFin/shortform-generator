# Short-Form Content Generator 🎬

A small Python media pipeline that turns a text script and background video into short-form content with generated narration, timed subtitles, and platform-specific cuts.

[See a quick demo here!](https://youtube.com/shorts/2q0wzHMRaTA)

## What it does

1. Generates an MP3 voiceover from a UTF-8 text script with Google Text-to-Speech.
2. Transcribes the voiceover with OpenAI Whisper and writes an SRT subtitle file.
3. Combines the background video, narration, and styled subtitles with FFmpeg.
4. Creates TikTok, Instagram, and YouTube output variants.

This project was built as an experiment in media automation and command-line tooling. It is intentionally a straightforward batch pipeline rather than a hosted application.

## Requirements

- Python 3.9+
- FFmpeg and FFprobe available on `PATH`
- Internet access when using gTTS (Google's service is contacted to generate speech)
- A Whisper model download on first transcription run (the default model is `small.en`)

Python dependencies are listed in [`requirements.txt`](requirements.txt).

## Setup

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install FFmpeg using your operating system's package manager or the [official FFmpeg downloads](https://ffmpeg.org/download.html), then verify:

```bash
ffmpeg -version
ffprobe -version
```

## Usage

Place text scripts in `scripts/` and a source video in `inputs/`. These directories are intentionally gitignored because media files can be large and may contain copyrighted material.

Update the example paths in `main.py`, then run:

```bash
python main.py
```

Generated files are written to `outputs/`, with platform-specific files under `outputs/tiktok/`, `outputs/instagram/`, and `outputs/youtube/`.

The main reusable entry point is `generateViralVideo`:

```python
from main import generateViralVideo

generateViralVideo(
    script_path="scripts/example.txt",
    source_video_path="inputs/background.mp4",
    video_output_path="outputs/example.mp4",
    randomize=True,
)
```

### `generateViralVideo` arguments

| Argument            | Type   | Default                   | Description                                                                      |
| ------------------- | ------ | ------------------------- | -------------------------------------------------------------------------------- |
| `script_path`       | `str`  | required                  | Path to a UTF-8 plain-text script used to generate the narration.                |
| `source_video_path` | `str`  | required                  | Path to the background video.                                                    |
| `video_output_path` | `str`  | required                  | Path where the combined MP4 should be saved.                                     |
| `temp_audio_output` | `str`  | `"temp_audio_output.mp3"` | Temporary MP3 path for generated narration.                                      |
| `temp_srt_output`   | `str`  | `"temp_subs.srt"`         | Temporary SRT path for generated subtitles.                                      |
| `randomize`         | `bool` | `False`                   | Start the background video at a random viable position instead of the beginning. |
| `karaoke`           | `bool` | `True`                    | Highlight the currently spoken word when `word_for_word=False`.                  |
| `word_for_word`     | `bool` | `True`                    | Show short groups of words instead of full Whisper segments.                     |
| `max_chars`         | `int`  | `8`                       | Maximum caption length when `word_for_word=True`. Must be positive.              |
| `lang`              | `str`  | `"en"`                    | gTTS language code.                                                              |
| `tld`               | `str`  | `"co.au"`                 | gTTS top-level domain used to select a regional accent.                          |
| `flush`             | `bool` | `True`                    | Delete the temporary MP3 and SRT files after video creation.                     |

Scripts should be plain UTF-8 text. The default subtitle mode groups words into short captions; `karaoke=True` can highlight the currently spoken word when `word_for_word=False`.

## Project structure

- `main.py` — orchestrates the complete workflow
- `tts.py` — narration generation and FFmpeg audio speed-up
- `srt.py` — Whisper transcription and SRT formatting
- `combine.py` — FFmpeg composition
- `segment.py` — platform-specific splitting
- `requirements.txt` — Python dependencies

## Known limitations

- gTTS requires network access and its available languages/accents depend on the service.
- Whisper can require substantial CPU, RAM, and disk space; transcription time depends on the selected model.
- FFmpeg is an external system dependency and must be installed separately.
- The current script is configured through constants in `main.py`; it does not yet provide a command-line interface.
- Platform duration limits are conservative project settings, not guarantees that platform policies will remain unchanged.

## License and media

No sample media is included in the repository. Only use source footage, scripts, fonts, and generated audio that you have permission to use and distribute.
