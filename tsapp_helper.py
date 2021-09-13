
import tsapp as ts
###############################################################################################
"""
            Adding to a scene
"""
###############################################################################################
def add_to_scene(frame, *args):
    """Adds all sprites to the scene, returns a list of all objects in the scene"""
    objarr = []
    for i in range(len(args)):    # Adds every sprite in the args to a list
        frame.add_object(args[i])
        objarr.append(args[i])
        
    return objarr  # Returns the list of objects
###############################################################################################
"""
            Positioning and moving functions
"""
###############################################################################################
def lock_to_mouse(obj):
    """Centers an object on the mouse"""
    obj.center_x = ts.get_mouse_x()
    obj.center_y = ts.get_mouse_y()

def pos_offset(offx, offy, obj):
    """Adds the offset to the object deturmined by the offest args"""
    obj.x += offx
    obj.y += offy

def txt_align(x, y, textobj):
    """Aligns the text object given to the two alignment args"""
    textobj.align = x
    textobj.align = y
    
def center_on(moveobj, centerobj, offset=50):
    """Centers one object on another"""
    moveobj.x = centerobj.center_x + offset
    moveobj.y = centerobj.center_y + offset
        
def rotate(sprite, degs):
    """Adds or subtracts from the angle of the sprite to spin it"""
    sprite.angle = degs
###############################################################################################
"""
            Edge Collision
"""
###############################################################################################
def check_edge(obj, window):
    """Checks if the center of an image is out of bounds and returns true if it is"""
    if obj.center_x <= 0 or obj.center_y <= 0:  # If obj is out of bounds
        return True                             # return true
    elif obj.center_x >= window.width or obj.center_y >= window.height:
        return True
    else:
        return False
    
def bounce_edge(obj, window):
    """Checks for edge and reverses the direction from witch it came"""
    if obj.center_x <= 0:
        obj.x_speed *= -1
    elif obj.center_y <= 0:
        obj.y_speed *= -1

    elif obj.center_x >= window.width:
        obj.x_speed *= -1
    elif obj.center_y >= window.height:
        obj.y_speed *= -1
###############################################################################################
"""
            Specialized Classes:
            
            Movement
            Cursor
            Animation
"""
###############################################################################################
class Movement:
    def __init__(self, mspeed):
        """Create a new movement object"""
        self.ms = mspeed
        
        self.mkdict ={ts.K_UP: [0, -self.ms], ts.K_DOWN: [0, self.ms],  # This is used for the x and y offests 
            ts.K_LEFT: [-self.ms, 0], ts.K_RIGHT: [self.ms, 0]}         # for each key, I found this to be the
                                                                        # easiest way to store the offsets
        self.mklist = [ts.K_UP, ts.K_DOWN, ts.K_LEFT, ts.K_RIGHT]
        
        self.dirlist = {'up': [0, -self.ms], 'down': [0, self.ms],      # This is for checking and applying to
            'left': [-self.ms, 0], 'right': [self.ms, 0]}               # the dictionary
    
    def arrow_move(self, sprite):
        """Applies a movement check to a sprite"""
        for i in range(len(self.mklist)):             # Check if any of the keys in mklist have been pressed.
            if ts.is_key_down(self.mklist[i]):        # Then add the offset specified by the key pressed
                sprite.x += self.mkdict[self.mklist[i]][0]
                sprite.y += self.mkdict[self.mklist[i]][1]

                
    def spin(self, speed, sprite):
        """Rotates at a constant rate"""
        if sprite is None:
            return True
        sprite.angle += speed
###############################################################################################
class Cursor:
    def __init__(self, follower_img, objlist):
        self.c = follower_img
        self.c.scale = 0.01   # Scale the follower down as to not be visible
        self.ojl = objlist    # Used in detect() to return the sprite the follower is colliding with
        
    def detect(self):
        """Runs the detecting algorythm with a scaled down png"""
        for i in range(len(self.ojl)):
            lock_to_mouse(self.c)  # Lock the follower image to the mouse
            
            if self.c.is_colliding_rect(self.ojl[i]):  # If the follower is colliding with a sprite in the object
                if self.ojl[i] is None:                # list and returns it
                    # if the sprite is a NoneType then return the first sprite in the list
                    return self.ojl[0]
                return self.ojl[i] # Return object colliding with the follower
###############################################################################################
class Animation:
    def __init__(self, window, framerate=30):
        self.fps = framerate
        self.win = window
        
    def animate_seq(self, sprite, duration, *args):
        """Takes the sprite, and a duration with a series of images
            and displays them in a sequence of even intervals"""
        ilist = []  # List for the images 
        
        for i in range(len(args)):
            # Takes all images in *args and sppends them to a list
            # I do this for easier handling and for future compatability
            ilist.append(args[i])
            
        tick = round(duration/len(ilist))  
        # A tick is equal to the duration over the length of the 
        # image list rounded to the nearest whole number.
        
        for x in range(len(ilist)):      # For every image in the list
            for wait in range(tick):     # change the sprites image to
                sprite.image = ilist[x]  # one image in the image list
                self.win.finish_frame()  # then changes to the another 
                                         # after the time of a tick has passed
