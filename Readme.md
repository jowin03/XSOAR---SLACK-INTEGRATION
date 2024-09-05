# Slack User Status Fetcher - XSOAR Integration
 - This script is designed for use in Cortex XSOAR (formerly Demisto) to retrieve a user's presence status from Slack using the Slack API. It first retrieves the user's profile information, followed by their presence status.

## Table of Contents
 - Features
 - Requirements
 - Installation
 - Configuration
 - Usage
 - Error Handling

### Features
 - Retrieves Slack user profile information using the Slack API.
 - Fetches the user's presence status (active, away, etc.).
 - Outputs the result in a format compatible with Cortex XSOAR.

### Requirements
 - A valid Slack API token with access to users.info and users.getPresence methods.
 - Cortex XSOAR environment for executing the script.
 - Python dependencies:
  - requests.

### Installation
 - Clone or download the script into your XSOAR environment.
 - Make sure the script is correctly configured to run in XSOAR by importing it into your integration scripts.
 - To install requests library if needed:
  - pip install requests

### Configuration

#### Slack API Token
 - To use the Slack API, you need to provide an API token with the required permissions. This token should be set in the XSOAR integration parameters under the password field.
 - The token can be generated in Slack by creating a Slack App or using an existing one. The app must have the following scopes:
  - users:read
  - users:read.presence
 - Ensure the token is passed securely through XSOAR.

#### Script Parameters
 - user_id: The Slack User ID of the user whose presence status is to be fetched. This parameter is passed through the XSOAR context.

### Usage
 - This script can be executed in XSOAR as part of a playbook or standalone command.

#### Example Command Usage:
 - !slack-get-user-status user_id=U123456
 - This command will fetch the presence status of the user with the given user_id from Slack and return a result in XSOAR.

### Output:
 - The script will return the following information in the XSOAR War Room:
  - Online if the user is active.
  - Offline if the user is not active.
  - Error: ... in case of an error.

### Error Handling
 - If the API token is missing or incorrect, the script will return an error:

 - "Token parameter is missing or empty."
 - If the user ID is invalid, the script will return an error:
  - "Error: Invalid user_id provided."
  - API errors such as status codes other than 200 OK are handled, and the response code and error message will be displayed.

## Additional Notes:
 - This integration is a custom development and is not related to any existing Slack integration in the XSOAR marketplace.
