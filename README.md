# ok.
A programmable simple AI assistant for linux. Written in Python3 with minimum dependency.  

## Getting Started
Just download/clone it and run it.
```
$ git clone https://github.com/0xcrypto/ok && cd ok
$ ./ok hi!
```

## It does nothing!
Presently, it just echoes what you say. This is a 3 hours quick hack but is heavily under development and I will be adding more intelligence to it soon. 

## Adding intelligence
If you like, you can add some intelligence yourself. Just read the code and figure it out yourself. It is midnight 1:17 here and I am feeling sleepy already. Will write instructions to add intelligence tomorrow. For now, I can give you a hint only.

1. Make an action that accepts thought object as argument and returns a thought object. Action can be a module, package or just function. It must reside in actions as a convention. 
2. Add some logic (which is the intelligence) to interpret the action in actions/think.py. Be it simple if...else statements or some probability stuff, you can do anything there.

Adding logic to think.py is the hardest part.

## Contributing
Simply send PRs and raise issues here. For documentation and future progress, checkout the [trello board](https://trello.com/b/CAvOh70N/ok-ai)

## Origin
In early 2016, I started a secret project codenamed Alvis with my friend. But due to some reason, we couldn't accomplish anything other than a simple hand drawn model. After nearly 2 years, I realised this model was not so bad and I could actually build it. So... here it is.