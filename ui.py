from flask import Blueprint, render_template, request, jsonify
from image_processor import process_image
from game_generator import generate_game_idea

ui_blueprint = Blueprint('ui', __name__)

@ui_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        images = request.files.getlist('images')
        user_idea = request.form.get('user_idea', '')
        
        processed_images = []
        for image in images:
            if image:
                processed_images.append(process_image(image))
        
        game_idea = generate_game_idea(processed_images, user_idea)
        
        return jsonify({'game_idea': game_idea})
    
    return render_template('index.html')
