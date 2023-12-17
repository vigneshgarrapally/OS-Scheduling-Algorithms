"""
Adaptive Priority Scheduling Algorithm (APSA)
"""

__all__ = ["apsa"]


def apsa(
    arrival_times,
    burst_times,
    WAITING_TIME_FACTOR,
    ARRIVAL_TIME_FACTOR,
    print_results=False,
):
    """
    Implements the Adaptive Priority Scheduling Algorithm (APSA).

    Args:
        arrival_times (list): List of arrival times for each process.
        burst_times (list): List of burst times for each process.
        WAITING_TIME_FACTOR (float): Factor to determine the waiting time boost for processes.
        ARRIVAL_TIME_FACTOR (float): Factor to determine the arrival time boost for processes.
        print_results (bool, optional): Flag to print the results. Defaults to False.

    Returns:
        tuple: A tuple containing the waiting times and turnaround times for each process.
    """
    num_processes = len(arrival_times)
    waiting_times = [0] * num_processes
    turnaround_times = [0] * num_processes
    priorities = [1 / (burst + arrival_times[i]) for i, burst in enumerate(burst_times)]
    completed = [False] * num_processes
    time = 0
    queue = []

    while not all(completed):
        # Add processes to the queue based on arrival time
        queue.extend(
            [
                i
                for i, arrival in enumerate(arrival_times)
                if arrival <= time and not completed[i] and i not in queue
            ]
        )

        # Recalculate priorities for waiting processes
        for i in queue:
            if not completed[i]:
                waiting_times[i] = time - arrival_times[i]
                # Boost priority for processes that have been waiting too long
                waiting_boost = max(waiting_times[i] * WAITING_TIME_FACTOR, 1)
                priorities[i] = (
                    1 / (burst_times[i] + arrival_times[i] / ARRIVAL_TIME_FACTOR)
                    + waiting_boost
                )

        # Select process with highest priority
        if queue:
            current_process = max(queue, key=lambda i: priorities[i])
            queue.remove(current_process)

            # Process execution simulation for one time unit
            burst_times[current_process] -= 1
            time += 1

            # Check if the process is completed
            if burst_times[current_process] <= 0:
                completed[current_process] = True
                turnaround_times[current_process] = (
                    time - arrival_times[current_process]
                )

        else:
            time += 1
    if print_results:
        print("Adaptive Priority Scheduling Algorithm (APSA):")
        print("WAITING_TIME_FACTOR:", WAITING_TIME_FACTOR)
        print("ARRIVAL_TIME_FACTOR:", ARRIVAL_TIME_FACTOR)
        print("Process\tArrival\tBurst\tWaiting\tTurnaround")
        for i in range(num_processes):
            print(
                f"{i+1}\t{arrival_times[i]}\t{burst_times[i]}\t{waiting_times[i]}\t{turnaround_times[i]}"
            )
        print("Average Waiting Time:", sum(waiting_times) / num_processes)
        print("Average Turnaround Time:", sum(turnaround_times) / num_processes)

    return waiting_times, turnaround_times


if __name__ == "__main__":
    arrival_times = [0, 1, 3, 4, 7]
    service_times = [10, 2, 5, 9, 7]
    WAITING_TIME_FACTOR = 0.5
    ARRIVAL_TIME_FACTOR = 10
    apsa(
        arrival_times,
        service_times,
        WAITING_TIME_FACTOR,
        ARRIVAL_TIME_FACTOR,
        print_results=True,
    )
