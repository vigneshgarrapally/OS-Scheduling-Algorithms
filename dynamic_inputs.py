from algorithms.fcfs import fcfs
from algorithms.hrrn import hrrn
from algorithms.srt import srt
from algorithms.spn import spn
from algorithms.rr import round_robin
from algorithms.mfq import mlfq as mfq
from algorithms.custom import apsa


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                raise ValueError("The number must be positive.")
            return value
        except ValueError as ve:
            print(f"Invalid input: {ve}")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                raise ValueError("The number must be positive.")
            return value
        except ValueError as ve:
            print(f"Invalid input: {ve}")


def get_input(prompt, count):
    while True:
        try:
            values = list(map(int, input(prompt).strip().split()))
            if len(values) != count:
                raise ValueError(f"Exactly {count} numbers are required.")
            if any(v < 0 for v in values):
                raise ValueError("Negative numbers are not allowed.")
            return values
        except ValueError as ve:
            print(f"Invalid input: {ve}")


def run_algorithm(algo, name, num_processes, is_rr=False, is_mfq=False):
    arrival_times = get_input(
        "Enter the processes' arrival times separated by space: ", num_processes
    )
    service_times = get_input(
        "Enter the processes' service times separated by space: ", num_processes
    )

    if is_rr:
        time_quantum = get_positive_int("Enter time quantum for Round Robin: ")
        algo(arrival_times, service_times, time_quantum, print_results=True)
    elif is_mfq:
        t1 = get_positive_int("Enter time quantum t1 for MLFQ: ")
        t2 = get_positive_int("Enter time quantum t2 for MLFQ: ")
        algo(arrival_times, service_times, t1, t2, print_results=True)
    elif "APSA" in name:
        waiting_time_factor = get_positive_float(
            "Enter the waiting time factor for APSA: "
        )
        arrival_time_factor = get_positive_int(
            "Enter the arrival time factor for APSA: "
        )
        algo(
            arrival_times,
            service_times,
            waiting_time_factor,
            arrival_time_factor,
            print_results=True,
        )
    else:
        algo(arrival_times, service_times, print_results=True)


def select_algorithm():
    algorithms = {
        "1": ("First-Come-First-Served (FCFS)", fcfs, False, False),
        "2": ("Round Robin (RR)", round_robin, True, False),
        "3": ("Shortest Process Next (SPN)", spn, False, False),
        "4": ("Shortest Remaining Time (SRT)", srt, False, False),
        "5": ("Highest Response Ratio Next (HRRN)", hrrn, False, False),
        "6": ("Multilevel Feedback Queue (MLFQ)", mfq, False, True),
        "7": ("Adaptive Priority Scheduling Algorithm (APSA)", apsa, False, False),
    }

    while True:
        print("\nSelect the scheduling algorithm to run:")
        for key, (name, _, _, _) in algorithms.items():
            print(f"{key}. {name}")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "0":
            break

        if choice in algorithms:
            name, algo, is_rr, is_mfq = algorithms[choice]
            print(f"\n{name}:")
            num_processes = get_positive_int("Enter the number of processes: ")
            run_algorithm(algo, name, num_processes, is_rr, is_mfq)
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    select_algorithm()
