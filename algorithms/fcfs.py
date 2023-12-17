"""
First-Come-First-Served Scheduling Algorithm
"""


__all__ = ["fcfs"]


def fcfs(arrival_times, service_times, print_results=False):
    """
    First-Come-First-Served Scheduling Algorithm

    This function implements the First-Come-First-Served (FCFS) scheduling algorithm.
    It takes a list of arrival times and service times of processes as input and returns
    the waiting times and turnaround times of each process.

    Parameters:
    arrival_times (list): List of arrival times of processes.
    service_times (list): List of service (burst) times of processes.
    print_results (bool): If True, prints the scheduling details.

    Returns:
    waiting_times (list): List of waiting times of each process.
    turnaround_times (list): List of turnaround times of each process.
    """
    n = len(arrival_times)
    waiting_times = [0] * n
    turnaround_times = [0] * n
    start_time = 0

    for i in range(n):
        if start_time < arrival_times[i]:
            start_time = arrival_times[i]
        waiting_times[i] = start_time - arrival_times[i]
        start_time += service_times[i]
        turnaround_times[i] = waiting_times[i] + service_times[i]

    if print_results:
        print("First-Come-First-Served Scheduling")
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
    fcfs(arrival_times, service_times, print_results=True)
