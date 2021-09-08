
import tsapp as ts

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

def add_to_scene(frame, *args):
    """Adds all sprites to the scene, returns a list of all objects in the scene"""
    objarr = []
    for i in range(len(args)):    # Adds every sprite in the args to a list
        frame.add_object(args[i])
        objarr.append(args[i])
        
    return objarr  # Returns the list of objects
        
def rotate(sprite, degs):
    """Adds or subtracts from the angle of the sprite to spin it"""
    sprite.angle = degs

        
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
