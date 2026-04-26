from urls.urls import Urls

class Endpoint:

    CREATE_USER_URL = f"{Urls.MAIN_PAGE_URL}/api/auth/register"

    USER_INFO_URL = f"{Urls.MAIN_PAGE_URL}/api/auth/user"