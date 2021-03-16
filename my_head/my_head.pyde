from random import randint
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

color_palette = color_palette_10
file_name = "color_palette_10"


# Plan: 
# Depict how my brain actually works
# Fountain that sprouts thoughts? 
# K.I.S.S.
# Line
# Thought clouds begin small and end larger

def setup(): 
    size(width, height)
    
    #background(30, 30, 30)
    background(255, 255, 255)
    
    # Draw fountain bottom
    # devide into 6, start after first
    start_x = width/3.5
    end_x = width - start_x
    line_y = height - height/5
    
    strokeWeight(3)
    line(start_x,line_y,end_x,line_y)
    
    # Draw arcs
    
    
    noFill()
    pushMatrix()
    translate(end_x-50, line_y-50)
    rotate(radians(115))
    arc(0, 0, 150, 100, radians(30), radians(160))
    popMatrix()
    
    pushMatrix()
    translate(start_x-50, line_y-50)
    rotateX(radians(100));
    arc(100, 0, 100, 150, radians(-160), radians(0))
    popMatrix()
    
    
    
    
    
    
    
    
    
    # Draw Shadow
    noStroke()
    fill(15, 15, 15, 5)

    #strokeWeight(4)
    stroke(30, 30, 30)
    col = color_palette[randint(0, len(color_palette)-1)]
    fill(col)
    circle(100, 100, circle_size)
