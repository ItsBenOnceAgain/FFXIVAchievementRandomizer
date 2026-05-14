from flask import Flask, request
import flask
import achievement_randomizer
import achievement_file_manager
import achievement_data_structs
from pydantic import TypeAdapter
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
        adapter = TypeAdapter(dict[str, achievement_data_structs.Achievement])
        response = flask.Response(adapter.dump_json(data[achievement_id], indent=4).decode())
    response.headers['Access-Control-Allow-Origin'] = frontend_url
    return response

@app.route('/achievement_data', methods=['GET'])
def get_all_achievements():
    data = achievement_file_manager.read_simple_achievement_data_from_file()
    adapter = TypeAdapter(dict[str, achievement_data_structs.Achievement])
    respone = flask.Response(adapter.dump_json(data, indent=4).decode())
    respone.headers['Access-Control-Allow-Origin'] = frontend_url
    return respone

@app.route('/filtered_achievement_data', methods=['GET'])
def get_filtered_achievements():
    try:
        data = get_filtered_achievement_from_request(request)
    except achievement_data_structs.CategoryFormatException as e:
        return e.args[0], 400

    adapter = TypeAdapter(dict[str, achievement_data_structs.Achievement])
    response = flask.Response(adapter.dump_json(data, indent=4).decode())
    response.headers['Access-Control-Allow-Origin'] = frontend_url
    return response

@app.route('/random_achievement', methods=['GET'])
def get_random_achievement():
    try:
        data = get_filtered_achievement_from_request(request)
    except achievement_data_structs.CategoryFormatException as e:
        return e.args[0], 400

    random_achievement = {}

    if len(data) > 0:
        random_key = list(data.keys())[random.randint(0, len(data) - 1)]
        random_achievement = data[random_key]
    
    adapter = TypeAdapter(dict[str, achievement_data_structs.Achievement])
    response = flask.Response(adapter.dump_json(random_achievement, indent=4).decode())
    response.headers['Access-Control-Allow-Origin'] = frontend_url
    return response
    
def get_filtered_achievement_from_request(request):
    data = achievement_file_manager.read_simple_achievement_data_from_file()
    filter = achievement_data_structs.FilterSettings()
    filter.allow_empty_achievements = request.args.get("allow_empty_achievements", "false").lower() == "true"
    allowed_category_strings = request.args.get("allowed_categories", "2,3,4,5,6,7,8,9").split(",")
    filter.allowed_categories = []
    try:
        filter.allowed_categories = [int(category) for category in allowed_category_strings]
    except:
        raise achievement_data_structs.CategoryFormatException("Category not in the correct format; must be a whole number.")

    filter.blacklisted_achievement_ids = [x for x in request.args.get("blacklisted_achievement_ids", "").split(",") if x]

    data = achievement_randomizer.filter_out_bad_achievements(data, filter)
    return data