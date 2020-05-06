
from collections import deque
from random import random
from math import log
#import linkedlist
from linkedlist import *

ARRIVAL = 0
DEPARTURE = 1

def exponential_random(var):
	u = random()
	return (-1.0/float(var)) * log(1.0-float(u))

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
		self.length = 0

	def add_to_gel(self, event):
		if (self.gel.is_empty):
			self.gel.add_first(Node(event))
		elif (self.gel.tail.data.event_time <= event.event_time):
			self.gel.add_last(Node(event))
		else:
			for e in iter(self.gel):
				if (e.data.event_time > event.event_time):
					self.gel.add_before(e.data, Node(event))

	def process_arrival(self, event):
		self.time = event.event_time
		next_arrival_time = self.time + exponential_random(self.lam)
		next_service_time = exponential_random(self.mu)
		next_arrival_event = Event(next_arrival_time, next_service_time, ARRIVAL)
		self.add_to_gel(next_arrival_event)

		if (len(self.buffer) == 0):
			self.length += 1
			departure_event = Event(self.time + event.service_time, event.service_time, DEPARTURE)
			self.add_to_gel(departure_event)
		else:
			if (self.length - 1 < MAXBUFFER):
				print("buffer is full")
				packets_dropped += 1 # the queue is full and therefore the packet is dropped
			else:
				server_busy_time += event.service_time
				print("buffer is not full")
				self.length += 1
				self.buffer.append(event)

		self.sum_queue_length += self.length
		self.mean_queue_length = float(sum_queue_length) / float(self.time)
		self.server_busy_time += event.service_time
		self.mean_server_util = float(server_busy_time) / float(self.time)

	def process_departure(self, event):
		self.time = event.event_time
		self.mean_queue_length = float(self.sum_queue_length) / float(self.time)
		self.mean_server_util = float(self.server_busy_time) / float(self.time)
		self.length -= 1

		if (len(self.buffer) > 0):

			departure_event = self.buffer.popLeft()
			departure_event.event_time = self.time +  departure_event.service_time
			departure_event.event_type = DEPARTURE

			self.add_to_gel(departure_event)

			self.sum_queue_length += len(self.buffer)
			self.mean_queue_length = float(self.sum_queue_length) / float(self.time)

# main functions
server = SingleServerQueue(0.0001, 1)

for i in range(10):
	nextEvent = server.gel.head.data
	server.gel.remove_node(server.gel.head.data)
	# same as transmission time for an event or size for a packet
	if (nextEvent.event_type == ARRIVAL):
		server.process_arrival(nextEvent)
	else:
		server.process_departure(nextEvent)

print(server.server_busy_time)
print(server.mean_queue_length)
print(server.mean_server_util)
print(server.packets_dropped)
