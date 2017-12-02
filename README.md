# ok.
A programmable simple AI framework in Python.  

## Getting Started
Just download/clone it and run it.
```
$ git clone https://github.com/0xcrypto/ok && cd ok
$ ./ok hi!
```

## It does nothing!
Presently, it just echoes what you say. It is heavily under development and I will be adding more intelligence to it soon. 

## Adding intelligence
If you like, you can add some intelligence yourself. 

1. Make an action that accepts thought object as argument and returns a thought/action object. Action can be a module, package or just function. It must reside in actions. 
2. Add some logic (which is the intelligence) to interpret the thought in actions. Be it simple if...else statements or some probability stuff, you can do anything.
3. Presently everything is a mess. So you will need to hardcode the call to your action in `ok` file.
```action.do('your_action_name', some_input_to_act_on)```

## Contributing
Simply send PRs and raise issues here. For documentation, present development and future plans, checkout the [trello board](https://trello.com/b/CAvOh70N/ok-ai)

## Future
I am quite excited with this project. Being simple to implement and smaller in size, I have decided to craft it into an ai engine for some game engines (pygame and maybe a javascript port for phaser too)
