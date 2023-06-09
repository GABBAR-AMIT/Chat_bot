import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = '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'  # Your OpenAI API key goes here
engine = pyttsx3.init()


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()  # Added parentheses to create a recognizer instance
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except Exception as e:  # Catching the specific exception for easier debugging
        print('An error occurred while transcribing audio:', str(e))


def generator_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5  # Fixed typo: "temerature" to "temperature"
    )
    return response.choices[0]["text"]  # Fixed typo: "choice" to "choices"


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
        # Wait for user to say "genius"
        print("Say 'Genius' to start recording your questions...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "genius":
                    # Record audio
                    filename = "input.wav"
                    print("Say your question...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"You said: {text}")

                        # Generate response using gpt-3
                        response = generator_response(text)
                        print(f"GPT-3 says: {response}")

                        # Read response using Text-to-speech
                        speak_text(response)

            except Exception as e:
                print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
