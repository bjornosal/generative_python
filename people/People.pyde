import time 
# Size Parameters
w, h = 600, 800

# Circle Size
cs = 40




#bottom = 1 - no color
# more color /grading as you move away from starting circle
# More circles as you get further away
def setGradient(int x, int y, float w, float h, color c1, color c2, int axis ) {

  noFill();

  if (axis == Y_AXIS) {  // Top to bottom gradient
    for (int i = y; i <= y+h; i++) {
      float inter = map(i, y, y+h, 0, 1);
      color c = lerpColor(c1, c2, inter);
      stroke(c);
      line(x, i, x+w, i);
    }
  }  
  else if (axis == X_AXIS) {  // Left to right gradient
    for (int i = x; i <= x+w; i++) {
      float inter = map(i, x, x+w, 0, 1);
      color c = lerpColor(c1, c2, inter);
      stroke(c);
      line(i, y, i, y+h);
    }
  

def setup():
    size(w, h)
    
    #background(30, 30, 30)
    background(255, 255, 255)
    
    # Take advantage of resolution
    pixelDensity(2)
    
    start_x = random(w/10, w - w/10)
    start_y = random(h-h/12, h-h/13)
     # Draw Shadow
    noStroke()
    fill(15, 15, 15, 5)
    # Draw Circle
    stroke(30, 30, 30)

    fill(0,0,0)
    circle(start_x, start_y, cs)
    
    y_loc_start = h-h/6
    y_loc_end = h-h/7
    x_loc_start = w/2-cs
    x_loc_end = w/2+cs
    
    amount_per_line = 1
    drawn = 0
    # doble antall per 'linje'
    # fjerne 1/2 sirkel-størrelse per linje
    
    while(y_loc_end > 100): 
        print(y_loc_end)
        if(drawn == amount_per_line): 
            y_loc_start -= cs   
            y_loc_end -= cs
            
            x_loc_start -= cs
            x_loc_end += cs
            
            if(x_loc_start < 0): 
                x_loc_start = 0
                
            if(x_loc_end > w): 
                x_loc_end = w
                
            drawn = 0
            amount_per_line += 1
        
        center_x = random(x_loc_start, x_loc_end)
        center_y = random(y_loc_start, y_loc_end)
        
        # Draw Shadow
        noStroke()
        fill(15, 15, 15, 5)

        # Draw Circle
        stroke(30, 30, 30)
        #fill(random(0, 255), random(0, 255), random(0, 255), random(100, 255))
        #fill(random(150, 255), random(200, 255), random(185, 255), random(0, 115))
        circle(center_x, center_y, cs)
        drawn += 1
        
    seed = time.time()    
    save("results/" + str(seed) + ".png")
