
import pytest
from pydantic import ValidationError
from unittest import mock

from your_component_folder import NikeITDepartmentCollector  # Update this import statement based on your folder structure
from your_component_folder import NikeITDepartmentCollectorInputDict, NikeITDepartmentCollectorOutputDict  # Update this import statement

# You might need to update this string to the proper path of a test configuration file.
TEST_CONFIG_FILE = "your_component_folder/test_configuration.yml"

# Define test cases with mocked input and expected output data
test_cases = [
    (
        {"api_key": "test_api_key"},
        {"personas_data": [{"name": "John Doe", "email": "johndoe@example.com"}]},
        200,
        {"personas": [{"name": "John Doe", "email": "johndoe@example.com", "department": "IT"}]},
    ),
    (
        {"api_key": "test_api_key"},
        {"personas_data": []},
        200,
        {"personas": [{"name": "Jane Doe", "email": "janedoe@example.com", "department": "HR"}]},
    ),
    (
        {"api_key": "test_api_key"},
        {"personas_data": []},
        404,
        None,
    ),
]

@pytest.mark.parametrize("input_data, expected_output, response_code, response_data", test_cases)
def test_transform(input_data, expected_output, response_code, response_data):
    # Prepare mocked objects
    input_obj = NikeITDepartmentCollectorInputDict(**input_data)
    expected_output_obj = NikeITDepartmentCollectorOutputDict(**expected_output)
    mocked_response = mock.Mock()
    mocked_response.status_code = response_code
    mocked_response.json.return_value = response_data

    # Create component instance, mock its requests.get call, and set the custom configuration path
    nike_it_dept_collector = NikeITDepartmentCollector()
    nike_it_dept_collector.api_endpoint = "http://fakeapi.com/personas"  # Replace with the actual endpoint from test configuration file
    with mock.patch("your_component_folder.requests.get", return_value=mocked_response):  # Update this import statement
        # Call component's transform() method and assert output
        output_obj = nike_it_dept_collector.transform(input_obj)
        assert output_obj == expected_output_obj

def test_invalid_input():
    with pytest.raises(ValidationError):
        invalid_input = {"wrong_key": "value"}
        NikeITDepartmentCollectorInputDict(**invalid_input)

def test_invalid_output():
    with pytest.raises(ValidationError):
        invalid_output = {"wrong_key": "value"}
        NikeITDepartmentCollectorOutputDict(**invalid_output)
