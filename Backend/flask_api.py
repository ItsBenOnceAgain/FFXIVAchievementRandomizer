from flask import Flask, request
import flask
import achievement_randomizer
import achievement_file_manager
import achievement_data_structs
import jsonpickle
import random

app = Flask(__name__)
frontend_url = 'http://localhost:5173'

@app.route('/achievement_data/<achievement_id>', methods=['GET'])
def get_achievement(achievement_id):
    data = achievement_file_manager.read_simple_achievement_data_from_file()
    response = flask.Response()
    if achievement_id not in data:
        response = flask.Response("Achievement not found", status=404)
    else:
        response = flask.Response(jsonpickle.encode(data[achievement_id], unpicklable=False))
    response.headers['Access-Control-Allow-Origin'] = frontend_url
    return response

@app.route('/achievement_data', methods=['GET'])
def get_all_achievements():
    data = achievement_file_manager.read_simple_achievement_data_from_file()
    respone = flask.Response(jsonpickle.encode(data, unpicklable=False))
    respone.headers['Access-Control-Allow-Origin'] = frontend_url
    return respone

@app.route('/filtered_achievement_data', methods=['GET'])
def get_filtered_achievements():
    data = achievement_file_manager.read_simple_achievement_data_from_file()
    filter = achievement_data_structs.FilterSettings()
    filter.allow_empty_achievements = request.args.get("allow_empty_achievements", "false").lower() == "true"
    filter.allow_legacy_achievements = request.args.get("allow_legacy_achievements", "false").lower() == "true"
    filter.allow_seasonal_achievements = request.args.get("allow_seasonal_achievements", "false").lower() == "true"
    filter.blacklisted_achievement_ids = request.args.get("blacklisted_achievement_ids", "").split(",") if request.args.get("blacklisted_achievement_ids", "") else [] 

    data = achievement_randomizer.filter_out_bad_achievements(data, filter)
    response = flask.Response(jsonpickle.encode(data, unpicklable=False))
    response.headers['Access-Control-Allow-Origin'] = frontend_url
    return response

@app.route('/random_achievement', methods=['GET'])
def get_random_achievement():
    data = achievement_file_manager.read_simple_achievement_data_from_file()
    filter = achievement_data_structs.FilterSettings()
    filter.allow_empty_achievements = request.args.get("allow_empty_achievements", "false").lower() == "true"
    filter.allow_legacy_achievements = request.args.get("allow_legacy_achievements", "false").lower() == "true"
    filter.allow_seasonal_achievements = request.args.get("allow_seasonal_achievements", "false").lower() == "true"
    filter.blacklisted_achievement_ids = request.args.get("blacklisted_achievement_ids", "").split(",") if request.args.get("blacklisted_achievement_ids", "") else [] 

    data = achievement_randomizer.filter_out_bad_achievements(data, filter)

    random_key = list(data.keys())[random.randint(0, len(data) - 1)]
    random_achievement = data[random_key]
    response = flask.Response(jsonpickle.encode(random_achievement, unpicklable=False))
    response.headers['Access-Control-Allow-Origin'] = frontend_url
    return response
    