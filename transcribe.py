def transcribe_audio(audio_path):
    import whisper
    model = whisper.load_model("base")

    result = model.transcribe(audio_path, task="translate")

    # 🔥 RETURN SEGMENTS INSTEAD OF FULL TEXT
    return result["segments"]