# Microservice_A

This microservice generates a random password based on 3 optional input parameters; length, use of numbers, and use of special characters. If no parameters are specified, the microservice returns a password with a default length of 12 characters which includes numbers and special characters. It was written for Jesus Martinez.
The microservice was developed with Flask and written in Python. 

In order to run this microservice locally, install Flask and the Python. The microservice runs at localhost, port 5000. 


Communication Contract

This microservice communicates using REST API. It accepts HTTP GET requests using a local endpoint and returns a JSON response. 



How to REQUEST data from this microservice:

With the microservice running locally, send a GET request to http://127.0.0.1:5000/generate-password, with optional query parameters. The "length" value must be an integer betweeen 6 and 100, while the "numbers" and "special" characters parameters except an integer value of either 0 or 1 (1 to include, 0 to exclude).

Example Call: 

http://127.0.0.1:5000/generate-password?length=40&numbers=1&special=0
This will request a password 40 characters long, including numbers and no special characters.



How to RECEIVE data from this microservice:

Once a GET request is sent, the microservice returns a JSON file containing the password (or error message if input is invalid).

Example Call: 

http://127.0.0.1:5000/generate-password?length=10

Reponse:
{
  "2x1pq#>r:H"
}

