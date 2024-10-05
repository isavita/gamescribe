import base64
from litellm import completion

def encode_image(image_file):
    """Encode the image to base64."""
    return base64.b64encode(image_file.read()).decode('utf-8')

def process_image(image_file):
    base64_image = encode_image(image_file)
    image_system_prompt = "You are a game design bot tasked with describing screenshots from 2D games to assist in game development and design."
    image_user_prompt = """Could you describe the game design elements, features, and the genre of the 2D game depicted in this screenshot to assist in game development and design?
    Provide only the requested information, omitting any additional commentary."""
    
    response = completion(
        model="mistral/pixtral-12b-2409", 
        messages=[
            {"role": "system", "content": image_system_prompt},
            {"role": "user", "content": [
                {"type": "text", "text": image_user_prompt},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}
            ]}
        ]
    )
    return response.choices[0].message.content
