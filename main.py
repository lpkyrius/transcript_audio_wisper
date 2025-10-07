import whisper

def transcrever_audio(audio_path, idioma="pt"):
    # Carrega o modelo base (há opções menores e maiores)
    model = whisper.load_model("base")

    # Transcreve o áudio
    resultado = model.transcribe(audio_path, language=idioma)

    return resultado["text"]

# Exemplo de uso:
if __name__ == "__main__":
    arquivo_audio = "entrevista.mp3"
    texto_transcrito = transcrever_audio(arquivo_audio, idioma="pt")
    print(texto_transcrito)

    # Salva em arquivo
    with open("entrevista_transcrita.txt", "w", encoding="utf-8") as f:
        f.write(texto_transcrito)

    print("-----")
    print("Done!")