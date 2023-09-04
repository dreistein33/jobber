from api import get_moti_letter
from flask import Flask, render_template, jsonify, request, Response
from flask_cors import CORS
from validation import check_request

app = Flask(__name__, template_folder="./templates/", static_folder="./static/")
CORS(app)


@app.route("/")
def home():
    return render_template("testing.html")


@app.route("/api/complete/", methods=["POST"])
def complete_query():
    decoded_details = request.json

    print(decoded_details)

    valid_details = check_request(decoded_details)
    print(valid_details)

    if valid_details:
        url = decoded_details["job_url"]
        person_details = decoded_details["details"]
        print(decoded_details, type(decoded_details))

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


if __name__ == "__main__":
    app.run(debug=True)