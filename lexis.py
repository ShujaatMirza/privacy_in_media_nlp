import requests


# L/N API helper functions provided by the database service 

def get_token(client_id, secret):
    """Gets Authorizaton token to use in other requests."""
    auth_url = 'https://auth-api.lexisnexis.com/oauth/v2/token' 
    payload = ('grant_type=client_credentials&scope=http%3a%2f%2f'
                'oauth.lexisnexis.com%2fall')
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(
            auth_url,
            auth=HTTPBasicAuth(client_id, secret),
            headers=headers,
            data=payload)
    json_data = r.json()
    print("Token retrieved successfully.")
    return json_data['access_token']


def build_url(content='News', query='', skip=0, expand='Document', top=50, filter=None):
    """Builds the URL part of the request to Web Services API."""
    if filter != None:
        api_url = ('https://services-api.lexisnexis.com/v1/' + content +
                    '?$expand=' + expand + '&$search=' + query +
                    '&$skip=' + str(skip) + '&$top=' + str(top) +
                    '&$filter=' + filter)
    else:
        api_url = ('https://services-api.lexisnexis.com/v1/' + content +
                    '?$expand=' + expand + '&$search=' + query +
                    '&$skip=' + str(skip) + '&$top=' + str(top))
    return api_url



def build_header(token):
    """Builds the headers part of the request to Web Services API."""
    headers = {'Accept': 'application/json;odata.metadata=minimal',
                'Connection': 'Keep-Alive',
                'Host': 'services-api.lexisnexis.com'}
    headers['Authorization'] = 'Bearer ' + token
    return headers


def get_result_count(json_data):
    """Gets the number of results from @odata.count in the response"""
    return json_data['@odata.count']


def time_now():
    """Gets current time to the second."""
    now = datetime.now()
    return now.strftime('%Y-%m-%d-%H%M%S')