"""
Shortest Remaining Time (SRT) Scheduling Algorithm
"""

__all__ = ["srt"]


def srt(arrival_times, service_times, print_results=False):
    """
    Shortest Remaining Time (SRT) Scheduling Algorithm
    Parameters:
    - arrival_times: List of arrival times
    - service_times: List of service (burst) times
    - print_results: Boolean, if True, print the process details in table format

    Returns:
    - waiting_times: List of waiting times for each process
    - turnaround_times: List of turnaround times for each process
    """
    n = len(arrival_times)
    waiting_times = [0] * n
    finish_times = [0] * n
    remaining_times = list(service_times)
    time = 0
    completed = 0

    while completed != n:
        # Find process with minimum remaining time
        shortest = min(
            [
                i
                for i in range(n)
                if arrival_times[i] <= time and remaining_times[i] > 0
            ],
            key=lambda x: remaining_times[x],
            default=-1,
        )

        if shortest == -1:
            time += 1
            continue

        remaining_times[shortest] -= 1
        time += 1

        if remaining_times[shortest] == 0:
            completed += 1
            finish_times[shortest] = time
            waiting_times[shortest] = (
                finish_times[shortest]
                - arrival_times[shortest]
                - service_times[shortest]
            )

    turnaround_times = [finish_times[i] - arrival_times[i] for i in range(n)]

    if print_results:
        print("\nShortest Remaining Time (SRT) Scheduling Algorithm")
        print("Process\tArrival Time\tService Time\tWaiting Time\tTurnaround Time")
        for i in range(n):
            print(
                f"{i + 1}\t\t{arrival_times[i]}\t\t{service_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}"
            )
        print(f"\nAverage Waiting Time: {sum(waiting_times) / n:.2f}")
        print(f"Average Turnaround Time: {sum(turnaround_times) / n:.2f}")

    return waiting_times, turnaround_times


if __name__ == "__main__":
    arrival_times = [0, 1, 3, 4, 7]
    service_times = [10, 2, 5, 9, 7]
    srt(arrival_times, service_times, print_results=True)
