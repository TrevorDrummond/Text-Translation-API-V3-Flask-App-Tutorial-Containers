import os, requests, uuid, json
from urllib import response

#UPDATE THESE VALUES TO THE CORRECT CONTAINER URLs
translate_base_url = 'http://localhost:5002'
detect_base_url = 'http://localhost:5001'

# No Subscription key required for a local cog services container

# Our Flask route will supply three arguments: text_input, language_output and language_input.
# When the translate text button is pressed in our Flask app, 2 Ajax calls are made. 
# First to get_detectlanguage to determine the language_input, then to get_translation.
# The Ajax request will grab these values from our web app, and use them in the request.
# See main.js for Ajax calls.
def get_translation(text_input, language_output, language_input):
    translate_base_url = 'http://localhost:5002'
    path = '/translate?api-version=3.0'
    params = '&from=' + language_input + '&to=' + language_output
    constructed_url = translate_base_url + path + params

    headers = {
        #'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text' : text_input
    }]
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()

def get_detectlanguage(text_input):    
    path = '/text/analytics/v3.0/languages'
    constructed_url = detect_base_url + path
#We're only detecting a single document as part of this call even though the service can do multiple.
    headers = {'Content-Type' : 'application/json'}
    body = { 'documents' : [{
        'id' : '1',
        'text' : text_input
    }]}

    response = requests.post(constructed_url, headers=headers, json=body)
    if response.status_code == 200:
        responseObject = json.loads(response.text)
        #Return the first detected result
        return responseObject['documents'][0]
        
