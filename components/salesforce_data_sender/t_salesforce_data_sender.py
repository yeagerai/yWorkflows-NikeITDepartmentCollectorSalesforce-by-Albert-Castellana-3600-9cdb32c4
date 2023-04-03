
import os
import yaml
import pytest
from typing import List, Dict, Optional
from core.abstract_component import AbstractComponent
from your_module import (  # Replace "your_module" with the actual module containing your SalesforceDataSender component
    SalesforceDataSender,
    SalesforceDataSenderInputDict,
    SalesforceDataSenderOutputDict,
)

# Define test cases with mocked input and expected output data
test_data = [
    (
        SalesforceDataSenderInputDict(
            name_and_email_list=[
                {"name": "John Doe", "email": "john@example.com"},
                {"name": "Jane Smith", "email": "jane@example.com"},
            ]
        ),
        SalesforceDataSenderOutputDict(status_message="Data sending to Salesforce was successful."),
    ),
    (
        SalesforceDataSenderInputDict(
            name_and_email_list=[]
        ),
        SalesforceDataSenderOutputDict(status_message="Data sending to Salesforce was successful."),
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_data,expected_output", test_data)
def test_salesforce_data_sender(input_data: SalesforceDataSenderInputDict, expected_output: SalesforceDataSenderOutputDict):
    # Set up the mocked SalesforceDataSender
    class MockedSalesforceDataSender(SalesforceDataSender):
        def __init__(self) -> None:
            super().__init__()
            self.salesforce_credentials = "mocked_credentials.yml"
        
        def load_credentials(self) -> Dict[str, str]:
            return {
                "username": "mock_username",
                "password": "mock_password",
                "security_token": "mock_security_token",
            }

    # Instance of the mocked component
    salesforce_data_sender = MockedSalesforceDataSender()

    # Call the transform() method with the mocked input
    output = salesforce_data_sender.transform(input_data)

    # Assert that the output matches the expected output
    assert output == expected_output

# Include error handling and edge case scenarios
def test_salesforce_data_sender_exception_handling(mocker):
    mocker.patch("your_module.Salesforce", side_effect=Exception("Mocked exception"))

    input_data = SalesforceDataSenderInputDict(
        name_and_email_list=[
            {"name": "John Doe", "email": "john@example.com"},
            {"name": "Jane Smith", "email": "jane@example.com"},
        ]
    )
    expected_output = SalesforceDataSenderOutputDict(
        status_message="Data sending to Salesforce failed: Mocked exception"
    )

    salesforce_data_sender = SalesforceDataSender()
    output = salesforce_data_sender.transform(input_data)

    assert output == expected_output
