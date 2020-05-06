
from collections import deque
from random import random
from math import log
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
		self.mu 		       = 1
		self.lam  			   = lam
		self.time   	       = exponential_random(lam)
		self.packets_dropped   = 0
		self.gel 			   = LinkedList()
		self.gel.head          = Node(Event(self.time, exponential_random(self.mu), ARRIVAL))
		self.buffer 		   = deque(maxlen = MAXBUFFER)
		self.length 		   = 0
		self.server_busy_time  = self.gel.head.data.service_time

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
		self.server_busy_time += next_service_time
		self.add_to_gel(next_arrival_event)

		if (len(self.buffer) == 0):
			self.length += 1
			departure_event = Event(self.time + event.service_time, event.service_time, DEPARTURE)
			self.add_to_gel(departure_event)
		else:
			if (self.length - 1 < MAXBUFFER):
				print("buffer is full")
				self.length += 1
				self.buffer.append(event)
			else:
				print("buffer full")
				packets_dropped += 1 # the queue is full and therefore the packet is dropped

	def process_departure(self, event):
		self.time = event.event_time
		self.length -= 1

		if (self.length > 0):

			departure_event = self.buffer.popLeft()
			departure_event.event_time = self.time + departure_event.service_time
			departure_event.service_time = 0
			departure_event.event_type = DEPARTURE

			self.add_to_gel(departure_event)

# main functions
server            = SingleServerQueue(0.02, 20)
sum_time          = 0
mean_queue_length = 0
mean_server_util  = 0

for i in range(10):
	nextEvent = server.gel.head.data
	server.gel.remove_node(server.gel.head.data)

	if (i != 0):
		mean_queue_length += server.length * (server.time - sum_time)
	# same as transmission time for an event or size for a packet
	if (nextEvent.event_type == ARRIVAL):
		server.process_arrival(nextEvent)
	else:
		server.process_departure(nextEvent)

	sum_time = nextEvent.event_time

mean_server_util = (float)(server.server_busy_time)/(float)(server.time)

#print(server.server_busy_time)
print(mean_queue_length)
print(mean_server_util * 100.0)
print(server.packets_dropped)
