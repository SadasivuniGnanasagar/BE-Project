from gtts import gTTS
import os

def generate_tts_segments(translated_segments):
    os.makedirs("outputs/segments", exist_ok=True)

    files = []

    for i, seg in enumerate(translated_segments):
        filename = f"outputs/segments/seg_{i}.mp3"

        # Generate speech
        tts = gTTS(text=seg["text"], lang="hi")
        tts.save(filename)

        files.append({
            "file": filename,
            "start": int(seg["start"] * 1000)  # convert seconds → ms
        })

    return files