from argostranslate import package, translate

def install_language_model(from_code="en", to_code="hi"):
    print("Downloading language model...")

    available_packages = package.get_available_packages()
    
    pkg = next(
        (p for p in available_packages if p.from_code == from_code and p.to_code == to_code),
        None
    )

    if pkg is None:
        raise Exception("Language pair not found!")

    package_path = pkg.download()
    package.install_from_path(package_path)

    print("Installed successfully!")
    

def translate_text(text, from_lang="en", to_lang="hi"):
    installed_languages = translate.get_installed_languages()

    from_lang_obj = next((l for l in installed_languages if l.code == from_lang), None)
    to_lang_obj = next((l for l in installed_languages if l.code == to_lang), None)

    if from_lang_obj is None or to_lang_obj is None:
        print("Installing missing language model...")
        install_language_model(from_lang, to_lang)
        return translate_text(text, from_lang, to_lang)

    translation = from_lang_obj.get_translation(to_lang_obj)
    return translation.translate(text)


# ================== ✅ ADD THIS NEW FUNCTION ==================

def translate_segments(segments, from_lang="en", to_lang="hi"):
    translated = []

    for seg in segments:
        translated_text = translate_text(seg["text"], from_lang, to_lang)

        translated.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": translated_text
        })

    return translated