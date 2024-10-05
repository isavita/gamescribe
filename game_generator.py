import logging
from litellm import completion
import re

logger = logging.getLogger(__name__)

MODEL_GENERATE_GAME = "mistral/mistral-large-latest"
MODEL_BUILD_GAME = "mistral/mistral-large-latest"

def generate_game_idea(game_descriptions, user_idea):
    logger.debug(f"Generating game idea based on {len(game_descriptions)} game descriptions and user idea")
    generator_system_prompt = """You are a Game Concept Generator, specialized in crafting detailed 2D game descriptions based on user ideas and existing game references."""
    
    games_prompt = ""
    if game_descriptions:
        games_prompt = "Game Examples:\n"
        for i, desc in enumerate(game_descriptions, 1):
            games_prompt += f"Game {i}:\n{desc}\n\n"
    
    logger.debug(f"==========GAMES PROMPT==========:\n{games_prompt}\n================================")
    generator_user_prompt = f"""Synthesize a new 2D game concept by combining elements from the following inputs:

    {games_prompt}
    User Idea:
    {user_idea}

    Create a detailed game description including:
    1. Concise overview
    2. Gameplay mechanics
    3. Visual style
    4. Unique features
    5. Ensure the description is comprehensive enough for direct game development."""
    logger.debug(f"==========GENERATOR USER PROMPT==========:\n{generator_user_prompt}\n================================")
    logger.debug("Sending prompt to AI for game idea generation")
    response = completion(
        model=MODEL_GENERATE_GAME,
        messages=[
            {"role": "system", "content": generator_system_prompt},
            {"role": "user", "content": generator_user_prompt}
        ]
    )
    logger.debug("Received response from AI")
    response_content = response.choices[0].message.content
    logger.debug(f"==========GAME IDEA RESPONSE==========:\n{response_content}\n================================")
    return response_content

def generate_playable_game(game_description):
    logger.debug(f"Generating playable game based on description")
    build_game_system_prompt = (
        "You are a game development bot designed to create visually appealing 2D JavaScript games based on game descriptions. "
        "Your output should be the complete HTML and JavaScript code for a standalone web page that can be embedded in an iframe."
    )

    build_game_user_prompt = f"""
    Please create a 2D JavaScript game based on the following description:

    {game_description}

    **Requirements:**
    - The game should be fully contained in a single HTML file.
    - Include all necessary JavaScript and CSS within the HTML file (no external files).
    - Ensure the game is visually appealing with engaging graphics and design elements.
    - The game should run independently and be embeddable using an iframe.
    - Do not include any explanatory text or comments—only provide the code.
    """

    logger.debug(f"==========BUILD GAME USER PROMPT==========:\n{build_game_user_prompt}\n================================")
    logger.debug("Sending prompt to AI for playable game generation")
    response = completion(
        temperature=0.0,
        model=MODEL_BUILD_GAME,
        messages=[
            {"role": "system", "content": build_game_system_prompt},
            {"role": "user", "content": build_game_user_prompt}
        ]
    )
    logger.debug("Received response from AI")
    game_code = response.choices[0].message.content.strip()
    logger.debug(f"==========GAME CODE RESPONSE==========:\n{game_code}\n================================")
    # Process the game code to extract HTML
    code_match = re.search(r"```html(.*?)```", game_code, re.DOTALL)
    if code_match:
        game_code = code_match.group(1).strip()
    else:
        html_start = game_code.find('<html')
        if html_start == -1:
            html_start = game_code.find('<!DOCTYPE html')
        if html_start != -1:
            game_code = game_code[html_start:].strip()

    return game_code
