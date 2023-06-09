import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get a list of available voices
voices = engine.getProperty('voices')

# Print the available voices
for voice in voices:
    print(voice.id)

# Set the desired voice
voice_id = "com.apple.speech.synthesis.voice.samantha"  # Example voice ID, replace with your preferred voice ID
engine.setProperty('voice', voice_id)

# Set other properties if desired
engine.setProperty('rate', 100)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.5)  # Volume level (0.0 to 1.0)

# Say the text using the selected voice
text = "Oye Oye Lucky Lucky Oye"
engine.say(text)
engine.runAndWait()
