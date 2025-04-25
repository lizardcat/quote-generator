import requests
import base64
from io import BytesIO

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
HEADERS = {
    "Authorization": f"Bearer YOUR_HUGGINGFACE_TOKEN"
}

def generate_image(prompt: str) -> str:
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    if response.status_code == 200:
        image_bytes = response.content
        filename = f"static/ai_images/{prompt[:50].replace(' ', '_')}.png"
        with open(filename, "wb") as f:
            f.write(image_bytes)
        return filename
    else:
        print("Error:", response.text)
        return None
