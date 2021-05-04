import unittest
import pygame
from event_queue import Eventqueue


class Test(unittest.TestCase):
    def setUp(self):
        self.eventqueue = Eventqueue(40)
        e2 = pygame.event.Event(pygame.KEYDOWN, key="K_DOWN")
        e3 = pygame.event.Event(pygame.KEYDOWN, key="K_DOWN")
        e4 = pygame.event.Event(
            pygame.KEYDOWN, key="K_DOWN", scancode=116, mod=0)
        self.event_list = [e2, e3, e4]

    def test_event_queue_accepts_events_returns_true(self):
        state = self.eventqueue.get_event(self.event_list)
        self.assertEqual(True, state)

    def test_event_queue_returns_true_when_no_events(self):
        state = self.eventqueue.get_event(())
        self.assertEqual(True, state)

    def test_event_queue_returns_false_when_event_type_quit(self):
        state = self.eventqueue.get_event([pygame.event.Event(pygame.QUIT)])
        self.assertEqual(False, state)

# eventqueuen testi antaa vaihtelevia tuloksia suorituskerrasta riippuen täytyy testata mikä juttu?
# <Event(2-KeyDown {'unicode': '', 'key': 275, 'mod': 0, 'scancode': 114, 'window': None})>
    def test_event_queue_pops_returns_work(self):
        self.eventqueue.get_event(self.event_list)
        state = isinstance(self.eventqueue.return_event(), tuple)
        self.assertEqual(True, state)

    # Tämä testi testaa, että eventque ei palauta suoritettavaa tapahtumaa,
    # jotta mato ei käänny itseään vastaan

    def test_event_queue_pops_does_not_return_ongoing_event(self):
        event = pygame.event.Event(
            pygame.KEYDOWN, key=276, scancode=116, mod=0)
        eventqueue = [event, event, event]
        for _ in range(3):
            self.eventqueue.get_event(eventqueue)
        for _ in range(3):
            event = self.eventqueue.return_event()
        self.assertEqual(None, event)

    def test_event_queue_pops_return_right_event_LEFT(self):
        self.eventqueue.return_event()
        self.eventqueue.reset_queue()
        self.eventqueue.get_event(
            [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)])
        event = self.eventqueue.return_event()
        self.assertEqual('L', event[2])

    def test_event_queue_pops_return_right_event_RIGHT(self):
        self.eventqueue.return_event()
        self.eventqueue.reset_queue()
        self.eventqueue.get_event(
            [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)])
        event = self.eventqueue.return_event()
        self.assertEqual('R', event[2])

    def test_event_queue_pops_return_right_event_UP(self):
        self.eventqueue.return_event()
        self.eventqueue.reset_queue()
        self._previously_executed = None
        self.eventqueue.get_event(
            [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)])
        event = self.eventqueue.return_event()
        self.assertEqual('U', event[2])

    def test_event_queue_pops_return_right_event_DOWN(self):
        self.eventqueue.return_event()
        self.eventqueue.reset_queue()
        self.eventqueue.get_event(
            [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)])
        event = self.eventqueue.return_event()
        self.assertEqual('D', event[2])
