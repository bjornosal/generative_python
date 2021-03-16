import time 
from random import randint
# Size Parameters
w, h = 800, 600

# Circle Size
cs = 40




#bottom = 1 - no color
# more color /grading as you move away from starting circle
# More circles as you get further away
color_palette_9 = ["#EAF0CE", "#FF934F", "#58A4B0" ]
color_palette_old_image = ["#cc7722","#800000","#03300","#002266"]
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

def setup():
    size(w, h)
    
    #background(30, 30, 30)
    background(255, 255, 255)
    
    # Take advantage of resolution
    pixelDensity(2)
    
    start_x = random(w/2, w - w/2)
    start_y = random(h-h/12, h-h/13)
     # Draw Shadow
    noStroke()
    fill(15, 15, 15, 5)
    # Draw Circle
    stroke(30, 30, 30)

    fill(0,0,0,20)
    circle(start_x, start_y, cs)
    
    y_loc_start = h-h/6
    y_loc_end = h-h/7
    x_loc_start = w/2-cs
    x_loc_end = w/2+cs
    
    amount_per_line = 1
    drawn = 0
    col_alpha = 20
    # doble antall per 'linje'
    # fjerne 1/2 sirkel-størrelse per linje
    
    while(y_loc_end > 100): 
        print(y_loc_end)
        if(drawn == amount_per_line): 
            y_loc_start -= cs   
            y_loc_end -= cs
            
            x_loc_start -= cs
            x_loc_end += cs
            
            if(x_loc_start < 40): 
                x_loc_start = 40
                
            if(x_loc_end > w-40): 
                x_loc_end = w-40
                
            drawn = 0
            amount_per_line += 1
            col_alpha += 15
        
        center_x = random(x_loc_start, x_loc_end)
        center_y = random(y_loc_start, y_loc_end)
        
        # Draw Shadow
        noStroke()
        fill(15, 15, 15, 5)

        # Draw Circle
        stroke(30, 30, 30)
        # Random color out of color scheme + increase alpha
        col = color_palette[randint(0, len(color_palette)-1)]
        rgb = tuple(int(col.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        fill(rgb[0], rgb[1], rgb[2], col_alpha)
        circle(center_x, center_y, cs)
        drawn += 1
        
    seed = time.time()    
    save("results/" + str(seed) + ".png")
