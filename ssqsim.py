
from collections import deque
from random import random
from math import log
#import linkedlist
from linkedlist import *

ARRIVAL = 0
DEPARTURE = 1

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
		self.time   	       = self.exponential_random(lam)
		self.packets_dropped   = 0
		self.gel = LinkedList()
		self.gel.head = Node(Event(self.time, ARRIVAL))
		self.buffer = deque(maxlen = MAXBUFFER)

	@staticmethod
	def exponential_random(var):
		u = random()
		return (-1/var)* log(1-u)

	def add_to_gel(event):
		if (gel.is_empty):
			gel.add_first(Node(event))
		elif (gel.tail.data.event_time <= event.event_time):
			gel.add_last(Node(event))
		else:
			for e in iter(gel):
				if (e.data.event_time > event.event_time):
					gel.add_before(e.data, Node(event))

	def process_arrival(event):
		time = event.event_time
		next_arrival_time = time + exponential_random(self.lam)
		next_service_time = exponential_random(self.mu)
		next_arrival_event = Event(next_arrival_time, next_service_time, ARRIVAL)
		add_to_gel(new_arrival_event)

		if (len(buffer) == 0):
			departure_event = Event(time + service_time, service_time, DEPARTURE)
			add_to_gel(departure_event)
		else:
			++server_busy_time
			if (len(buffer) == MAXBUFFER):
				++packets_dropped # the queue is full and therefore the packet is dropped
			else:
				buffer.append(event)

				sum_queue_length += len(buffer)
				mean_queue_length = sum_queue_length / time
				mean_server_util = server_busy_time / time

	def process_departure(event):
		time = event.event_time
		mean_queue_length = sum_queue_length / time
		mean_server_util = server_busy_time / time

		if (len(buffer) > 0):

			departure_event = buffer.popLeft()
			departure_event.event_time = time + departure_event.service_time
			departure_event.event_type = DEPARTURE

			add_to_gel(departure_event)

			sum_queue_length += len(buffer)
			mean_queue_length = sum_queue_length / time

# main functions
server = SingleServerQueue(0.2, 1)
for i in 100000:
	nextEvent = server.gel.remove_node(server.gel.head.data)
	# same are transmission time for an event or size for a baguette
	if (nextEvent.event_time == ARRIVAL):
		process_arrival(nextEvent)
	else:
		process_departure(nextEvent)

		print(server.mean_queue_length)
		print(server.mean_server_util)
		print(server.packets_dropped)
