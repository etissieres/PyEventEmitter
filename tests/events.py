import unittest as test
import event_emitter as events


class TestEventEmitter(test.TestCase):
    def setUp(self):
        self.em = events.EventEmitter()

    def test_add_listener(self):
        times_hello_emitted = 0

        @events.on(emitter=self.em, event="hello")
        def hello(name, age):
            nonlocal times_hello_emitted
            times_hello_emitted += 1
            self.assertEqual(name, "toto")
            self.assertEqual(age, 22)

        self.em.on("hello", hello)
        self.assertEqual(self.em.count("hello"), 2)
        self.em.emit("hello", "toto", age=22)
        self.assertEqual(times_hello_emitted, 2)

    def test_add_once_listener(self):
        times_hello_emitted = 0

        @events.once(emitter=self.em, event="hello")
        def hello(name, age):
            nonlocal times_hello_emitted
            times_hello_emitted += 1
            self.assertEqual(name, "toto")
            self.assertEqual(age, 22)

        self.em.once("hello", hello)
        self.assertEqual(self.em.count("hello"), 2)
        self.em.emit("hello", "toto", age=22)
        self.assertEqual(times_hello_emitted, 2)
        self.assertEqual(self.em.count("hello"), 0)

    def test_remove_listener(self):
        times_hello_emitted = 0

        def hello():
            nonlocal times_hello_emitted
            times_hello_emitted += 1

        self.em.on("hello", hello)
        self.assertEqual(self.em.count("hello"), 1)
        self.em.remove("hello", hello)
        self.assertEqual(self.em.count("hello"), 0)
        self.em.emit("hello")
        self.assertEqual(times_hello_emitted, 0)

    def test_remove_once_listener(self):
        times_hello_emitted = 0

        def hello():
            nonlocal times_hello_emitted
            times_hello_emitted += 1

        self.em.once("hello", hello)
        self.assertEqual(self.em.count("hello"), 1)
        self.em.remove("hello", hello)
        self.assertEqual(self.em.count("hello"), 0)
        self.em.emit("hello")
        self.assertEqual(times_hello_emitted, 0)

    def test_remove_all_listener(self):
        times_hello_emitted = 0

        @events.on(emitter=self.em, event="hello")
        def hello():
            nonlocal times_hello_emitted
            times_hello_emitted += 1

        self.em.on("hello", hello)
        self.assertEqual(self.em.count("hello"), 2)
        self.em.remove_all("hello")
        self.assertEqual(self.em.count("hello"), 0)
        self.em.emit("hello")
        self.assertEqual(times_hello_emitted, 0)

    def test_listener_reusability(self):
        times_hello_emitted = 0

        em1 = events.EventEmitter()
        em2 = events.EventEmitter()

        def hello():
            nonlocal times_hello_emitted
            times_hello_emitted += 1

        em1.once("hello", hello)
        em2.on("hello", hello)

        em1.emit("hello")
        self.assertEqual(times_hello_emitted, 1)
        em2.emit("hello")
        self.assertEqual(times_hello_emitted, 2)
        em1.emit("hello")
        self.assertEqual(times_hello_emitted, 2)
        em2.emit("hello")
        self.assertEqual(times_hello_emitted, 3)


if __name__ == "__main__":
    test.main()
