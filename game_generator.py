import logging
from litellm import completion

logger = logging.getLogger(__name__)

def generate_game_idea(game_descriptions, user_idea):
    logger.debug(f"Generating game idea based on {len(game_descriptions)} game descriptions and user idea")
    generator_system_prompt = """You are a Game Concept Generator, specialized in crafting detailed 2D game descriptions based on user ideas and existing game references."""
    
    games_prompt = ""
    if game_descriptions:
        games_prompt = "Game Examples:\n"
        for i, desc in enumerate(game_descriptions, 1):
            games_prompt += f"Game {i}:\n{desc}\n\n"
    
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
    
    logger.debug("Sending prompt to AI for game idea generation")
    response = completion(
        model="mistral/mistral-large-latest",
        messages=[
            {"role": "system", "content": generator_system_prompt},
            {"role": "user", "content": generator_user_prompt}
        ]
    )
    logger.debug("Received response from AI")
    return response.choices[0].message.content
