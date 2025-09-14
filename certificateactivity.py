from PIL import Image, ImageDraw, ImageFont
from rembg import remove
import os
import io

# Create a blank image with white background
img = Image.new('RGB', (2480, 3508), color = (255, 255, 255))

# Rotate the image to landscape orientation
rotated_img = img.rotate(90, expand=True)

# Add black border to the image
draw = ImageDraw.Draw(rotated_img)
border_color = (0, 0, 0)
border_width = 5
margin = 40
draw.rectangle(
    [margin + border_width // 2, margin + border_width // 2,
     rotated_img.width - margin - border_width // 2, rotated_img.height - margin - border_width // 2],
    outline=border_color,
    width=border_width
)

# Add purple border inside the black border
purple_color = (189, 140, 195)
purple_border_width = 25
margin += 40
draw.rectangle(
    [margin + border_width + purple_border_width // 2, margin + border_width + purple_border_width // 2,
     rotated_img.width - margin - border_width - purple_border_width // 2, rotated_img.height - margin - border_width - purple_border_width // 2],
    outline=purple_color,
    width=purple_border_width
)

#Putting BISU logo on the top left corner
bisu_logo_path = r'TrophyDesignProject\bisu.jpg'
logo = Image.open(bisu_logo_path).convert("RGBA")
left_margin = 700
top_margin = 200
datas = logo.getdata()
newData = []
for item in datas:
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        newData.append((255, 255, 255, 0)) 
    else:
        newData.append(item)
logo.putdata(newData)
logo = logo.resize((200, 200))
rotated_img.paste(logo, (left_margin, top_margin), logo)

#Add text to the top center of the image
title_text = "Republic of the Philippines"
subtitle_text = "Bohol Island State University"
department_text = "College of Computing and Information Sciences"
place_text = "Magsija, Balilihan, Bohol"

certificate_text = "Certificate of Recognition"
sub_text = "is awarded to"




# #Putting CCIS logo on the top right corner
# ccis_logo_path = r'TrophyDesignProject\ccis.jpg'
# ccis_logo = Image.open(ccis_logo_path).convert("RGBA")
# ccis_left_margin = 1800
# ccis_top_margin = 200
# ccis_datas = ccis_logo.getdata()
# ccis_newData = []
# for item in ccis_datas:
#     if item[0] > 200 and item[1] > 200 and item[2] > 200:
#         ccis_newData.append((255, 255, 255, 0)) 
#     else:
#         ccis_newData.append(item)
# ccis_logo.putdata(ccis_newData)
# ccis_logo = ccis_logo.resize((180, 180))
# rotated_img.paste(ccis_logo, (ccis_left_margin, ccis_top_margin), ccis_logo)

# Show the image
rotated_img.show()
