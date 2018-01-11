class thought(object):
  """ thought object """
  act = on = ''

  def __init__(self, this='', do='', posX=0, posY=0, posZ=0, posT=0):
    self.position = {'x': posX, 'y': posY, 'z': posZ, 't': posT} # thought vector as in 4d space.
    self.act = do
    self.on = this

  def __add__(self, secondThought):
    return thought(self.on + secondThought.on,
      secondThought.act, 
      self.position['x'] + self.position['x'],
      self.position['y'] + self.position['y'],
      self.position['z'] + self.position['z'],
      self.position['t'] + self.position['t']
    )

  def __repr__(self):
    on = self.on.__repr__()
    if( self.act ):
      toRet = "[Thought Object: "+ self.__name__() +"] (" + self.act + "): " + on
    else:
      toRet = "[Thought Object: "+ self.__class__.__name__ +"] (bare): " + on 
    
    try:
      toRet += "\n" + self.position.__repr__()
    except:
      pass
    return toRet
