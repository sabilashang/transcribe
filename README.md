# transcribeYT 🎥✍️

**transcribeYT** is a tool for extracting and transcribing audio from YouTube videos into text files utilizing Pytube for audio extraction and Open AI's Whisper AI model for accurate language transcription.📹📝

## 🚀 Features
- 🎧 **YouTube Audio Extraction**: Downloads audio from YouTube videos for transcription.
- 🗣️ **Whisper AI Transcription**: Converts extracted audio into text using the Whisper AI model.
- 💾 **File Saving**: Saves the transcribed text into a specified file format for easy access.
- ❌ **Error Handling**: Provides informative error messages if the URL is incorrect.

# 📋 Requirements
- Python 3.x 🐍
- [pytube](https://github.com/pytube/) library 📦
- whisper library 📦
- static-ffmpeg library 📦

## 🔧 Setup:
1. Clone the repository and navigate to the folder
   - ```git clone https://github.com/sabilashang/transcribeYT.git```
   - ```cd transcribeYT```
2. Create and Activate a Virtual Environment
   - ```python -m venv .venv```
   - ```venv\Scripts\activate```
3. Install Required Packages:
   - ```pip install -r requirements.txt```
4. Ensure `ffmpeg` is installed and available in your system PATH.

## 🖥️ Usage:
1. **Run the Script**: ```python transcribeYT.py```
2. **Provide the URL**:
   - Enter a valid YouTube URL when prompted.
   - Specify the name for the output file (without extension).
   - The script will download the audio, transcribe it, and save the text in a `.doc` file.

> **Note**: The processing speed may vary based on the length of the video and your network speed.

## 📝 Example Usage
  - Enter the URL: `https://www.youtube.com/.....`
  - Save as: `transcription_output`
  - The script will generate a file named `transcription_output.doc` containing the transcript of the video.

## ⚠️ License:
This project is under No License: This code is for personal use only. Copying, modifying, or using this code for academic, commercial, or other purposes is not permitted. Feel free to reach out if required permission to reuse.

## 📫 Contact:
Feel free to reach out if you have any questions!
**Instagram**: [@sabilashan_g](https://www.instagram.com/sabilashan_g/)
