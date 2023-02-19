from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageColor, ImageFont
import openai
import urllib.request

app = Flask(__name__)
IMAGE_GEN_OPENAI_ENDPOINT = "https://api.openai.com/v1/images/generations"
BEARER_TOKEN = "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"


@app.route("/getComicURL")
def getComicURL():
    name1 = request.headers.get("name1")
    name2 = request.headers.get("name2")
    quantity1 = request.headers.get("quantity1")
    objectName = request.headers.get("objectName")
    quantity2 = request.headers.get("quantity2")
    nameSelect1 = request.headers.get("nameSelect1")
    nameSelect2 = request.headers.get("nameSelect2")
    nameSelect3 = request.headers.get("nameSelect3")
    quantity3 = request.headers.get("quantity3")

    promptComic1 = f"{name1} is sitting at a table with {quantity1} {objectName} in front of them; comic book art; extreme long shot"
    promptComic2 = f"{name2} is sitting at a table with {quantity2} {objectName} in front of them; comic book art; extreme long shot"
    promptComic3 = f"{nameSelect1} giving {quantity3} {objectName} to {nameSelect2}; comic book art; extreme long shot"
    promptComic4 = f"{nameSelect3} sitting at an empty table; comic book art; extreme long shot"
    getComicStrip(promptComic1, promptComic2, promptComic3, promptComic4, objectName, nameSelect3)

    return jsonify({"url": "url_image"})


def getComicStrip(promptComic1: str, promptComic2: str, promptComic3: str, promptComic4: str, objectName: str,
                  nameSelect3: str) -> str:
    openai.api_key = BEARER_TOKEN
    response1 = openai.Image.create(prompt=promptComic1,
                                    n=1,
                                    size="256x256")
    response2 = openai.Image.create(prompt=promptComic2,
                                    n=1,
                                    size="256x256")
    response3 = openai.Image.create(prompt=promptComic3,
                                    n=1,
                                    size="256x256")
    response4 = openai.Image.create(prompt=promptComic4,
                                    n=1,
                                    size="256x256")

    urllib.request.urlretrieve(response1["data"][0]["url"], "image1.png")
    image1 = Image.open("image1.png")

    urllib.request.urlretrieve(response2["data"][0]["url"], "image2.png")
    image2 = Image.open("image2.png")

    urllib.request.urlretrieve(response3["data"][0]["url"], "image3.png")
    image3 = Image.open("image3.png")

    urllib.request.urlretrieve(response4["data"][0]["url"], "image4.png")
    image4 = Image.open("image4.png")

    draw = ImageDraw.Draw(image4)
    font = ImageFont.load_default()
    draw.text((35, 35), f"Draw the number of {objectName} {nameSelect3} has", fill="black", font=font)

    finalComicImage = Image.new("RGB", (1024, 256), (250, 250, 250))
    finalComicImage.paste(image1, (0, 0))
    finalComicImage.paste(image2, (256, 0))
    finalComicImage.paste(image3, (512, 0))
    finalComicImage.paste(image4, (768, 0))
    finalComicImage.save("comicStrip.png", "PNG")
    return "comicStrip.png"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
