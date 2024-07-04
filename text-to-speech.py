import win32com.client as wincom

voice= wincom.Dispatch("SAPI.SpVoice")

print("Hello User !!!")
text=input("Enter your text here to listen: ")
voice.Speak( text )
