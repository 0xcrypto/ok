# okai. ![progress: initial stage](https://img.shields.io/badge/progress-initial%20stage-blue.svg)
A programmable simple AI bot (without any AI so far) in Python.

## The name
Okai is pronounced as o-kaa-e. It is short for "obviously knows artificial intelligence". Okai is a guy.

## What is it/he for?
I am confused too. But for now, you can use him as your butler. Ask him to do
anything, he will do it. Ofcourse you will need to teach him first.

## Getting Started
Just download/clone it and run it.
```
$ git clone https://github.com/0xcrypto/ok && cd ok
$ ./ok express.printterm Hello!
```

## He cannot do anything!
Well everything depends on actions installed. For now, there are little to no actions. But you can always build one yourself. In the nearby future, Okai will generate actions itself (learning on itself... the skill that makes us intellect species).

## Adding intelligence
If you like, you can add some intelligence yourself. 

1. Make an action that accepts thought object as argument and returns a thought/action object. Action can be a module, package or just function. It must reside in actions. 
2. Add some logic (which is the intelligence) to interpret the thought in actions. Be it simple if...else statements or some probability stuff, you can literally do anything.
4. Command okai with 
``` $ ./ok [your_action] [some_input_to_act_on] ```

## Contributing
Simply send PRs and raise issues here. For documentation, present development and future plans, checkout the [trello board](https://trello.com/b/CAvOh70N/ok-ai)
