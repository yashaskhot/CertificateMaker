import json
from PIL import Image, ImageFont, ImageDraw

def imgexp(data_obj, font_size):
    my_image = Image.open("AppointmentLetter.png")
    title_font = ImageFont.truetype('arial.ttf', font_size)
    image_editable = ImageDraw.Draw(my_image)
    
    # Position the text
    name_position = (730, 1810)  #found this value by trial and error plz dont change
    position_position = (575, 2145)
    description_position = (650, 3000)
    
    # Format the text
    tempname = data_obj['name']
    name_text = tempname+","
    position_text = data_obj['position']
    
    # Format the description with bullet points
    description = data_obj['description']
    formatted_description = ["• " + item for item in description]
    
    # Write the text on the image
    image_editable.text(name_position, name_text, (0,0,0), font=title_font)
    image_editable.text(position_position, position_text, (0,0,0), font=title_font)

    # Write each line of the description on the image
    for i, line in enumerate(formatted_description):
        image_editable.text((description_position[0], description_position[1] + i*font_size), line, (0,0,0), font=title_font)
    
    my_image=my_image.convert('RGB')
    my_image.save(f"AppointmentLetters/{tempname}_Certificate.png")

# Load JSON file
with open('data.json') as f:
    data = json.load(f)

# Define the font size
font_size = 60

# Loop through the data
for item in data:
    imgexp(item, font_size)
