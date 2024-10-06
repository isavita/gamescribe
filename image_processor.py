import base64
import logging
import os
from litellm import completion

logger = logging.getLogger(__name__)

MODEL_PROCESS_IMAGE = "mistral/pixtral-12b-2409"

def process_image(image_file):
    logger.debug(f"Processing image: {image_file.filename}")
    base64_image = encode_image(image_file)
    mime_type = get_mime_type(image_file.filename)
    
    image_system_prompt = "You are a game design bot tasked with describing screenshots from 2D games to assist in game development and design."
    image_user_prompt = """Could you describe the game design elements, features, mood, main idea, and the genre of the 2D game depicted in this screenshot to assist in game development and design?
    Provide only the requested information, omitting any additional commentary."""
    
    logger.debug("Sending image to AI for analysis")
    response = completion(
        model=MODEL_PROCESS_IMAGE, 
        messages=[
            {"role": "system", "content": image_system_prompt},
            {"role": "user", "content": [
                {"type": "text", "text": image_user_prompt},
                {"type": "image_url", "image_url": f"data:{mime_type};base64,{base64_image}"}
            ]}
        ]
    )
    logger.debug("Received response from AI")
    response_content = response.choices[0].message.content
    logger.debug(f"==========IMAGE PROCESS RESPONSE==========:\n{response_content}\n================================")
    return response_content

def encode_image(image_file):
    """Encode the image to base64."""
    # logger.debug(f"Encoding image: {image_file.filename}")
    return base64.b64encode(image_file.read()).decode('utf-8')

def get_mime_type(filename):
    """Determine the MIME type based on the file extension."""
    extension = os.path.splitext(filename)[1].lower()
    if extension in ['.jpg', '.jpeg']:
        return 'image/jpeg'
    elif extension == '.png':
        return 'image/png'
    else:
        raise ValueError(f"Unsupported image format: {extension}")
