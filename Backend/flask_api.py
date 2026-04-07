from flask import Flask
import achievement_randomizer
import achievement_file_manager
import jsonpickle

app = Flask(__name__)

@app.route('/achievement_data/<achievement_id>')
def get_achievement(achievement_id):
    data = achievement_file_manager.read_simple_achievement_data_from_file()
    if achievement_id not in data:
        return "Achievement not found", 404
    return jsonpickle.encode(data[achievement_id])