class EventEmitter(object):
    _event_emitters = []

    def __init__(self):
        EventEmitter._event_emitters.append(self)
        self._events = {}

    def __del__(self):
        EventEmitter._event_emitters.remove(self)

    def on(self, event, listener):
        if not event in self._events:
            self._events[event] = []
        self._events[event].append(listener)

    def emit(self, event, *args, **kwargs):
        if event in self._events:
            for listener in self._events[event]:
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
