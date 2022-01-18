import os, requests, uuid, json
from urllib import response

# No Subscription key required for a local cog services container


# Our Flask route will supply two arguments: text_input and language_output.
# When the translate text button is pressed in our Flask app, the Ajax request
# will grab these values from our web app, and use them in the request.
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
#We're only detecting a single document as part of this call even though the container can do multiple.    
    detect_base_url = 'http://localhost:5001'
    path = '/text/analytics/v3.0/languages'
    constructed_url = detect_base_url + path

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
        
