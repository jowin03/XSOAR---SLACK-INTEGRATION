import requests
import demisto

def get_user_presence():
    # Get the user_id argument from the XSOAR context
    user_id = demisto.args().get('user_id')

    # Get the token from integration parameters
    token_info = demisto.params().get('password')
    
    # Check and extract the token from the token_info
    if token_info:
        token = token_info['password'] if isinstance(token_info, dict) and 'password' in token_info else token_info
        demisto.debug(f"Extracted Token: {token}")
    else:
        token = None
        demisto.debug("Token Info is None")
    
    if not token:
        return_error("Token parameter is missing or empty.")
    
    # Get user info from Slack API
    url_user_info = f"https://slack.com/api/users.info?user={user_id}"
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response_user_info = requests.get(url_user_info, headers=headers)
    
    if response_user_info.status_code != 200:
        return_error(f"Error: {response_user_info.status_code}, {response_user_info.text}")

    user_info = response_user_info.json()
    if not user_info.get('ok'):
        return_error(f"Error: {user_info.get('error')}")

    user_name = user_info.get('user', {}).get('profile', {}).get('real_name', 'Unknown')

    # Get user presence from Slack API
    url_presence = f"https://slack.com/api/users.getPresence?user={user_id}"
    response_presence = requests.get(url_presence, headers=headers)
    
    if response_presence.status_code != 200:
        return_error(f"Error: {response_presence.status_code}, {response_presence.text}")

    presence_info = response_presence.json()

    if not presence_info.get('ok'):
        if presence_info.get('error') == 'user_not_found':
            return_error("Error: Invalid user_id provided.")
        return_error(f"Error: {presence_info.get('error')}")

    presence_status = presence_info.get('presence')

    # Create the output entry for XSOAR
    entry = {
        'Type': 1,  # Note
        'ContentsFormat': 'json',
        'Contents': presence_status,
        'HumanReadable': f'The presence status of user {user_name} ({user_id}) is {presence_status}.',
        'EntryContext': {
            'Slack.UserPresence(val.UserID == obj.UserID)': {
                'UserID': user_id,
                'UserName': user_name,
                'Presence': presence_status
            }
        }
    }

    demisto.results(entry)


# Execute the function when the script is called
get_user_presence()
