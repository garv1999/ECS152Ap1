
from collections import deque
from numpy import random
import linkedlist

ARRIVAL = 0
DEPARTURE = 1

class Event:
	event_type # arrival or departure
	next_event
	prev_event

	# default constructor
	def __init__(self, cur_time, event_type):
		self.event_type = event_type
		self.event_time = cur_time
		self.service_time = service_time

class SingleServerQueue:
	"""d main class"""

	MAXBUFFER

	gel = LinkedList()
	buffer = deque()

	# default constructor
	def __init__(self, service_rate, arrival_rate):
		self.length 	  = 0 # number of packets in queue
		self.time   	  = 0 # current time
		self.service_rate = service_rate
		self.arrival_rate = arrival_rate
		self.mu 		  = 1 # gupti is d cutest beta in d world
		self.lam		  = # whatever the test whats us to do SO CUUUUUTE
		self.gel.add_first(Node(Event(time, ARRIVAL)))

    int def exponential_random(var):
    	# u = np.random.uniform(0,1)
		u = random()
		return exp_random = (-1/var)* math.log(1-u)

	def process_arrival(event, lam):
		arrival_time = exponential_random(lam)
		service_time = exponential_random(mu)

		if (length != 0)
			time = time + arrival_time
			new_event = Event(time, ARRIVAL) # creating a new event
			buffer.append(new_event)
			if (length - 1 < MAXBUFFER):
				buffer.append(new_event)
			else
				print("hey")
				#drop the packet

			# gel.add_last(Node(new_event)) # adding that event to the gel
		if (length == 0) :
			departure_event = Event("""need to fill this """, DEPARTURE)
			length++
			departure_event = event()

			# insert event into global event list
			for (e in gel)
				if (e.data.service_time >= event.service_time)
					gel.add_before(e, event)

server = SingleServerQueue()
	for i in 100000:
		firstEvent = gel.popLeft()
		if (firstEvent.event_time == ARRIVAL):
			#process arival_Event
		else:
			#process service_completion
			print ("hey")
