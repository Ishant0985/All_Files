import os
import requests
import json
from config import img_apikey

# Create a folder for saving generated images
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

# Extract middle two words from the prompt
def get_middle_words(prompt):
    words = prompt.split()
    if len(words) < 2:
        return "image"  # Default name for short prompts
    middle_index = len(words) // 2
    if len(words) % 2 == 0:
        return f"{words[middle_index - 1]}_{words[middle_index]}"
    return f"{words[middle_index]}_{words[middle_index]}"

# Generate image using LightX API
def generate_image(api_key, prompt):
    url = "https://stablediffusionapi.com/api/v3/text2img"

    payload = json.dumps({
    "key": img_apikey,
    "prompt": prompt,
    "negative_prompt": None,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker": "yes",
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        result = response.json()
        if "image_url" in result:
            image_url = result["image_url"]
            folder_name = "ai_images"
            create_folder(folder_name)

            # Save image with middle words as filename
            file_name = f"{get_middle_words(prompt)}.jpg"
            file_path = os.path.join(folder_name, file_name)

            # Download and save the image
            image_response = requests.get(image_url)
            with open(file_path, "wb") as file:
                file.write(image_response.content)

            print(f"Image saved as: {file_path}")
        else:
            print("Error: Image URL not found in the response.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Example Usage
api_key = "your_lightx_api_key_here"  # Replace with your actual API key
prompt = "A serene waterfall in a dense jungle"
generate_image(api_key=img_apikey, prompt=prompt)
