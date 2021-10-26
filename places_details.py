from google_api_client import GooglePlaceClient

result = GooglePlaceClient.get().place(place_id="ChIJySjGnBI1K4gR3lmQ6CdtL4c",
                                       fields=["name",
                                               "geometry/location/lat",
                                               "geometry/location/lng",
                                               "formatted_address",
                                               "icon",
                                               "icon_background_color",
                                               "icon_mask_base_uri",
                                               "type",
                                               "photo",
                                               ])

print(result)
