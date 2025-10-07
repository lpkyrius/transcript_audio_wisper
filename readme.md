# Audio Transcription with Whisper

A simple Python script that uses OpenAI's Whisper model to transcribe audio files to text. This tool is particularly useful for converting speech in audio files into written text, supporting multiple languages.

## Features

- Transcribes audio files to text using OpenAI's Whisper model
- Supports multiple languages (default is Portuguese)
- Saves transcriptions to text files
- Simple and easy to use

## Requirements

- Python 3.6 or higher
- FFmpeg (required by Whisper)

### Installation

1. Install FFmpeg:
   - On macOS: `brew install ffmpeg`
   - On Ubuntu/Debian: `sudo apt update && sudo apt install ffmpeg`
   - On Windows: Download from [FFmpeg's official website](https://ffmpeg.org/download.html)

2. Install the required Python package:
   ```bash
   pip install -U openai-whisper

## Usage

1. Place your audio file (e.g., interview.mp3) in the project directory

2. Run the script:
```bash 
python main.py
```

3. The transcription will be saved as ```transcribed_interview.txt```


## Customization
You can modify the main.py file to:

- Change the input audio file name

- Specify a different language (e.g., "en" for English, "es" for Spanish)

- Adjust the model size for better accuracy

- Options: ```tiny```, ```base```, ```small```, ```medium```, ```large```

## Notes

- The first run will download the Whisper model (default: ```base```)

- Larger models offer better accuracy but require more memory and processing time

- Supported audio formats: MP3, WAV, M4A, and others compatible with FFmpeg

## License

This project is open source and available under the MIT License.