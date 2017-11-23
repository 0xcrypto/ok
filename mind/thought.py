class thought(object):
  """ thought object """
  act = on = ''

  def __init__(self, this, do='', posX=0, posY=0, posZ=0, posT=0):
    self.position = {'x': posX, 'y': posY, 'z': posZ, 't': posT} # thought vector as in 4d space.
    self.act = do
    self.on = this


