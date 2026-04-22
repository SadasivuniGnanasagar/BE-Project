import os
import gradio as gr

from utils.audio import extract_audio
from pipeline.transcribe import transcribe_audio
from pipeline.translate import translate_segments   # ✅ NEW
from pipeline.tts import generate_tts_segments      # ✅ NEW
from pipeline.sync import merge_audio_segments, merge_with_video  # ✅ NEW


def process(video_path):
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("outputs/segments", exist_ok=True)

    audio_path = "outputs/audio.wav"
    final_video = "outputs/output.mp4"

    print("\n========== START PROCESS ==========\n")

    # STEP 1: Extract audio
    print("Step 1: Extracting Audio...")
    extract_audio(video_path, audio_path)
    print("Audio exists:", os.path.exists(audio_path))

    # STEP 2: Transcribe (WITH TIMESTAMPS)
    print("\nStep 2: Transcribing...")
    segments = transcribe_audio(audio_path)   # now returns segments
    print("Total segments:", len(segments))

    # STEP 3: Translate each segment
    print("\nStep 3: Translating...")
    translated_segments = translate_segments(segments)
    print("Sample:", translated_segments[0]["text"] if translated_segments else "None")

    # STEP 4: Generate TTS per segment
    print("\nStep 4: Generating Speech...")
    tts_files = generate_tts_segments(translated_segments)
    print("Generated segments:", len(tts_files))

    # STEP 5: Merge all segments into one synced audio
    print("\nStep 5: Syncing Audio...")
    final_audio = merge_audio_segments(tts_files)
    print("Final audio exists:", os.path.exists(final_audio))

    # STEP 6: Merge with video (REPLACE original audio)
    print("\nStep 6: Merging with Video...")
    output_video = merge_with_video(video_path, final_audio)
    print("Final video exists:", os.path.exists(output_video))

    print("\n========== DONE ==========\n")

    return output_video


def ui(video):
    return process(video)


gr.Interface(
    fn=ui,
    inputs=gr.Video(label="Upload Video"),
    outputs=gr.Video(label="Translated Video"),
    title="🎬 Futurecine - AI Video Translator",
    description="Upload a video → Get translated & dubbed output"
).launch()