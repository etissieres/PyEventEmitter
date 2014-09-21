PyEventEmitter
==============

Python events library, heavily inspired by Node.js' EventEmitter.

Installation
============

::

    $ pip install PyEventEmitter

How to use
==========

The library provides an EventEmitter class. This class let you bind
listeners to events and trigger events.

.. code:: python

    import event_emitter as events

    em = events.EventEmitter()

    def hello(who):
        print('Hello {}'.format(who))

    em.on('hello', hello)
    em.emit('hello', who='World')  # prints Hello World

You can also use ``on`` decorator :

.. code:: python

    import event_emitter as events

    em = events.EventEmitter()

    @events.on(emitter=em, event='hello')
    def hello(who):
        print('Hello {}'.format(who))

    em.emit('hello', who='World')  # prints Hello World

Using ``once`` instead of ``on`` may be usefull if you want your
listener to be called once :

.. code:: python

    import event_emitter as events

    em = events.EventEmitter()

    def hello(who):
        print('Hello {}'.format(who))

    em.once('hello', hello)
    em.emit('hello', who='World')  # prints Hello World
    em.emit('hello', who='World')  # nothing happens

Of course, there is also a decorator for this :

.. code:: python

    import event_emitter as events

    em = events.EventEmitter()

    @events.once(emitter=em, event='hello')
    def hello(who):
        print('Hello {}'.format(who))

    em.emit('hello', who='World')  # prints Hello World

You can remove a listener bound to an event :

.. code:: python

    import event_emitter as events

    em = events.EventEmitter()

    def hello(who):
        print('Hello {}'.format(who))

    em.on('hello', hello)
    em.remove('hello', hello)
    em.emit('hello', who='World')  # nothing happens

You can also remove all listeners bound to an event thanks to
``remove_all``.

The ``count`` method returns the number of listeners bound to an event :

.. code:: python

    import event_emitter as events

    em = events.EventEmitter()

    def hello(who):
        print('Hello {}'.format(who))

    em.on('hello', hello)
    print(em.count('hello'))  # prints 1

