import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self) -> None:
        self.URL = "https://api.sheety.co/68fbf06139fe3354aae967c6b57d5bc3/flightDeals/prices/"

        pass

    def put_row(self, city):
        put_res = requests.put(self.URL+str(city["id"]), json={
            "price": {
                "city": city["city"],
                "iataCode": city["iataCode"],
                "lowestPrice": city["lowestPrice"]
            },
        }, headers={
            "Authorization": "Basic ZGlhZ29uYWxsZXk6ZWV3cnF5dXRpd3J0eQ=="
        })
        # print(put_res.json())

    def get_email_list(self):
        URL = "https://api.sheety.co/68fbf06139fe3354aae967c6b57d5bc3/flightDeals/users"
        auth = {
            "Authorization": "Basic ZGlhZ29uYWxsZXk6ZWV3cnF5dXRpd3J0eQ=="
        }

        email_res = requests.get(URL, headers=auth)
        email_res.raise_for_status()
        return [user["email"] for user in email_res.json()["users"]]


{'users': [{'firstName': 'Tom', 'lastName': 'Larraine', 'email': 'tom@gmail.com', 'id': 2},
           {'firstName': 'tom', 'lastName': 'lao', 'email': 'tomlao@gmail.com', 'id': 3}]}
