from flask import Flask, request
import flask
import achievement_data_structs
import random
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)
frontend_url = 'http://localhost:5173'
mongo_connection_string = 'mongodb://localhost:27017/'
mongo_database_name = 'ffxiv-achievement-rando'
mongo_collection_name = 'achievements'

@app.route('/achievement_data/<achievement_id>', methods=['GET'])
def get_achievement(achievement_id):
    data = query_db_by_id(int(achievement_id))
    response = flask.Response()
    if not data:
        response = construct_response("Achievement not found", status_code=404)
    else:
        response = construct_response(data)
    return response

@app.route('/achievement_data', methods=['GET'])
def get_all_achievements():
    data = get_filtered_achievement_from_request(request)
    return construct_response(data)

@app.route('/random_achievement', methods=['GET'])
def get_random_achievement():
    data = get_filtered_achievement_from_request(request)

    random_achievement = {}
    response = flask.Response()
    if len(data) > 0:
        random_achievement = data[random.randint(0, len(data) - 1)]
        response = construct_response(random_achievement)
    else:
        response = construct_response("No achievements found with the given filters", status_code=404)
    
    return response

def query_db(filter: achievement_data_structs.FilterSettings):
    data = []
    try:
        uri = mongo_connection_string
        client = MongoClient(uri)

        database = client[mongo_database_name]
        collection = database[mongo_collection_name]

        query = {}
        if not filter.allow_empty_achievements:
            query["name"] = {"$nin": ["None", ""]}
        
        if filter.allowed_categories:
            query["category"] = {"$in": filter.allowed_categories}
        
        if filter.blacklisted_achievement_ids:
            query["id"] = {"$nin": filter.blacklisted_achievement_ids}
        
        data = list(collection.find(query))

        client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
    return data

def query_db_by_id(achievement_id: int):
    data = {}
    try:
        uri = mongo_connection_string
        client = MongoClient(uri)

        database = client[mongo_database_name]
        collection = database[mongo_collection_name]

        data = collection.find_one({"id": achievement_id})

        client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
    return data

def construct_response(response_data, status_code=200):
    response = flask.Response(json_util.dumps(response_data), status_code)
    response.headers['Access-Control-Allow-Origin'] = frontend_url
    return response

def get_filtered_achievement_from_request(request):
    filter = achievement_data_structs.FilterSettings()
    filter.allow_empty_achievements = request.args.get("allow_empty_achievements", "false").lower() == "true"
    filter.allowed_categories = [x for x in request.args.get("allowed_categories", "").split(",") if x]
    filter.blacklisted_achievement_ids = [x for x in request.args.get("blacklisted_achievement_ids", "").split(",") if x]

    data = query_db(filter)
    return data