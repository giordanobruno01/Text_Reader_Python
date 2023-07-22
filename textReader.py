from IPython.display import Audio,display
from gtts import gTTS
from playsound import playsound
import gtts.lang
import time

dictio = gtts.lang.tts_langs()
number = 1

while(True):
  tex = input("write something ")
  for i in dictio:
    print(i , " for ",dictio.get(i))
    number+=1
  language = input()
  if language not in dictio:
    print("wrong input")
  else:
    v = gTTS(text = tex,lang=language, slow = False)
    v.save("voice.mp3")
    sound_file="/content/voice.mp3"

    display(Audio(sound_file, autoplay=True))
    time.sleep(15)
  contin = input("press 0 to exit or anything to continue ")
  if(contin.strip() == "0"):
    exit() 