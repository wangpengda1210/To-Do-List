# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
print(f"min: {min(test_dict, key=lambda x: test_dict[x])}")
print(f"max: {max(test_dict, key=lambda x: test_dict[x])}")
