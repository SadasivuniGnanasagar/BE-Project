# BE-Project
It performs speech recognition → translation → text-to-speech → video merging to generate a fully translated video.

🚀 Features
🎤 Extract audio from video
🧠 Speech-to-text using Whisper
🌐 Language translation using Argos Translate
🔊 Text-to-speech generation (Hindi voice)
🎞️ Sync translated audio with original video
🖥️ Simple UI using Gradio
🏗️ Project Pipeline
Audio Extraction
Extracts audio from input video using FFmpeg
Speech Recognition
Converts audio → text using Whisper
Supports multilingual input (e.g., Telugu)
Translation
Translates text from English → Hindi using Argos Translate
Text-to-Speech
Converts translated text into speech using gTTS
Audio Synchronization
Aligns translated audio segments with timestamps
Video Merging
Combines translated audio with original video
📁 Project Structure
futurecine/
│── app.py
│── outputs/
│── utils/
│   └── audio.py
│── pipeline/
│   ├── transcribe.py
│   ├── translate.py
│   ├── tts.py
│   └── sync.py
⚙️ Installation
1. Clone the repository
git clone <your-repo-link>
cd futurecine
2. Create virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install gradio openai-whisper argostranslate gTTS moviepy
4. Install FFmpeg
Download from: https://ffmpeg.org/download.html
Add to system PATH
▶️ Run the Project
python app.py

Open browser:

http://127.0.0.1:7860
🎯 Usage
Upload a video file
Wait for processing:
Audio extraction
Transcription
Translation
TTS generation
Merging
Download translated video output
🌍 Supported Flow
Input: Telugu / English / other languages
Output: Hindi (voice translated video)
⚠️ Limitations
Not perfect lip-sync (approx. 80–90% accuracy)
TTS voice may sound robotic
Processing time depends on video length
Requires internet for gTTS
🔮 Future Improvements
🎯 Better voice models (Coqui TTS)
🎬 Subtitle generation (SRT)
🌐 Multiple language selection
⚡ Faster processing with GPU
🎭 Emotion-aware voice synthesis
🧠 Tech Stack
Python
Whisper (Speech Recognition)
Argos Translate
gTTS
FFmpeg
Gradio
