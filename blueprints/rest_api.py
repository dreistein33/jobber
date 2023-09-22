# REST-API for generating GPT responses

from flask import Blueprint, jsonify, request, Response
from ..api import get_moti_letter
from ..validation import check_request

rest_api = Blueprint("rest_api", __name__)


@rest_api.route("/api/complete/", methods=["POST"])
def complete_query():
    decoded_details = request.json

    print(decoded_details)

    # Make sure all of the keys needed are here.
    valid_details = check_request(decoded_details)
    print(valid_details)

    if valid_details:
        url = decoded_details["job_url"]
        person_details = decoded_details["details"]
        language = person_details["language"]
        job_title = person_details["job_title"]
        person_name = person_details["person_name"]
        person_surname = person_details["person_surname"]
        person_age = person_details["person_age"]
        person_interests = person_details["person_interests"]
        person_about = person_details["person_about"]
        
        letter = get_moti_letter(language, url, job_title, person_name, person_surname, person_age, person_interests, person_about)

        return jsonify({"data": letter})

    return Response(
        "Bad Response. Invalid Data.",
        status=400
    ) 
