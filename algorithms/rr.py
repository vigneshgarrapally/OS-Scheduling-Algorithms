"""
Round Robin Scheduling Algorithm
"""

__all__ = ["round_robin"]


def round_robin(arrival_times, service_times, quantum, print_results=False):
    """
    Round Robin Scheduling Algorithm

    Parameters:
    arrival_times (list): List of arrival times of processes.
    service_times (list): List of service (burst) times of processes.
    quantum (int): Time quantum for the round-robin scheduling.
    print_results (bool): If True, prints the scheduling details.

    Returns:
    waiting_times (list): List of waiting times for each process.
    turnaround_times (list): List of turnaround times for each process.
    """
    n = len(arrival_times)
    remaining_times = list(service_times)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    t = 0  # Current time

    while True:
        done = True
        for i in range(n):
            if remaining_times[i] > 0:
                done = False
                if remaining_times[i] > quantum:
                    t += quantum
                    remaining_times[i] -= quantum
                else:
                    t += remaining_times[i]
                    waiting_times[i] = t - service_times[i] - arrival_times[i]
                    remaining_times[i] = 0

        if done:
            break

    for i in range(n):
        turnaround_times[i] = service_times[i] + waiting_times[i]

    if print_results:
        print("Round Robin Scheduling")
        print(f"Time Quantum: {quantum}")
        print("Process\tArrival\tService\tWaiting\tTurnaround")
        for i in range(n):
            print(
                f"{i+1}\t{arrival_times[i]}\t{service_times[i]}\t{waiting_times[i]}\t{turnaround_times[i]}"
            )

        print(f"Average Waiting Time: {sum(waiting_times)/n}")
        print(f"Average Turnaround Time: {sum(turnaround_times)/n}")

    return waiting_times, turnaround_times


if __name__ == "__main__":
    arrival_times = [0, 1, 3, 4, 7]
    service_times = [10, 2, 5, 9, 7]
    time_quantum = 7
    round_robin(arrival_times, service_times, time_quantum, print_results=True)
