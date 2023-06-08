import pyttsx3
engine = pyttsx3.init()
text = " Oye Oye Lucky Lucky Oye,O Lucky Lucky Oye O Lucky O Le Petrol To Pawaaya Hi Ni Koi Gal Ni,Saaddi Gaddi Te Goodwill Naal Chal Di A ?"
engine.say(text)
engine.runAndWait()
engine.setProperty('rate', 100)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.1)  # Volume level (0.0 to 1.0)
