import requests
from urls.api_endpoints import Endpoint
class User:

    @staticmethod
    def create_user(payload):
        return requests.post(f"{Endpoint.CREATE_USER_URL}", json=payload)

    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        return requests.delete(Endpoint.USER_INFO_URL, headers=headers)