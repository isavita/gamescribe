import logging
from flask import Blueprint, render_template, request, jsonify
from image_processor import process_image
from game_generator import generate_game_idea, generate_playable_game

logger = logging.getLogger(__name__)

ui_blueprint = Blueprint('ui', __name__)

@ui_blueprint.route('/', methods=['GET', 'POST'])
def index():
    logger.debug("Received request to index")
    if request.method == 'POST':
        logger.debug("Received POST request")
        images = request.files.getlist('images')
        user_idea = request.form.get('user_idea', '')
        
        processed_images = []
        for image in images:
            if image:
                logger.debug(f"Processing image: {image.filename}")
                processed_images.append(process_image(image))
        
        logger.debug("Generating game idea")
        game_idea = generate_game_idea(processed_images, user_idea)
        logger.debug(f"==========GAME IDEA==========:\n{game_idea}\n================================")
        
        logger.debug("Sending response")
        return jsonify({'game_idea': game_idea})
    
    logger.debug("Rendering index page")
    return render_template('index.html')

@ui_blueprint.route('/generate_game', methods=['POST'])
def generate_game():
    logger.debug("Received request to generate playable game")
    game_description = request.json.get('game_description', '')
    game_code = generate_playable_game(game_description)
    logger.debug("Generated playable game code")
    return jsonify({'game_code': game_code})
