import base64
import requests
import os

url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

def imageGen(prompt, picNum, secondaryPrompt):
    body = {
    "steps": 40, # change
    "width": 1024,
    "height": 1024,
    "seed": 0,
    "cfg_scale": 5, # change
    "samples": 1,
    "text_prompts": [
        {
        "text": prompt,
        "weight": 1
        },
        {
        "text": secondaryPrompt,
        "weight": 0.3
        },
        {
        "text": "blurry, bad",
        "weight": -1
        }
    ],
    }

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-yHys1bvlJURBvIKHA4NNsZNGvpX5mIa257RAiWUlZqzjOkVz",
    }

    response = requests.post(
    url,
    headers=headers,
    json=body,
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    # make sure the out directory exists
    if not os.path.exists("./out"):
        os.makedirs("./out")

    for i, image in enumerate(data["artifacts"]):
        with open(f'./out/img{picNum}.jpg', "wb") as f:
            f.write(base64.b64decode(image["base64"]))