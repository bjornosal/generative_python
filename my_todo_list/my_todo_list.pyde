from random import randint
import time 
width = 6000
height =  8000

square_size = 260
margin = 20

passpartout = square_size*2
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

color_palette = color_palette_10
file_name = "color_palette_10"

def get_absolute_max_for_line(max_amount_on_line):
    if(max_amount_on_line < max_width/square_size): 
        return max_amount_on_line
    else: 
        return max_width/square_size
    
def get_start_position(max_amount_on_line): 
    return ((max_width - (max_amount_on_line*square_size)) - ((max_width - (max_amount_on_line*square_size))/2)) + (square_size)

def setup():
    size(width, height)
    
    #background(30, 30, 30)
    background(255, 255, 255)
    
    # Take advantage of resolution
    pixelDensity(2)

    # start med halve
    # øk med et tilfeldig antall til siden er fylt
    # start med orden
    # end i kaos
    # viktig - passpartou på 2 firkanter

    
    # max_amount_on_line = (max_width/2)/square_size
    max_amount_on_line = 2
    amount_on_line = 0
    
    x = get_start_position(max_amount_on_line)
    y = 0 + passpartout
    max_rotation = 0
    while(y < max_height):
        if(amount_on_line >= max_amount_on_line):
            amount_on_line = 0
            increase_by_amount = randint(1, 2)
            max_amount_on_line = get_absolute_max_for_line(max_amount_on_line + randint(1,2))
            x = get_start_position(max_amount_on_line)
            y = y + square_size + margin
            if(y >= max_height/4): 
                #should rotate max to 80 degrees?
                max_rotation += 5

            if(y >= max_height): 
                continue
            
        amount_on_line += 1
        
        pushMatrix();
        # Draw Shadow
        noStroke()
        fill(15, 15, 15, 5)

        strokeWeight(4)
        stroke(30, 30, 30)
        col = color_palette[randint(0, len(color_palette)-1)]
        
        # move grid down to rotate
        fill(col)
        translate(x, y)
        rotate(radians(random(-max_rotation, max_rotation)))
        square(0, 0, square_size)
        popMatrix();
        x = x + square_size + margin
        
    
    save("results/"+file_name+"-" + str(time.time()) + ".png")
