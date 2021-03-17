from random import randint
import time 
width = 800
height =  600

circle_size = 26
margin = 2

passpartout = circle_size*2
max_width = width-passpartout
max_height = height-passpartout

color_palette_joggen = ["#A3A798", "#C9C0AF", "#C2B08C"]
#["#898F80", "#D2BEA9","#C2B08C"]
color_palette_1 = ["#fffffa","#0d5c63","#44a1a0","#78cdd7","#247b7b"] #https://coolors.co/fffffa-0d5c63-44a1a0-78cdd7-247b7b 
color_palette_2 = ["#51a3a3","#75485e","#cb904d","#dfcc74","#c3e991"] #https://coolors.co/51a3a3-75485e-cb904d-dfcc74-c3e991
color_palette_3 = ["#d9e5d6","#00a7e1","#eddea4","#f7a072","#ff9b42"] #https://coolors.co/d9e5d6-00a7e1-eddea4-f7a072-ff9b42
color_palette_4 = ["#ffadad","#ffd6a5","#fdffb6","#caffbf","#9bf6ff","#a0c4ff","#bdb2ff","#ffc6ff","#fffffc"] #https://coolors.co/ffadad-ffd6a5-fdffb6-caffbf-9bf6ff-a0c4ff-bdb2ff-ffc6ff-fffffc
color_palette_5 = ["#f94144","#f3722c","#f8961e","#f9844a","#f9c74f","#90be6d","#43aa8b","#4d908e","#577590","#277da1"] #https://coolors.co/f94144-f3722c-f8961e-f9844a-f9c74f-90be6d-43aa8b-4d908e-577590-277da1
color_palette_6 = ["#1a535c","#4ecdc4","#f7fff7","#ff6b6b","#ffe66d"]
color_palette_7 = ["#ff7eb9", "#ff65a3","#7afcff", "#feff9c", "#fff740"]
color_palette_8 = ["#f1e8b8","#f9e784","#77B6EA","#EFB9CB", "#BCD0B40"]
#color_palette_9 = ["#EAF0CE", "#C0C5C1","#083D77" ]
color_palette_9 = ["#EAF0CE", "#FF934F","#58A4B0" ]
color_palette_10 = ["#d9e5d6", "#eddea4","#A7CADC","#FFB370"] #https://coolors.co/d9e5d6-00a7e1-eddea4-f7a072-ff9b42
color_palette_11 = ["#cc7722","#800000","#003300","#002266"]
roygbiv_warm = [
      '#705f84',
      '#687d99',
      '#6c843e',
      '#fc9a1a',
      '#dc383a',
      #'#aa3a33',
      '#9c4257'
    ]


color_palette = roygbiv_warm
file_name = "roygbiv_warm"

def get_absolute_max_for_line(max_amount_on_line):
    if(max_amount_on_line < max_width/circle_size): 
        return max_amount_on_line
    else: 
        return max_width/circle_size
    
def get_start_position(max_amount_on_line): 
    return ((max_width - (max_amount_on_line*circle_size)) - ((max_width - (max_amount_on_line*circle_size))/2)) + (circle_size)

def setup():
    size(width, height)
    
    #background(30, 30, 30)
    background(255, 255, 255)
    
    pixelDensity(2)


    max_amount_on_line = 1
    amount_on_line = 0
    alpha_level = 0
    x = get_start_position(max_amount_on_line)
    y = height - passpartout
    max_rotation = 0
    x_margin = 5
    y_margin = -5
    #Calculate these instead
    cs = circle_size
    while(y > 0):
        if(amount_on_line >= max_amount_on_line):
            amount_on_line = 0
            increase_by_amount = randint(1, 2)
            max_amount_on_line = max_amount_on_line + randint(1,2)
            x = get_start_position(max_amount_on_line)
            y -= circle_size - y_margin
            alpha_level += 10
            x_margin += 4
            y_margin -= 6
            cs += 4
                        
        amount_on_line += 1
        pushMatrix();
        # Draw Shadow
        noStroke()
        fill(15, 15, 15, 5)

        strokeWeight(1)
        stroke(30, 30, 30)
        col = color_palette[randint(0, len(color_palette)-1)]

        rgb = tuple(int(col.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        fill(rgb[0], rgb[1], rgb[2], alpha_level)
        
        translate(x, y)
        circle(0, 0, cs)
        popMatrix();
        x = x + circle_size + x_margin

        
    
    save("results/"+file_name+"-" + str(time.time()) + ".png")
