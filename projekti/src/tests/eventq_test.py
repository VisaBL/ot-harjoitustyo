import unittest
import pygame
from event_queue import Eventqueue


class Test(unittest.TestCase):
    def setUp(self):
        self.eventqueue = Eventqueue(40)
        e2 = pygame.event.Event(pygame.KEYDOWN, key=275)
        e3 = pygame.event.Event(pygame.KEYDOWN, key=273)
        e4 = pygame.event.Event(pygame.KEYDOWN, key=276)
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
        eventqueue = [pygame.event.Event(
            pygame.KEYDOWN, key=276, scancode=116, mod=0)]
        self.eventqueue.get_event(self.event_list)
        state = isinstance(self.eventqueue.return_event(), tuple)
        self.assertEqual(True, state)

    def test_event_queue_pops_returns_right_event(self):
        eventqueue = [pygame.event.Event(
            pygame.KEYDOWN, key=274, scancode=116, mod=0)]
        event = self.eventqueue.get_event(self.event_list)
        self.assertEqual(True, event)
