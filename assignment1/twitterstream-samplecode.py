# pulled from https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Sampled-Stream/sampled-stream.py
# twitter-stream also seems easy to use: https://github.com/twitivity/twitter-stream.py/tree/master/examples

import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
bearer_token = os.getenv('PROJECT_BEARER_TOKEN')

def create_url():
    return "https://api.twitter.com/2/tweets/sample/stream?tweet.fields=lang"


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2SampledStreamPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    #print(response.status_code)
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            tweet = json_response['data']['text'].replace("\n", "")
            if json_response['data']['lang'] == 'en': 
                #print(json.dumps(json_response, indent=4, sort_keys=True))
                print(tweet)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )


def main():
    url = create_url()
    timeout = 0
    while True:
        connect_to_endpoint(url)
        timeout += 1


if __name__ == "__main__":
    main()