# rain_alert
Python project to help the user know if it's going to rain or not on a particular day, before leaving the house.
The request model in python is used to make an API call to the One Call API 3.0 of the Openweather map API
Specific parameters are passed in order to record the hourly data for the next 48 hours.
The response in the json format is later sliced to get hold of the first 12 hours (this is assumed to be te number of hours the user will spend outside.)
The weather id which specifies the weather condition is retrieved.
Based on the weather condition, an SMS is sent to the user using the twilio API, this is to remind the user to take an umbrella before going out, if it's going to rain.
To automate the script, and make it run daily at 7:00 A.M. UTC (server time). The project was hosted on the PythonAnywhere server.
