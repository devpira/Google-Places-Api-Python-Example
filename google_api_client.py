import os

from dotenv import load_dotenv
import googlemaps


class GooglePlaceClient:

    @staticmethod
    def get():
        load_dotenv()

        google_api_key = os.getenv("GOOGLE_API_KEY")
        return googlemaps.Client(key=google_api_key)
