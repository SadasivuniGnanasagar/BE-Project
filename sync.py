import os

def merge_audio_segments(audio_files):
    """
    Takes list of segment audio files with start times,
    adds delay, and merges into one final audio file.
    """

    delayed_files = []

    # Step 1: Add delay to each segment
    for i, item in enumerate(audio_files):
        input_file = item["file"]
        delay = item["start"]  # in milliseconds
        output_file = f"outputs/segments/delayed_{i}.mp3"

        cmd = f'ffmpeg -i "{input_file}" -af "adelay={delay}|{delay}" "{output_file}" -y'
        os.system(cmd)

        delayed_files.append(output_file)

    # Step 2: Merge all delayed audio files
    inputs = " ".join([f'-i "{f}"' for f in delayed_files])

    final_audio = "outputs/final_audio.mp3"

    cmd = f'ffmpeg {inputs} -filter_complex amix=inputs={len(delayed_files)} "{final_audio}" -y'
    os.system(cmd)

    return final_audio


def merge_with_video(video_path, audio_path):
    """
    Replace original video audio with translated audio
    """

    output_video = "outputs/output.mp4"

    cmd = f'ffmpeg -i "{video_path}" -i "{audio_path}" -map 0:v -map 1:a -c:v copy -shortest "{output_video}" -y'
    os.system(cmd)

    return output_video