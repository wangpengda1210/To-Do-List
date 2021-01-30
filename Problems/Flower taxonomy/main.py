iris = {}


def add_iris(id_n, species, petal_length, petal_width, **additional_features):
    new_iris = {"species": species, "petal_length": petal_length, "petal_width": petal_width}
    for key, value in additional_features.items():
        new_iris[key] = value
    iris[id_n] = new_iris
