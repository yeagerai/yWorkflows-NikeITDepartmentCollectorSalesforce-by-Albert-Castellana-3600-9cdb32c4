markdown
# Component Name

NikeITDepartmentCollector

# Description

The NikeITDepartmentCollector component is designed to retrieve and filter IT department-specific data from the given API. It's a Yeager Workflow component that inherits from the AbstractComponent class.

# Input and Output Models

## Input Model

### NikeITDepartmentCollectorInputDict

The input model is a Pydantic BaseModel that takes:

- `api_key`: str - An API key required to make API calls to the target API.

## Output Model

### NikeITDepartmentControllerOutputDict

The output model is a Pydantic BaseModel that returns:

- `personas_data`: List[Dict[str, str]] - A filtered list of IT department personas, each containing a name and email.

# Parameters

The only parameter used in the NikeITDepartmentCollector component is:

- `api_endpoint`: str - The target API endpoint URL, defined in the component's YAML configuration. This parameter is passed internally to the transform function within the class.

# Transform Function

The transform() function performs the following steps:

1. Extract the API key from the input argument, `args.api_key`.
2. Create an Authorization header using the API key.
3. Send a GET request to the specified `api_endpoint` using `requests.get()` and providing the headers.
4. Check if the response status code is 200:
   - If yes, filter out the IT department personas from the response and store it in `it_personas_data`.
   - If no, set an empty list to `it_personas_data`.
5. Return the output model with the filtered IT department personas data, `NikeITDepartmentCollectorOutputDict(personas_data=it_personas_data)`.

# External Dependencies

The component requires the following external libraries and dependencies:

- **requests**: To make HTTP requests to the API.
- **yaml**: To load and parse the component's YAML configuration.
- **dotenv**: To load environment variables.
- **fastapi**: To define and expose the component's APIs.
- **pydantic**: To define input and output models for data validation and serialization.

# API Calls

The component makes a single API call:

- GET request to the `api_endpoint`: This call retrieves the personas data from the API. The Authorization header includes the API key provided in the input arguments. The purpose of this API call is to fetch and filter the IT department personas.

# Error Handling

The component checks the response status code and handles it accordingly:

- If the status code is 200, it processes the response and filters the IT department personas data.
- If the status code is not 200, it sets an empty list to `it_personas_data` and continues without raising any exceptions.

# Examples

To use the NikeITDepartmentCollector component in a Yeager Workflow, you need to set up environment variables, create the input model, and call the transform function.

Example:

