


import requests
import json
import wave
import os
import subprocess

def text_to_speech_batch(text_list, api_key, voice_id, output_prefix=""):
    CHUNK_SIZE = 1024
    XI_API_KEY = api_key
    VOICE_ID = voice_id

    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    
    headers = {
        "Accept": "application/json",
        "xi-api-key": XI_API_KEY
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
                "Welcome to DataTalk for Legal, an advanced knowledge management tool designed specifically for legal professionals. Let's explore how it can streamline your contract drafting process.",
                "To begin, we'll search for clauses related to confidentiality. Notice how the search bar is prominently placed for easy access.",
                "We're typing 'classified' into the search field. DataTalk uses AI-powered semantic search to find relevant clauses, even if they don't contain this exact word.",
                "Initiating the search. DataTalk's AI engine is now scanning your entire document collection for relevant clauses.",
                "Here are the search results. Notice how DataTalk has found clauses that are semantically related to 'classified', demonstrating its understanding of legal context.",
                "We're selecting the first relevant clause. DataTalk allows you to choose multiple clauses to combine or compare.",
                "Now, we're selecting a second relevant clause. This feature is particularly useful when drafting comprehensive confidentiality agreements.",
                "By clicking 'Combine Selected Clauses', DataTalk will merge these clauses intelligently, maintaining coherence and legal accuracy.",
                "Let's review the combined clause. Notice how DataTalk has seamlessly integrated the key elements from both selected clauses.",
                "Now, we can provide feedback or request modifications to the combined clause. This demonstrates DataTalk's ability to refine clauses based on specific requirements.",
                "We're requesting a specific duration for the confidentiality obligation. This showcases DataTalk's flexibility in clause customization.",
                "Submitting the feedback. DataTalk's AI will now process this request and modify the clause accordingly.",
                "Here's the AI-generated clause with the requested modifications. Notice how it intelligently incorporated the duration while maintaining the original intent.",
                "Let's start a new search to demonstrate DataTalk's versatility. We're clearing the previous search terms.",
                "Now, we're preparing to search for payment-related clauses. This illustrates how DataTalk can assist with various aspects of contract drafting.",
                "We're searching for 'remuneration'. Again, DataTalk will use its semantic understanding to find relevant payment clauses.",
                "Initiating the search for payment-related clauses. DataTalk is now scanning your document collection.",
                "Here are the results for payment-related clauses. Notice the variety of relevant clauses DataTalk has identified.",
                "DataTalk also allows you to view the full document containing a specific clause. This feature helps you understand the broader context of each clause.",
                "We're now examining the full document. This feature is crucial for ensuring that selected clauses align with the overall contract structure and intent.",
                "This concludes our demonstration of DataTalk for Legal. As you've seen, it significantly streamlines the contract drafting process, allowing you to leverage your existing document collection efficiently and intelligently."
            ]

file_lengths = text_to_speech_batch(text_list, api_key, voice_id_english)
print("File lengths:")
for file, length in file_lengths.items():
    print(f"{file}: {length} seconds")
