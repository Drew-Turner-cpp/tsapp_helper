
import tsapp as ts

def txt_align(x, y, textobj):
    """Aligns the text object given to the two alignment args"""
    sprite.align = x
    sprite.align = y
    
def center_on(moveobj, centerobj, offset=50):
    """Centers one object on another"""
    moveobj.x = centerobj.x + offset
    moveobj.y = centerobj.y + offset

def add_to_scene(frame, *args):
    """Adds all sprites to the scene"""
    for i in range(len(args)):
        frame.add_object(args[i])
        
def rotate(sprite, degs):
    """sets the sprites angle"""
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
        sprite.angle += speed
        
    
