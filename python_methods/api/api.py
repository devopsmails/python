API = Application Programming Interface

  => Is a set of commands, functions, protocols, and Objects that 
  programmers can use to create software or interact with external system,
  
  Your Program ------------>> API(Request with proper rules) ----------->> External System
  Your program <<------------ API(Response(data))<<----------------------  External System
  
Example:
  
import requests # helps to call the api requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)

Results:
('-100.1727', '12.3296')
