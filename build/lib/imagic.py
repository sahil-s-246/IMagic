import argparse
import google.generativeai as genai
from PIL import Image
from rich.console import Console
import os
import configparser

cfg = configparser.ConfigParser()
cfg.read('val.cfg')

console = Console()


def generate_insights(data):
    genai.configure(api_key=cfg["Api"]["gemini"])

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(["What is in this photo?", data])
    return response.text


def main():
    parser = argparse.ArgumentParser(description='CLI Tool for Generating Insights from File Data')
    parser.add_argument('-i', '--input_file', type=str, required=True, help='Path to the input file')

    args = parser.parse_args()

    # Read the file content
    with open(args.input_file, 'rb') as f:
        image = Image.open(f)
        insights = generate_insights(image)

        console.print(insights)


if __name__ == '__main__':
    main()
