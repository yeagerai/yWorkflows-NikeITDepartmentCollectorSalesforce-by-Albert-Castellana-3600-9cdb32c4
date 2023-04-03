
# SalesforceDataSender

Receives the extracted name and email list from the NameEmailExtractor component, connects to Salesforce using the provided SalesforceCredentials, and uploads the data. Finally, returns a status message with the indication whether data sending was successful or not.

## Initial generation prompt
description: Receives the extracted name and email list, connects to Salesforce using
  the provided SalesforceCredentials, and uploads the data. Finally, returns a status
  message with the indication whether data sending was successful or not.
inputs_from: NameEmailExtractor
name: SalesforceDataSender


## Transformer breakdown
- Load salesforce_credentials from salesforce_credentials.yml
- Establish a connection to Salesforce using the provided credentials
- Iterate through the name_and_email_list and upload each entry to Salesforce
- If data sending is successful, return a status message indicating success
- If data sending fails, return a status message indicating error

## Parameters
[{'name': 'salesforce_credentials', 'default_value': 'salesforce_credentials.yml', 'description': 'Salesforce credentials config file', 'type': 'str'}]

        