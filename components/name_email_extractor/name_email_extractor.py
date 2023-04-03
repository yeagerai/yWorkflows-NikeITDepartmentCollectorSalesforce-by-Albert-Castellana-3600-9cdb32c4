
from typing import Any, Dict, List
from pydantic import BaseModel
from fastapi import FastAPI

from core.abstract_component import AbstractComponent

class NameEmailExtractorInputDict(BaseModel):
    data: List[Dict[str, str]]

class NameEmailExtractorOutputDict(BaseModel):
    extracted_data: List[Dict[str, str]]

class NameEmailExtractor(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(
        self, args: NameEmailExtractorInputDict
    ) -> NameEmailExtractorOutputDict:
        results = []
        for item in args.data:
            name = item.get("name")
            email = item.get("email")
            if name and email:
                result = {"name": name, "email": email}
                results.append(result)
        return NameEmailExtractorOutputDict(extracted_data=results)

name_email_extractor_app = FastAPI()

@name_email_extractor_app.post("/transform/")
async def transform(
    args: NameEmailExtractorInputDict,
) -> NameEmailExtractorOutputDict:
    name_email_extractor = NameEmailExtractor()
    return name_email_extractor.transform(args)
