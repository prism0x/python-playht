from json import load
import os
import requests
from dotenv import load_dotenv
import json
import hashlib
import traceback
import time

load_dotenv()

playht_userid = os.environ["PLAYHT_USER_ID"]
playht_secret = os.environ["PLAYHT_SECRET"]
playht_appid = os.environ["PLAYHT_APP_ID"]

CONVERT_ENDPOINT = "https://play.ht/api/v1/convert"
CHECK_ENDPOINT = "https://play.ht/api/v1/articleStatus?transcriptionId="

DOWNLOAD_DIR = "tts-out"
# ENDPOINT = "https://play.ht/api/transcripe"

# print(playht_userid, playht_secret)


def tts(
    content,
    voice="en-US-AriaNeural",
    narration_style="newscast-casual",
    speed=115,  # value between 20 - 200
    # narration_style="customerservice"
):
    data = {
        "voice": voice,
        "content": [content],
        "appId": playht_appid,
        "narrationStyle": narration_style,
        "globalSpeed": "%d%%" % (speed),  # // Optional
        #   "ssml": string[],
        #   "title": string,          // Optional
        #   "pronunciations": { key: string, value: string }[], // Optional
        #   "trimSilence": boolean,   // Optional
    }

    dumped_data = json.dumps(data)
    data_hash = hashlib.sha256(dumped_data.encode("utf-8")).hexdigest()
    fname = data_hash + ".mp3"
    fpath = DOWNLOAD_DIR + "/" + fname

    if not os.path.exists(DOWNLOAD_DIR):
        os.mkdir(DOWNLOAD_DIR)

    if os.path.exists(fpath):
        return fpath

    headers = {
        "Authorization": playht_secret,
        "X-User-ID": playht_userid,
        "Content-Type": "application/json",
    }
    try:
        print("Transcribing:", content)
        response = requests.post(CONVERT_ENDPOINT, data=dumped_data, headers=headers)
        transcriptionId = response.json()["transcriptionId"]

        # Wait until transcription is generated
        time.sleep(5)

        # Get the transcription URL
        response2 = requests.get(CHECK_ENDPOINT + transcriptionId, headers=headers)
        audio_url = response2.json()["audioUrl"]

        # Download and save the mp3
        response3 = requests.get(audio_url, allow_redirects=True)
        open(fpath, "wb").write(response3.content)
        return fpath
    except:
        traceback.print_stack()
        raise Exception("There was an issue transcribing")
