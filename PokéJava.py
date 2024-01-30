# PokeJava.py

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Function to fetch Pokémon data from the PokéAPI
def get_pokemon_data(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to fetch Pokémon image URL
def get_pokemon_image_url(pokemon_id):
    return f'https://pokeapi.co/media/sprites/pokemon/{pokemon_id}.png'

# API route to get Pokémon data by ID
@app.route('/pokemon/<int:pokemon_id>', methods=['GET'])
def get_pokemon_by_id(pokemon_id):
    pokemon_data = get_pokemon_data(pokemon_id)
    if pokemon_data:
        response = {
            'name': pokemon_data['name'],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'image_url': get_pokemon_image_url(pokemon_id)
        }
        return jsonify(response)
    else:
        return jsonify({'error': 'Pokemon not found'}), 404

# Route to render the homepage
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
