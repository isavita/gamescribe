from litellm import completion

def generate_game_idea(game_descriptions, user_idea):
    generator_system_prompt = """You are a Game Concept Generator, specialized in crafting detailed 2D game descriptions based on user ideas and existing game references.
    Your output includes a concise game overview followed by comprehensive gameplay, visual, and mechanical details suitable for direct game development."""
    
    # Prepare the game descriptions part of the prompt
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
    5. Ensure the description is comprehensive enough for direct game development.

    Provide only the requested information, omitting any additional commentary.
    If no game examples were provided, focus solely on expanding the user's idea into a full game concept."""
    
    response = completion(
        model="mistral/mistral-large-latest",
        messages=[
            {"role": "system", "content": generator_system_prompt},
            {"role": "user", "content": generator_user_prompt}
        ]
    )
    return response.choices[0].message.content
