from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from test import get_moti_letter

app = Flask(__name__, template_folder="./templates/", static_folder="./static/")
CORS(app)


@app.route("/")
def home():
    return render_template("testing.html")


@app.route("/api/complete/", methods=["POST"])
def complete_query():

    def find_all_keys_recursive(dictionary):
        all_keys = set()
        for key, value in dictionary.items():
            all_keys.add(key)
            if isinstance(value, dict):
                nested_keys = find_all_keys_recursive(value)
                all_keys.update(nested_keys)
        return all_keys

    def check_request(request_dict):
        acceptable_keys = {"language", "job_url", "details", "job_title", "person_name", "person_surname", "person_age", "person_interests", "person_about"}

        all_keys = find_all_keys_recursive(request_dict)

        is_url_correct = request_dict.get("job_url", "").startswith("https://www.pracuj.pl")
        

        return True if all_keys == acceptable_keys and is_url_correct else False


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
    else:
        return jsonify({"data": f"Error:"})

if __name__ == "__main__":
    app.run(debug=True)