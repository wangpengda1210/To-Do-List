def tallest_people(**people):
    tallest = {}
    tallest_height = 0

    for name, height in people.items():
        if height > tallest_height:
            tallest.clear()
            tallest_height = height
            tallest[name] = height
        elif height == tallest_height:
            tallest[name] = height

    for key, value in sorted(tallest.items()):
        print(f"{key} : {value}")
