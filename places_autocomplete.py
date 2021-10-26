import uuid

from dataclasses import dataclass
from google_api_client import GooglePlaceClient


@dataclass
class AutoCompletePlaceResult:
    result: list = None
    session_token: str = ""


def show_auto_complete_place_results(input_text: str, session_token: str = None) -> AutoCompletePlaceResult:
    if not session_token:
        session_token = str(uuid.uuid4())

    result = GooglePlaceClient.get().places_autocomplete(input_text=input_text, session_token=session_token)
    return AutoCompletePlaceResult(result=result, session_token=session_token)


return_result = show_auto_complete_place_results(input_text="CN Tow")

print(return_result.result[0])
print("place_id")
print(return_result.result[0]["place_id"])
