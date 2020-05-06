
from collections import deque
from random import random
from math import log
#import linkedlist
from linkedlist import *

ARRIVAL = 0
DEPARTURE = 1

def exponential_random(var):
	u = random()
	return (-1/var)* log(1-u)

class Event:
	# default constructor
	def __init__(self, cur_time, service_time, event_type):
		self.service_time = service_time
		self.event_type = event_type
		self.event_time = cur_time

class SingleServerQueue:
	# default constructor
	def __init__(self, lam, MAXBUFFER):
		self.MAXBUFFER         = MAXBUFFER
		self.sum_queue_length  = 0
		self.mean_queue_length = 0
		self.server_busy_time  = 0
		self.mean_server_util  = 0
		self.mu 		       = 1
		self.lam  			   = lam
		self.time   	       = exponential_random(lam)
		self.packets_dropped   = 0
		self.gel = LinkedList()
		self.gel.head = Node(Event(self.time, exponential_random(self.mu), ARRIVAL))
		self.buffer = deque(maxlen = MAXBUFFER)

	def add_to_gel(self, event):
		if (gel.is_empty):
			gel.add_first(Node(event))
		elif (gel.tail.data.event_time <= event.event_time):
			gel.add_last(Node(event))
		else:
			for e in iter(gel):
				if (e.data.event_time > event.event_time):
					gel.add_before(e.data, Node(event))

	def process_arrival(self, event):
		self.time = event.event_time
		next_arrival_time = self.time + exponential_random(self.lam)
		next_service_time = exponential_random(self.mu)
		next_arrival_event = Event(next_arrival_time, next_service_time, ARRIVAL)
		self.add_to_gel(next_arrival_event)

		if (len(buffer) == 0):
			departure_event = Event(self.time + event.service_time, event.service_time, DEPARTURE)
			self.add_to_gel(departure_event)
		else:
			++server_busy_time
			if (len(self.buffer) == MAXBUFFER):
				++packets_dropped # the queue is full and therefore the packet is dropped
			else:
				self.buffer.append(event)

				self.sum_queue_length += len(self.buffer)
				self.mean_queue_length = sum_queue_length / self.time
				self.mean_server_util = server_busy_time / self.time

	def process_departure(self, event):
		self.time = event.event_time
		self.mean_queue_length = self.sum_queue_length / self.time
		self.mean_server_util = self.server_busy_time / self.time

		if (len(self.buffer) > 0):

			departure_event = self.buffer.popLeft()
			departure_event.event_time = self.time + departure_event.service_time
			departure_event.event_type = DEPARTURE

			self.add_to_gel(departure_event)

			self.sum_queue_length += len(self.buffer)
			self.mean_queue_length = self.sum_queue_length / self.time

# main functions
server = SingleServerQueue(0.2, 1)
for i in range(100000):
	nextEvent = server.gel.head.data
	server.gel.remove_node(nextEvent)
	# same are transmission time for an event or size for a baguette
	if (nextEvent.event_type == ARRIVAL):
		server.process_arrival(nextEvent)
	else:
		server.process_departure(nextEvent)

		print(server.mean_queue_length)
		print(server.mean_server_util)
		print(server.packets_dropped)
