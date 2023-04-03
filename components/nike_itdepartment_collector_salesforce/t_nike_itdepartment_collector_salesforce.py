
import pytest
from fastapi.testclient import TestClient
from core.workflows.nike_it_department_collector_salesforce import (
    NikeITDepartmentCollectorSalesforce,
    NikeITDepartmentCollectorSalesforceIn,
    NikeITDepartmentCollectorSalesforceOut,
    SalesforceCredentials,
    Status,
)
from main import nike_it_collector_app

client = TestClient(nike_it_collector_app)

test_cases = [
    (
        NikeITDepartmentCollectorSalesforceIn(
            SalesforceCredentials={
                "client_id": "sample_client_id",
                "client_secret": "sample_client_secret",
                "username": "sample_username",
                "password": "sample_password",
                "security_token": "sample_security_token",
            },
            API_URL="sample_api_url",
        ),
        NikeITDepartmentCollectorSalesforceOut(
            Status={"success": True, "message": "API call successful"}
        ),
    ),
    (
        NikeITDepartmentCollectorSalesforceIn(
            SalesforceCredentials={
                "client_id": "",
                "client_secret": "",
                "username": "",
                "password": "",
                "security_token": "",
            },
            API_URL="sample_api_url",
        ),
        NikeITDepartmentCollectorSalesforceOut(
            Status={"success": False, "message": "API call failed, invalid credentials"}
        ),
    ),
]

@pytest.mark.parametrize("input_data, expected_output", test_cases)
def test_transform(input_data, expected_output):
    response = client.post("/transform/", json=input_data.dict())
    assert response.status_code == 200
    assert response.json() == expected_output.dict()

### Add additional test scenarios and edge cases as needed ###
