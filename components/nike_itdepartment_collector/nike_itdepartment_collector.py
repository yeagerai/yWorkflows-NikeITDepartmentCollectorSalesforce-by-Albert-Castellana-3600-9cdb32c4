
import os
from typing import List, Dict, Optional
import requests
import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class NikeITDepartmentCollectorInputDict(BaseModel):
    api_key: str


class NikeITDepartmentCollectorOutputDict(BaseModel):
    personas_data: List[Dict[str, str]]


class NikeITDepartmentCollector(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.api_endpoint: str = yaml_data["parameters"]["api_endpoint"]

    def transform(
        self, args: NikeITDepartmentCollectorInputDict
    ) -> NikeITDepartmentCollectorOutputDict:
        api_key = args.api_key
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(self.api_endpoint, headers=headers)

        if response.status_code == 200:
            it_personas_data = [
                {"name": persona["name"], "email": persona["email"]}
                for persona in response.json()["personas"]
                if persona["department"] == "IT"
            ]
        else:
            it_personas_data = []

        return NikeITDepartmentCollectorOutputDict(personas_data=it_personas_data)


load_dotenv()
nike_it_dept_collector_app = FastAPI()


@nike_it_dept_collector_app.post("/transform/")
async def transform(
    args: NikeITDepartmentCollectorInputDict,
) -> NikeITDepartmentCollectorOutputDict:
    nike_it_dept_collector = NikeITDepartmentCollector()
    return nike_it_dept_collector.transform(args)

