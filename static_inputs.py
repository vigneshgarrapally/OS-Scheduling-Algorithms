"""
This file contains static inputs for testing the algorithms which covers the
basic requirements of the project.
"""

from algorithms.fcfs import fcfs
from algorithms.hrrn import hrrn
from algorithms.srt import srt
from algorithms.spn import spn
from algorithms.rr import round_robin
from algorithms.mfq import mlfq as mfq
from algorithms.custom import apsa

# define static inputs
arrival_times = [0, 1, 3, 4, 7]
service_times = [10, 2, 5, 9, 7]

# time quanta for some algorithms
time_quanta = 7

# now call all of the  algorithms with print_results=True
fcfs(arrival_times, service_times, print_results=True)
print("\n")
round_robin(arrival_times, service_times, time_quanta, print_results=True)
print("\n")
spn(arrival_times, service_times, print_results=True)
print("\n")
srt(arrival_times, service_times, print_results=True)
print("\n")
hrrn(arrival_times, service_times, print_results=True)
print("\n")
mfq(arrival_times, service_times, 8, 16, print_results=True)
print("\n")
apsa(arrival_times, service_times, 0.5, 10, print_results=True)
