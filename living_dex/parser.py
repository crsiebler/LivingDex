import json


def parse_pokemon(file, pokemon):
    if pokemon["captured"] is False and pokemon["shiny"] is False:
        file.write("+%s," % pokemon["id"])


def parse_box(file, box):
    for pokemon in box["pokemon"]:
        parse_pokemon(file, pokemon)


def parse_boxes(file, boxes):
    for idx, box in enumerate(boxes):
        if idx < 61:
            parse_box(file, box)


def parse_json_data(file, data):
    parse_boxes(file, data["boxes"])


def open_files(input_file, output_file):
    with open(input_file, "r") as json_file, open(output_file, "w") as output:
        parse_json_data(output, json.load(json_file))


def parse(input_file, output_file):
    """Write list to the file as "<pokemon1>,<pokemon2>,<pokemon3>""" ""
    try:
        open_files(input_file, output_file)
    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
