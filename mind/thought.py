class thought(object):
  """ thought object """
  act = on = ''

  def __init__(self, this, do=''):
    self.act = do
    self.on = this