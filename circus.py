import urequests
import ujson

class Circus:
    def __init__(self, API_KEY: str, POSITION: tuple = (0.0, 0.0, 0.0)):
        self.__API_KEY = API_KEY
        self.__POSITION = POSITION
        
    def post_value(self, public_key: str, value) -> str:
        COT_API_URL = "https://circusofthings.com/WriteValue"
        lat, lon, alt = self.__POSITION
        request_url = f"{COT_API_URL}?Key={public_key}&Token={self.__API_KEY}&Value={value}&Lat={lat}&Lon={lon}&Alt={alt}"
        response = urequests.get(request_url)
        result = response.text
        response.close()
        return ujson.loads(result)

    def get_value(self, public_key: str) -> str:
        COT_API_URL = "https://circusofthings.com/ReadValue"
        request_url = f"{COT_API_URL}?Key={public_key}&Token={self.__API_KEY}"
        response = urequests.get(request_url)
        result = response.text
        response.close()
        return ujson.loads(result)


