import requests 

def test_program(length=18, numbers=1, special=1):

    response = requests.get("http://127.0.0.1:5000/generate-password" + "?length=" + str(length) + "&numbers=" + str(numbers) + "&special=" + str(special))
    json_data = response.json()

    return json_data

print("Test Case 1 (length, digits, and special characters not specified)")
print("Password: " + test_program())

print("Test Case 2 (length is 10, numbers not specified, and special characters not specified)")
print("Password: " + test_program(length=10))

print("Test Case 3 (length is 10, numbers not included, and special characters not specified)")
print("Password: " + test_program(length=10, numbers=0))

print("Test Case 4 (length is 10, numbers not included, and special characters not included)")
print("Password: " + test_program(length=10, numbers=0, special=0))

print("Test Case 5 (length not specified, numbers not included, and special characters not included)")
print("Password: " + test_program(numbers=0, special=0))

print("Test Case 6 (length not specified, numbers not specified, and special characters not included)")
print("Password: " + test_program(special=0))

print("Test Case 6 (length out of range)")
print(test_program(length=4))

print("Test Case 7 (numbers value out of range)")
print(test_program(numbers=2))