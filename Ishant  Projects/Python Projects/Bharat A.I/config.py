# todo: Add your api key here
import os
api_key = "3Ov4JqqFElGBcHKOcqLZvXmf1KpjELgR"

img_apikey = "b6416d2f15e14d8a9e0d77a0abdd3c26_4fd7f544a7bb42508477f4b44ffab4c1_andoraitools"
# import speech_recognition as sr
# import whisper

# # Whisper मॉडल लोड करें
# model = whisper.load_model("base")

# def recognize_speech_with_whisper():
#     # Recognizer ऑब्जेक्ट बनाएं
#     recognizer = sr.Recognizer()
    
#     # माइक्रोफोन से इनपुट लें
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source, duration=1)  # बैकग्राउंड नॉइज़ को एडजस्ट करें
#         audio = recognizer.listen(source)  # ऑडियो इनपुट कैप्चर करें
        
#         # ऑडियो को WAV फॉर्मेट में सेव करें (Whisper के लिए)
#         with open("temp_audio.wav", "wb") as f:
#             f.write(audio.get_wav_data())
        
#         # ऑडियो फाइल को Whisper से ट्रांसक्राइब करें
#         print("Recognizing with Whisper...")
#         result = model.transcribe("temp_audio.wav")
        
#         # ट्रांसक्रिप्शन से टेक्स्ट निकालें
#         text = result['text']
        
#         # टेक्स्ट को फ़ंक्शन से रिटर्न करें
#         return text

# # मुख्य प्रोग्राम
# if __name__ == "__main__":
#     # टेक्स्ट प्राप्त करें
#     recognized_text = recognize_speech_with_whisper()
#     print(f"Recognized Text: {recognized_text}")
