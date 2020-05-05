
from collections import deque
from enum import Enum
import linkedlist

ARRIVAL = 0
DEPARTURE = 1

class Event:
	# these are variables
	event_time # For an arrival event it is the time the packet arrives at the transmitter and for a departure event it is the time when the server is finished transmitting the packet.
	event_type # arrival or departure
	next_event # ptr to next event
	prev_event # ptr to prev event

	# this is a constructor
	def __init__(self):
		printf("hi")



class SingleServerQueue:
	"""d main class"""

	MAXBUFFER
	length
	time
	service_rate
	arrival_rate

	gel = deque()
	buffer = deque()

	# default constructor
	def __init__(self, service_rate, arrival_rate):
		super(SingleServerQueue, self).__init__()
		self.length 	  = 0
		self.time   	  = 0
		self.service_rate = service_rate
		self.arrival_rate = arrival_rate


	def clock(arg):
		for i in 100000:
			firstEvent = gel.popLeft()
			if (firstEvent.event_time == ARRIVAL):
				#process arival_Event
			else:
				#process service_completion
				print ("hey")


	def processArrival(arg):
		curr_time = event_time
		if ()
