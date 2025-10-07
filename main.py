import whisper

def transcrever_audio(audio_path, lang="pt"):
    # Loads base model (There are smaller and larger options)
    model = whisper.load_model("base")
    # model = whisper.load_model("medium")

    # transcribes the audio
    result = model.transcribe(audio_path, language=lang)

    return result["text"]

# Use example:
if __name__ == "__main__":
    audio_file = "interview.mp3"
    transcribed_text = transcrever_audio(audio_file, lang="pt")
    print(transcribed_text)

    # Salva em arquivo
    with open("interview_transcrita.txt", "w", encoding="utf-8") as f:
        f.write(transcribed_text)

    print("Done! Check the interview_transcrita.txt file")