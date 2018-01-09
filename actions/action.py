import importlib
from mind.thought import thought

class action(thought):
  def do(action, act_on):
    if(type(act_on) != thought):
      act_on = thought(act_on)
    
    todo = action.split('.')[-1]

    try:
      action = importlib.import_module('actions.'+ action)
      # (act_on)

    except ImportError:
      print("\n[ok]: I don't know how to act - " + action + '.\n')
      # return thought('raise', 'EXIT_FAILURE')
      return thought('')

    try:
      return getattr(action, todo).do(act_on)

    except Exception as e:
      print("[ok]: I know how to act - " + action.__name__ + " but cannot do - " + todo)
      print("[...] Because " + e.args[0])
