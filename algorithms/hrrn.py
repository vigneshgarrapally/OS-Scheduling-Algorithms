"""
Highest Response Ratio Next (HRRN) Scheduling Algorithm
"""

__all__ = ["hrrn"]


def hrrn(arrival_times, service_times, print_results=False):
    """
    Highest Response Ratio Next (HRRN) Scheduling Algorithm

    This function implements the Highest Response Ratio Next (HRRN) scheduling algorithm.
    It schedules the processes based on their response ratio, which is calculated as the ratio
    of the sum of the waiting time and the service time to the service time.

    Parameters:
    - arrival_times: List of arrival times for each process.
    - service_times: List of service (burst) times for each process.
    - print_results: Boolean value indicating whether to print the process details in table format.

    Returns:
    - waiting_times: List of waiting times for each process.
    - turnaround_times: List of turnaround times for each process.
    """
    n = len(arrival_times)
    waiting_times = [0] * n
    finish_times = [0] * n
    start_times = [0] * n
    remaining_times = list(service_times)
    time = 0
    processes = set(range(n))

    while processes:
        available_processes = [
            (i, ((time - arrival_times[i]) + service_times[i]) / service_times[i])
            for i in processes
            if arrival_times[i] <= time
        ]
        if not available_processes:
            time += 1
            continue

        # Process with the highest response ratio
        next_process = max(available_processes, key=lambda x: x[1])[0]
        processes.remove(next_process)
        waiting_times[next_process] = time - arrival_times[next_process]
        time += service_times[next_process]
        finish_times[next_process] = time
        start_times[next_process] = (
            waiting_times[next_process] + arrival_times[next_process]
        )

    turnaround_times = [service_times[i] + waiting_times[i] for i in range(n)]

    if print_results:
        print("Highest Response Ratio Next (HRRN) Scheduling Algorithm")
        print(
            "Process\tArrival Time\tService Time\tWaiting Time\tStart Time\tTurnaround Time"
        )
        for i in range(n):
            print(
                f"{i + 1}\t\t{arrival_times[i]}\t\t{service_times[i]}\t\t{waiting_times[i]}\t\t{start_times[i]}\t\t{turnaround_times[i]}"
            )
        print(f"\nAverage Waiting Time: {sum(waiting_times) / n:.2f}")
        print(f"Average Turnaround Time: {sum(turnaround_times) / n:.2f}")

    return waiting_times, turnaround_times


if __name__ == "__main__":
    arrival_times = [0, 1, 3, 4, 7]
    service_times = [10, 2, 5, 9, 7]
    hrrn(arrival_times, service_times, print_results=True)
