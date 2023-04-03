
import os
import yaml
from typing import List, Dict, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from simple_salesforce import Salesforce

from core.abstract_component import AbstractComponent


class SalesforceDataSenderInputDict(BaseModel):
    name_and_email_list: List[Dict[str, str]]


class SalesforceDataSenderOutputDict(BaseModel):
    status_message: str


class SalesforceDataSender(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.salesforce_credentials: Optional[str] = os.environ.get(
            yaml_data["parameters"]["salesforce_credentials"]
        )

    def transform(
        self, args: SalesforceDataSenderInputDict
    ) -> SalesforceDataSenderOutputDict:
        with open(self.salesforce_credentials, "r", encoding="utf-8") as file:
            credentials_data = yaml.safe_load(file)
        
        sf = Salesforce(
            username=credentials_data["username"],
            password=credentials_data["password"],
            security_token=credentials_data["security_token"]
        )

        try:
            for entry in args.name_and_email_list:
                # Replace "ObjectName" with the actual name of the Salesforce object where the data should be sent
                sf.ObjectName.create({"Name": entry["name"], "Email": entry["email"]})
            status_message = "Data sending to Salesforce was successful."
        except Exception as e:
            status_message = f"Data sending to Salesforce failed: {str(e)}"

        return SalesforceDataSenderOutputDict(status_message=status_message)


load_dotenv()
salesforce_data_sender_app = FastAPI()

@salesforce_data_sender_app.post("/transform/")
async def transform(
    args: SalesforceDataSenderInputDict,
) -> SalesforceDataSenderOutputDict:
    salesforce_data_sender = SalesforceDataSender()
    return salesforce_data_sender.transform(args)
