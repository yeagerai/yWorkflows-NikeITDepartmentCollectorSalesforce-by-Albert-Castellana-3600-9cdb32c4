
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow

class SalesforceCredentials(BaseModel):
    client_id: str
    client_secret: str
    username: str
    password: str
    security_token: str

class NikeITDepartmentCollectorSalesforceIn(BaseModel):
    SalesforceCredentials: SalesforceCredentials
    API_URL: str

class Status(BaseModel):
    success: bool
    message: str

class NikeITDepartmentCollectorSalesforceOut(BaseModel):
    Status: Status

class NikeITDepartmentCollectorSalesforce(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: NikeITDepartmentCollectorSalesforceIn, callbacks: typing.Any
    ) -> NikeITDepartmentCollectorSalesforceOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)

        nike_it_department_data = results_dict["NikeITDepartmentAPI"]
        salesforce_status = results_dict["SalesforceAPI"]

        status = Status(success=salesforce_status.success, message=salesforce_status.message)

        out = NikeITDepartmentCollectorSalesforceOut(Status=status)
        return out

load_dotenv()
nike_it_collector_app = FastAPI()

@nike_it_collector_app.post("/transform/")
async def transform(
    args: NikeITDepartmentCollectorSalesforceIn,
) -> NikeITDepartmentCollectorSalesforceOut:
    nike_it_collector = NikeITDepartmentCollectorSalesforce()
    return await nike_it_collector.transform(args, callbacks=None)
