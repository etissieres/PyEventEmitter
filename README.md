# PyEvents

Python events library.

# How to use

The library provides an EventEmitter class.
This class let you bind listeners to events and trigger events.

```python
import pyevents.events as events

em = events.EventEmitter()

def hello(who):
    print('Hello {}'.format(who))

em.on('hello', hello)
em.emit('hello', who='World')  # prints Hello World
```

You can also use `on` decorator :

```python
import pyevents.events as events

em = events.EventEmitter()

@events.on(emitter=em, event='hello')
def hello(who):
    print('Hello {}'.format(who))

em.emit('hello', who='World')  # prints Hello World
```

Using `once` instead of `on` may be usefull if you want your listener to be called once :

```python
import pyevents.events as events

em = events.EventEmitter()

def hello(who):
    print('Hello {}'.format(who))

em.once('hello', hello)
em.emit('hello', who='World')  # prints Hello World
em.emit('hello', who='World')  # nothing happens
```
