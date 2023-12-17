"""
Multi-Level Feedback Queue Scheduling
Input: Arrival times, service times, time quantum for first queue, time quantum for second queue
Output: Waiting times, turnaround times
"""

from queue import Queue

__all__ = ["mlfq"]


class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.completed = False
        self.priority = None


def get_process_by_pid(processes, pid):
    for process in processes:
        if process.pid == pid:
            return process
    return None


def mlfq(arrival_times, service_times, t1, t2, print_results=False):
    """
    Implements the Multi-Level Feedback Queue (MLFQ) scheduling algorithm.

    Args:
        arrival_times (list): List of arrival times for each process.
        service_times (list): List of service times for each process.
        t1 (int): Time quantum for the first queue.
        t2 (int): Time quantum for the second queue.
        print_results (bool, optional): Whether to print the scheduling results. Defaults to False.

    Returns:
        tuple: A tuple containing the waiting times and turnaround times for each process.
    """
    n = len(arrival_times)
    processes = [Process(i, arrival_times[i], service_times[i]) for i in range(n)]
    queues = [Queue() for _ in range(3)]
    time_quantum = [t1, t2, float("inf")]
    current_time = 0
    current_process = None
    gantt_chart = []

    while any(p.remaining_time > 0 for p in processes):
        for process in processes:
            if (
                process.arrival_time <= current_time
                and not process.completed
                and process.priority is None
            ):
                queues[0].put(process.pid)
                process.priority = 0

        for i in range(len(queues)):
            if not queues[i].empty() and (
                current_process is None or i < current_process.priority
            ):
                if current_process:
                    queues[current_process.priority].put(current_process.pid)
                pid = queues[i].get()
                current_process = get_process_by_pid(processes, pid)
                break

        if current_process:
            current_process.remaining_time -= 1
            time_quantum[current_process.priority] -= 1

            if current_process.remaining_time == 0:
                current_process.waiting_time = (
                    current_time
                    - current_process.arrival_time
                    - current_process.burst_time
                    + 1
                )
                current_process.completed = True
                current_process = None
            elif time_quantum[current_process.priority] == 0:
                if current_process.priority < 2:
                    queues[current_process.priority + 1].put(current_process.pid)
                    current_process.priority += 1
                current_process = None
                time_quantum = [8, 16, float("inf")]

        current_time += 1

    if print_results:
        print("Multi-Level Feedback Queue Scheduling")
        print("First Queue: Time Quantum = 8")
        print("Second Queue: Time Quantum = 16")
        print("Third Queue: FCFS")
        print("Process\tArrival Time\tService Time\tWaiting Time\tTurnaround Time")
        for i in range(n):
            print(
                f"{i + 1}\t\t{arrival_times[i]}\t\t{service_times[i]}\t\t{processes[i].waiting_time}\t\t{processes[i].waiting_time + service_times[i]}"
            )
    waiting_times = [p.waiting_time for p in processes]
    turnaround_times = [p.waiting_time + p.burst_time for p in processes]
    print(f"\nAverage Waiting Time: {sum(waiting_times) / n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_times) / n:.2f}")
    return waiting_times, turnaround_times


if __name__ == "__main__":
    # Test the function
    arrival_times = [0, 16, 20]
    service_times = [36, 20, 12]
    waiting_times = mlfq(arrival_times, service_times, 8, 16, print_results=True)
