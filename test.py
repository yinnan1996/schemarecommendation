import requests
import pprint

if __name__ == '__main__':
    data = {
        "_ord": [
            "Magnetic Electronic Materials Category",
            "Material Information",
        ],
        "Magnetic Electronic Materials Category": {
            "r": True,
            "t": 1,
            "misc": {}
        },
        "Material Information": {
            "r": False,
            "t": 9,
            "misc": {
                "_ord": [
                    "Chemical Formula",
                    "Crystal Structure"
                ],
                "Chemical Formula": {
                    "r": False,
                    "t": 1,
                    "misc": {}
                },
                "Crystal Structure": {
                    "r": False,
                    "t": 1,
                    "misc": {}
                }
            }
        },
    }
    resp = requests.post("http://127.0.0.1:5000/api/example", json=data)
    pprint.pprint(resp.json())