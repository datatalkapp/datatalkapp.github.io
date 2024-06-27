


import requests
import json
import wave
import os
import subprocess

api_key = 

def text_to_speech_batch(text_list, api_key, voice_id, output_prefix="nl_"):
    CHUNK_SIZE = 1024
    XI_API_KEY = api_key
    VOICE_ID = voice_id

    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    
    headers = {
        "Accept": "application/json",
        "xi-api-key": 
    }
    
    file_lengths = {}

    for index, text in enumerate(text_list, start=0):
        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8,
                "style": 0.0,
                "use_speaker_boost": True
            }
        }
        
        response = requests.post(tts_url, headers=headers, json=data, stream=True)
        
        if response.ok:
            mp3_path = f"{output_prefix}{index}.mp3"
            wav_path = f"{output_prefix}{index}.wav"
            
            # Save MP3 file
            with open(mp3_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    f.write(chunk)
            print(f"Audio stream saved successfully as {mp3_path}")
            
            
        else:
            print(f"Error processing text {index}: {response.text}")

    return file_lengths

# Example usage
api_key = ""
voice_id_english = "N9pRiILmOUmfE5t0Xv9D"
voice_id_flemish = "s7Z6uboUuE4Nd8Q2nye6"

text_list = [
    "Welkom bij DataTalk voor Juridische Professionals, een geavanceerd kennisbeheersysteem speciaal ontworpen voor juristen. Laten we eens kijken hoe het uw contractopstelling kan vereenvoudigen.",
    "We beginnen met het zoeken naar clausules over vertrouwelijkheid. Let op hoe de zoekbalk prominent aanwezig is voor gemakkelijke toegang.",
    "We typen 'vertrouwelijk' in het zoekveld. DataTalk gebruikt AI-gestuurde semantische zoektechnologie om relevante clausules te vinden, zelfs als ze dit exacte woord niet bevatten.",
    "De zoekopdracht wordt gestart. De AI-motor van DataTalk doorzoekt nu uw volledige documentenverzameling op relevante clausules.",
    "Hier zijn de zoekresultaten. Merk op hoe DataTalk clausules heeft gevonden die semantisch gerelateerd zijn aan 'vertrouwelijk', wat zijn begrip van de juridische context aantoont.",
    "We selecteren de eerste relevante clausule. Met DataTalk kunt u meerdere clausules kiezen om te combineren of te vergelijken.",
    "Nu selecteren we een tweede relevante clausule. Deze functie is vooral handig bij het opstellen van uitgebreide geheimhoudingsovereenkomsten.",
    "Door op 'Geselecteerde clausules combineren' te klikken, voegt DataTalk deze clausules intelligent samen, met behoud van samenhang en juridische nauwkeurigheid.",
    "Laten we de gecombineerde clausule bekijken. Merk op hoe DataTalk de belangrijkste elementen uit beide geselecteerde clausules naadloos heeft geïntegreerd.",
    "Nu kunnen we feedback geven of wijzigingen aanvragen voor de gecombineerde clausule. Dit toont aan hoe DataTalk clausules kan verfijnen op basis van specifieke eisen.",
    "We vragen om een specifieke duur voor de geheimhoudingsplicht. Dit laat de flexibiliteit van DataTalk zien bij het aanpassen van clausules.",
    "De feedback wordt ingediend. De AI van DataTalk zal dit verzoek nu verwerken en de clausule dienovereenkomstig aanpassen.",
    "Hier is de door AI gegenereerde clausule met de gevraagde aanpassingen. Merk op hoe deze de duur intelligent heeft verwerkt met behoud van de oorspronkelijke bedoeling.",
    "Laten we een nieuwe zoekopdracht starten om de veelzijdigheid van DataTalk te demonstreren. We wissen de vorige zoektermen.",
    "Nu bereiden we ons voor om te zoeken naar betalingsgerelateerde clausules. Dit illustreert hoe DataTalk kan helpen bij verschillende aspecten van het opstellen van contracten.",
    "We zoeken op 'vergoeding'. Opnieuw zal DataTalk zijn semantisch begrip gebruiken om relevante betalingsclausules te vinden.",
    "We starten de zoekopdracht naar betalingsgerelateerde clausules. DataTalk doorzoekt nu uw documentenverzameling.",
    "Hier zijn de resultaten voor betalingsgerelateerde clausules. Merk de verscheidenheid aan relevante clausules op die DataTalk heeft gevonden.",
    "Met DataTalk kunt u ook het volledige document bekijken dat een specifieke clausule bevat. Deze functie helpt u de bredere context van elke clausule te begrijpen.",
    "We bekijken nu het volledige document. Deze functie is cruciaal om ervoor te zorgen dat geselecteerde clausules aansluiten bij de algehele contractstructuur en -intentie.",
    "Hiermee sluiten we onze demonstratie van DataTalk voor Juridische Professionals af. Zoals u heeft gezien, vereenvoudigt het aanzienlijk het proces van contractopstelling, waardoor u efficiënt en intelligent gebruik kunt maken van uw bestaande documentenverzameling."
]

file_lengths = text_to_speech_batch(text_list, api_key, voice_id_flemish)
print("File lengths:")
for file, length in file_lengths.items():
    print(f"{file}: {length} seconds")
