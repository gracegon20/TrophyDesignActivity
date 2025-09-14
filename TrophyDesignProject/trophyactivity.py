from PIL import Image, ImageDraw, ImageFont
from rembg import remove
import os
import io
import math

# Create a blank image with white background
img = Image.new('RGB', (1580, 1508), color = (255, 255, 255))
draw= ImageDraw.Draw(img)

# Load fonts (adjust path or use default)
def load_font(font_name, size):
    try:
        return ImageFont.truetype(font_name, size)
    except IOError:
        return ImageFont.load_default()
title_font = load_font("arialbd.ttf", 40)
award_font = load_font("arialbd.ttf", 60)
text_font = load_font("arial.ttf", 30)

# Draw the base of the trophy
canvas_width = 1580 
canvas_height = 1508
base_top = 900
base_width = 600
base_height = 150
border_thickness = 5
margin = 200

base_left = (canvas_width - base_width) // 2

base_top = canvas_height - base_height - margin

draw.rectangle(
    [base_left, base_top, base_left + base_width, base_top + base_height],
    fill="#895716",
    outline="#222016",
    width=border_thickness
)

#Text on the base
text = "INTRAMURALS 2025"
bbox = draw.textbbox((0, 0), text, font=title_font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
text_x = base_left + (base_width - w) // 2
text_y = base_top + (base_height - h) // 2
draw.text((text_x, text_y), text, fill="white", font=title_font)

# Draw an ellipse for design next to the base
ellipse_width = int(base_width * 1.7)   
ellipse_height = int(base_height * 6.5)  
ellipse_left = (canvas_width - ellipse_width) // 2
ellipse_top = base_top - ellipse_height
margin = 20
ellipse_border = 20

draw.ellipse(
    [ellipse_left, ellipse_top,
    ellipse_left + ellipse_width,
    ellipse_top + ellipse_height],
    outline="gold",
    fill = "#FFF8DC",  
    width = ellipse_border
)

# Add smaller rectangle
small_rec_width = int(ellipse_width * 0.4)   
small_rec_height = int(ellipse_height * 0.05) 
small_rec_left = (canvas_width - small_rec_width) // 2

top = base_top - small_rec_height 
bottom = base_top

draw.rectangle(
    [small_rec_left, top, small_rec_left + small_rec_width, bottom],
    fill="gold",
    outline="#E4C214"
)

# Text for Smaller Rectangle
text = "BISU - BALILIHAN CAMPUS"
font_size = 20
font = load_font("arialbd.ttf", font_size)
while True:
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    if w <= small_rec_width and h <= small_rec_height:
        break
    font_size -= 1
    font = load_font("arialbd.ttf", font_size)

text_x = small_rec_left + (small_rec_width - w) // 2
text_y = top + (small_rec_height - h) // 2
draw.text((text_x, text_y), text, fill="black", font=font)

# Add a polygon inside the circle
pol_width = int(small_rec_width * 0.5)  
pol_height = int(small_rec_height * 9)  
trapezoid_top_width = int(pol_width * 0.5)
trapezoid_bottom_width = int(pol_width * 0.8)
trapezoid_height = int(pol_height * 0.5)

trapezoid_top_left = (canvas_width - trapezoid_top_width) // 2
trapezoid_bottom_left = (canvas_width - trapezoid_bottom_width) // 2
trapezoid_bottom = top  
trapezoid_top = trapezoid_bottom - trapezoid_height

# Define the points of the trapezoid
trapezoid_points = [
    (trapezoid_top_left, trapezoid_top),  
    (trapezoid_top_left + trapezoid_top_width, trapezoid_top),  
    (trapezoid_bottom_left + trapezoid_bottom_width, trapezoid_bottom),  
    (trapezoid_bottom_left, trapezoid_bottom) 
]

# Draw the trapezoid
draw.polygon(trapezoid_points, fill="gold", outline="gold")

#Add another circle for design
circle_diameter = int(ellipse_width * 0.75)
circle_left = (canvas_width - circle_diameter) // 2
circle_top = ellipse_top + (ellipse_height - circle_diameter) // 2
circle_bottom = trapezoid_bottom
circle_thickness = 15
draw.ellipse(
    [circle_left, circle_top, 
    circle_left + circle_diameter, 
    circle_top + circle_diameter],
    outline="gold",
    fill = None,
    width = circle_thickness
)

# Add decoration inside the inner circle (before the inner line)
num_small_dots = 26              
small_dot_radius = 20            
outer_radius = circle_diameter // 2
inner_radius = outer_radius - 70  
center_x = canvas_width // 2
center_y = ellipse_top + ellipse_height // 2

small_mid_radius = (inner_radius + outer_radius) // 2 - 20 

for i in range(num_small_dots):
    angle = (2 * math.pi / num_small_dots) * i
    x = center_x + int(small_mid_radius * math.cos(angle))
    y = center_y + int(small_mid_radius * math.sin(angle))

    fill_color = "gold"

    draw.ellipse(
        [x - small_dot_radius, 
        y - small_dot_radius,
        x + small_dot_radius,
        y + small_dot_radius],
        fill=fill_color,
        outline="gold"
    )

# Add two arcs for the left and right sides after the small dots with some space
arc_radius = outer_radius - 50
arc_thickness = 10

# Left arc
left_arc_start_angle = 90  
left_arc_end_angle = 270
draw.arc(
    [center_x - arc_radius, center_y - arc_radius,
     center_x + arc_radius, center_y + arc_radius],
    start=left_arc_start_angle,
    end=left_arc_end_angle,
    fill="gold",
    width=arc_thickness
)

# Right arc
right_arc_start_angle = -90  
right_arc_end_angle = -180
draw.arc(
    [center_x - arc_radius, center_y - arc_radius,
     center_x + arc_radius, center_y + arc_radius],
    start=right_arc_start_angle,
    end=right_arc_end_angle,
    fill="gold",
    width=arc_thickness
)

# Draw another upside down trapezoid with added space
space_between_trapezoids = 20 
up_trap_width = int(pol_width * 1)
up_trap_height = int(pol_height * 0.2)
up_trap_top_width = int(up_trap_width * 0.8)
up_trap_bottom_width = int(up_trap_width * 0.5)
up_trap_bottom_left = (canvas_width - up_trap_bottom_width) // 2
up_trap_bottom = trapezoid_top - space_between_trapezoids  
up_trap_top = up_trap_bottom - up_trap_height
up_trap_top_left = (canvas_width - up_trap_top_width) // 2
up_trap_points = [
    (up_trap_bottom_left, up_trap_bottom),
    (up_trap_bottom_left + up_trap_bottom_width, up_trap_bottom),
    (up_trap_top_left + up_trap_top_width, up_trap_top),
    (up_trap_top_left, up_trap_top)
]
draw.polygon(up_trap_points, fill="gold", outline="gold")

#Add the award text
award_text = "BEST IN CHEER SQUAD".upper()
font_size = 50
text_spacing = 20
font = load_font("arialbd.ttf", font_size) 
text_bbox = draw.textbbox((0, 0), award_text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_x = (canvas_width - text_width) // 2
text_y = up_trap_top - text_height - 120
draw.text((text_x, text_y), award_text, fill="black", font=font)

# Add subtitle text in paragraph form and center it
sub_text = (
    "Given this on 12th day of September during the BISU Intramurals 2025\n"
    "@ Bohol Island State University Balilihan Campus\n"
    "Magsija, Balilihan, Bohol, Philippines."
)
font_size = 18
font = load_font("arial.ttf", font_size)
lines = sub_text.split("\n")
line_spacing = 6  

# Calculate total height of the paragraph
total_text_height = sum(
    draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1]
    for line in lines
) + (len(lines) - 1) * line_spacing

text_y = up_trap_top - total_text_height - 30

for line in lines:
    text_bbox = draw.textbbox((0, 0), line, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = (canvas_width - text_width) // 2
    draw.text((text_x, text_y), line, fill="black", font=font)
    text_y += text_bbox[3] - text_bbox[1] + line_spacing

# Add image for the bisu logo above the small trapezoid
bisu_logo_path = r'TrophyDesignProject\bisu.jpg'
logo = Image.open(bisu_logo_path).convert("RGBA")
datas = logo.getdata()
newData = []
for item in datas:
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        newData.append((255, 255, 255, 0)) 
    else:
        newData.append(item)
logo.putdata(newData)
logo = logo.resize((200, 200))

# Calculate position to place the logo above the small trapezoid
logo_x = (canvas_width - logo.width) // 2
logo_y = up_trap_top - logo.height - 170  

img.paste(logo, (logo_x, logo_y), logo)

# Add picture design for decoration beside the bisu logo
cheer_decoration_path = r'TrophyDesignProject\\cheer.jpg'
decoration = Image.open(cheer_decoration_path).convert("RGBA")
datas = decoration.getdata()
newData = []
for item in datas:
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        newData.append((255, 255, 255, 0)) 
    else:
        newData.append(item)
decoration.putdata(newData)
decoration = decoration.resize((150, 150))

# Calculate position to place the decoration beside the BISU logo
decoration_x = logo_x + logo.width + 5
decoration_y = logo_y + 50  

flipped_decoration = decoration.transpose(Image.FLIP_LEFT_RIGHT)
img.paste(flipped_decoration, (decoration_x, decoration_y), flipped_decoration)

#Add another piture design for the left side of the bisu logo
squad_decoration_path = r'TrophyDesignProject\\squad.jpg'
squad_decoration = Image.open(squad_decoration_path).convert("RGBA")
datas = squad_decoration.getdata()
newData = []
for item in datas:
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        newData.append((255, 255, 255, 0)) 
    else:
        newData.append(item)
squad_decoration.putdata(newData)
squad_decoration = squad_decoration.resize((150, 150))

left_decoration_x = logo_x - squad_decoration.width - 5
left_decoration_y = decoration_y
img.paste(squad_decoration, (left_decoration_x, left_decoration_y), squad_decoration)

#Add some lines for decoration
num_leaves = 24
leaf_length = 70
leaf_width = 25

center_x = canvas_width // 2
center_y = ellipse_top + ellipse_height // 2
outer_radius = circle_diameter // 2
inner_radius = int(outer_radius * 1)  

for i in range(num_leaves):
    angle = (2 * math.pi / num_leaves) * i

    # Position along the middle ring
    mid_radius = (inner_radius + outer_radius) // 2
    mid_x = center_x + int(mid_radius * math.cos(angle))
    mid_y = center_y + int(mid_radius * math.sin(angle))

    # Triangle direction
    dx = math.cos(angle)
    dy = math.sin(angle)

    # Triangle tip & base
    tip_x = mid_x + int(leaf_length * dx)
    tip_y = mid_y + int(leaf_length * dy)
    base_left_x = mid_x - int(leaf_width * dy)
    base_left_y = mid_y + int(leaf_width * dx)
    base_right_x = mid_x + int(leaf_width * dy)
    base_right_y = mid_y - int(leaf_width * dx)

    leaf_points = [(base_left_x, base_left_y),
                   (tip_x, tip_y),
                   (base_right_x, base_right_y)]
    draw.polygon(leaf_points, fill="gold", outline="gold")

# Save the image in the TrophyDesignProject folder
output_folder = r"TrophyDesignProject"
os.makedirs(output_folder, exist_ok=True)  
output_path = os.path.join(output_folder, "TrophyActivity.png")
img.save(output_path)
img = Image.open(output_path)

#Show the image
img.show()

