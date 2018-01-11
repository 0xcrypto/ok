import importlib
from mind.thought import thought

class action(thought):
  def do(action, act_on):
    if(type(act_on) != thought):
      act_on = thought(act_on)
    
    todo = action.split('.')[-1]

    if( not callable(action) ):
      try:
        action = importlib.import_module('actions.'+ action)
  
      except ImportError:
        print("\n[ok]: I don't know how to - " + action + '.\n')
        # return thought('raise', 'EXIT_FAILURE')
        return thought('')

      try:
        toAct = getattr(action, todo)()
        return toAct.do(act_on)
      
      except Exception as e:
        print("[ok]: I can - " + action.__name__ + " but cannot - " + todo)
        print("[...] Because " + e.args[0])
        print()
        print(e)

    else:
      return action(act_on)
    
    return thought('')
    # return thought('raise', 'EXIT_FAILURE')
