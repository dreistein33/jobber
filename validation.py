# Define functions need to check either the request data, database and form data

from .database.models import User


def find_all_keys_recursive(dictionary: dict) -> set:
    """Flatten dict from request to get all the keys."""
    all_keys = set()
    for key, value in dictionary.items():
        all_keys.add(key)
        if isinstance(value, dict):
            nested_keys = find_all_keys_recursive(value)
            all_keys.update(nested_keys)
    return all_keys


def check_request(request_dict: dict) -> bool:
    acceptable_keys = {"language", "job_url", "details", "job_title", "person_name", "person_surname", "person_age", "person_interests", "person_about"}

    all_keys = find_all_keys_recursive(request_dict)

    # Accept only one site with work offers for now
    is_url_correct = request_dict.get("job_url", "").startswith("https://www.pracuj.pl")
    
    # Compare expected keys to keys that has been sent by user
    return True if all_keys == acceptable_keys and is_url_correct else False


def is_user_in_db(email: str, name: str) -> bool:
    email_exists = User.query.filter_by(email=email).first()
    print(email_exists)
    name_exists = User.query.filter_by(name=name).first()

    if email_exists or name_exists:
        return True

    return False
