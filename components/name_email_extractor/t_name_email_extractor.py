
import pytest
from typing import List, Dict
from pydantic import BaseModel

from core.abstract_component import AbstractComponent
from .your_module import NameEmailExtractor, NameEmailExtractorInputDict, NameEmailExtractorOutputDict

# Define test cases with mocked input and expected output data
test_cases = [
    (
        NameEmailExtractorInputDict(
            data=[
                {"name": "John Doe", "email": "john.doe@example.com"},
                {"name": "Jane Doe", "email": "jane.doe@example.com"},
                {"name": "Bob Smith", "email": ""},
            ]
        ),
        NameEmailExtractorOutputDict(
            extracted_data=[
                {"name": "John Doe", "email": "john.doe@example.com"},
                {"name": "Jane Doe", "email": "jane.doe@example.com"},
            ]
        ),
    ),
    (
        NameEmailExtractorInputDict(data=[{"name": "", "email": ""}]),
        NameEmailExtractorOutputDict(extracted_data=[]),
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_data, expected_output", test_cases)
def test_name_email_extractor(input_data: NameEmailExtractorInputDict, expected_output: NameEmailExtractorOutputDict):
    # Initialize the component
    name_email_extractor = NameEmailExtractor()

    # Call the component's transform() method
    output = name_email_extractor.transform(input_data)

    # Assert that the output matches the expected output
    assert output == expected_output
