from win32com.client import Dispatch


def speak(str):
    speak = Dispatch("SAPI.SpVoice")  # To give voice in which you want to hear
    speak.Speak(str)  # To speak the string using given as argument


if __name__ == '__main__':
    m = input("Enter text you want to hear: ")
    speak(m)


#Try getching data with an API
#Make him read that data/top 10 news