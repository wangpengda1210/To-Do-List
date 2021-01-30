def select_dates(potential_dates):
    result = ""

    for potential_date in potential_dates:
        if potential_date["age"] > 30 and potential_date["city"] == "Berlin" and \
                "art" in potential_date["hobbies"]:
            result += potential_date["name"] + ", "

    return result[0:-2]
