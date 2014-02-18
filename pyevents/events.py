class EventEmitter(object):
    event_emitters = []

    def __init__(self):
        EventEmitter.event_emitters.append(self)
        self._events = {}

    def __del__(self):
        EventEmitter.event_emitters.remove(self)

    def on(self, event, listener):
        if not event in self._events:
            self._events[event] = []
        self._events[event].append(listener)

    def once(self, event, listener):
        def wrapper(*args, **kwargs):
            self.remove(event, wrapper)
            listener(*args, **kwargs)
        self.on(event, wrapper)

    def emit(self, event, *args, **kwargs):
        if event in self._events:
            # 'once' may delete items while iterating over listeners -> we use a copy
            listeners = self._events[event][:]
            for listener in listeners:
                listener(*args, **kwargs)

    def remove(self, event, listener):
        if event in self._events:
            self._events[event].remove(listener)

    def remove_all(self, event):
        if event in self._events:
            self._events[event] = []

    def count(self, event):
        return len(self._events[event]) if event in self._events else 0


def on(event_emitter, event):
    def decorator(func):
        event_emitter.on(event, func)
        return func
    return decorator


def once(event_emitter, event):
    def decorator(func):
        event_emitter.once(event, func)
        return func
    return decorator
