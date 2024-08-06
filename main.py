import json
from PIL import Image, ImageFont, ImageDraw

magic_number = 30


def imgexp(name: str, font_size, line_spacing):
    my_image = Image.open("cert.png")
    title_font = ImageFont.truetype("./font/GoogleSans.ttf", font_size)
    image_editable = ImageDraw.Draw(my_image)

    contents = name.split(" ")

    length = len(name) // 2
    length *= magic_number
    # Position the text
    name_position = (
        950 - length,
        550,
    )  # found this value by trial and error plz dont change
    # position_position = (290, 957)
    # description_position = (355, 1350)

    # Format the text
    tempname = name
    name = [text.capitalize() for text in contents]
    name = " ".join(name)
    # name_text = tempname + ","
    # position_text = data_obj["position"]

    # Format the description with bullet points
    # description = data_obj["description"]
    # formatted_description = ["• " + item for item in description]

    # Write the text on the image
    image_editable.text(name_position, name, (107, 107, 110), font=title_font)
    # image_editable.text(position_position, position_text, (0, 0, 0), font=title_font)

    # Write each line of the description on the image
    # for i, line in enumerate(formatted_description):
    #     image_editable.text((description_position[0], description_position[1] + i*(font_size+line_spacing)), line, (0,0,0), font=title_font)

    my_image = my_image.convert("RGB")
    my_image.save(f"AppointmentLetters/{tempname}_Certificate.pdf")


# Load JSON file
with open("data.json") as f:
    data = json.load(f)

# data = ["Omesh Vaishnavi Nagave"]

# Define the font size
font_size = 72
line_spacing = 12
# data = ["Abhiraj"]
# Loop through the data
for item in data:
    print(item)
    imgexp(item, font_size, line_spacing)
