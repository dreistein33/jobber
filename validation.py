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