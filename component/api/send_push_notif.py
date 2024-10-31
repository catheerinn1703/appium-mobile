from pprint import pprint

import requests


def send_push_notif(headers, channel_id, user_id):
    url = 'https://sqemp-be.stg.squantumengine.com/'
    channel_id = channel_id
    path = f'v1/push_notification/channel/{channel_id}/send_test'
    payload = {
        "user_id": [
            user_id
        ]
    }

    response = requests.post(url=url + path, headers=headers, json=payload)
    data = response.json()
    print(response)
    pprint(data)
    assert response.status_code == 200
    return response, data
