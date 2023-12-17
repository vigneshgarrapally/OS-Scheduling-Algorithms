"""
Shortest Process Next (SPN) Scheduling Algorithm
"""

__all__ = ["spn"]


def spn(arrival_times, service_times, print_results=False):
    """
    Shortest Process Next (SPN) Scheduling Algorithm

    This function implements the Shortest Process Next (SPN) scheduling algorithm.
    It takes a list of arrival times and service times as input and returns the waiting times and turnaround times for each process.

    Parameters:
    - arrival_times: List of arrival times for each process.
    - service_times: List of service (burst) times for each process.
    - print_results: Boolean value indicating whether to print the process details and summary. Default is False.

    Returns:
    - waiting_times: List of waiting times for each process.
    - turnaround_times: List of turnaround times for each process.
    """
    n = len(arrival_times)
    waiting_times = [0] * n
    finish_times = [0] * n
    service_times_remaining = list(service_times)
    time = 0
    processes = set(range(n))

    while processes:
        available_processes = [i for i in processes if arrival_times[i] <= time]
        if not available_processes:
            time += 1
            continue

        shortest_process = min(
            available_processes, key=lambda i: service_times_remaining[i]
        )
        processes.remove(shortest_process)
        waiting_times[shortest_process] = time - arrival_times[shortest_process]
        time += service_times_remaining[shortest_process]
        finish_times[shortest_process] = time

    turnaround_times = [finish_times[i] - arrival_times[i] for i in range(n)]

    if print_results:
        print("Shortest Process Next Scheduling")
        print("Process\tArrival\tService\tWaiting\tTurnaround")
        for i in range(n):
            print(
                f"{i + 1}\t{arrival_times[i]}\t{service_times[i]}\t{waiting_times[i]}\t{turnaround_times[i]}"
            )
        print(f"\nAverage Waiting Time: {sum(waiting_times) / n:.2f}")
        print(f"Average Turnaround Time: {sum(turnaround_times) / n:.2f}")

    return waiting_times, turnaround_times


if __name__ == "__main__":
    arrival_times = [0, 1, 3, 4, 7]
    service_times = [10, 2, 5, 9, 7]
    spn(arrival_times, service_times, print_results=True)
