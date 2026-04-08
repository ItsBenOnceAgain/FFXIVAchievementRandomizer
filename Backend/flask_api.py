from flask import Flask, request
import achievement_randomizer
import achievement_file_manager
import achievement_data_structs
import jsonpickle
import random

app = Flask(__name__)

@app.route('/achievement_data/<achievement_id>', methods=['GET'])
def get_achievement(achievement_id):
    data = achievement_file_manager.read_simple_achievement_data_from_file()
    if achievement_id not in data:
        return "Achievement not found", 404
    return jsonpickle.encode(data[achievement_id])

@app.route('/achievement_data', methods=['GET'])
def get_all_achievements():
    data = achievement_file_manager.read_simple_achievement_data_from_file()
    return jsonpickle.encode(data)

@app.route('/filtered_achievement_data', methods=['GET'])
def get_filtered_achievements():
    try:
        data = achievement_file_manager.read_simple_achievement_data_from_file()
        filter = achievement_data_structs.FilterSettings()
        filter.allow_empty_achievements = request.args.get("allow_empty_achievements", "false").lower() == "true"
        filter.allow_legacy_achievements = request.args.get("allow_legacy_achievements", "false").lower() == "true"
        filter.allow_seasonal_achievements = request.args.get("allow_seasonal_achievements", "false").lower() == "true"
        filter.blacklisted_achievement_ids = request.args.get("blacklisted_achievement_ids", "").split(",") if request.args.get("blacklisted_achievement_ids", "") else [] 

        data = achievement_randomizer.filter_out_bad_achievements(data, filter)
        return jsonpickle.encode(data)
    except:
        return "Invalid request body", 400

@app.route('/random_achievement', methods=['GET'])
def get_random_achievement():
    try:
        data = achievement_file_manager.read_simple_achievement_data_from_file()
        filter = achievement_data_structs.FilterSettings()
        filter.allow_empty_achievements = request.args.get("allow_empty_achievements", "false").lower() == "true"
        filter.allow_legacy_achievements = request.args.get("allow_legacy_achievements", "false").lower() == "true"
        filter.allow_seasonal_achievements = request.args.get("allow_seasonal_achievements", "false").lower() == "true"
        filter.blacklisted_achievement_ids = request.args.get("blacklisted_achievement_ids", "").split(",") if request.args.get("blacklisted_achievement_ids", "") else [] 

        data = achievement_randomizer.filter_out_bad_achievements(data, filter)

        random_key = list(data.keys())[random.randint(0, len(data) - 1)]
        random_achievement = data[random_key]

        return jsonpickle.encode(random_achievement)
    except:
        return "Invalid request body", 400
    