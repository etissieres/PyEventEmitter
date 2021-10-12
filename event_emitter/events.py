__all__ = ["EventEmitter", "on", "once"]

import types
import typing


class ListenerWrapper(object):
    def __init__(self, listener, is_once=False):
        self.listener = listener
        self.is_once = is_once

    def __call__(self, *args, **kwargs) -> typing.NoReturn:
        self.listener(*args, **kwargs)

    def __eq__(self, other) -> bool:
        if isinstance(other, ListenerWrapper):
            return other.listener == self.listener
        if isinstance(other, types.FunctionType):
            return other == self.listener
        return False


class EventEmitter(object):
    def __init__(self):
        self._events: dict = {}

    def on(self, event, listener) -> typing.NoReturn:
        self._on(event, ListenerWrapper(listener))

    def once(self, event, listener) -> typing.NoReturn:
        self._on(event, ListenerWrapper(listener, is_once=True))

    def _on(self, event, listener_wrapper) -> typing.NoReturn:
        if event not in self._events:
            self._events[event] = []
        self._events[event].append(listener_wrapper)

    def emit(self, event, *args, **kwargs) -> typing.NoReturn:
        if event in self._events:
            # 'once' may delete items while iterating over listeners -> we use a copy
            listeners = self._events[event][:]
            for listener in listeners:
                if listener.is_once:
                    self.remove(event, listener)
                listener(*args, **kwargs)

    def remove(self, event, listener) -> typing.NoReturn:
        if event in self._events:
            events = self._events[event]
            if listener in events:
                events.remove(listener)

    def remove_all(self, event) -> typing.NoReturn:
        if event in self._events:
            self._events[event] = []

    def count(self, event) -> int:
        return len(self._events[event]) if event in self._events else 0


def on(emitter, event) -> typing.Any:
    def decorator(func):
        emitter.on(event, func)
        return func

    return decorator


def once(emitter, event) -> typing.Any:
    def decorator(func):
        emitter.once(event, func)
        return func

    return decorator
