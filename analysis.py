import pandas as pd
import matplotlib.pyplot as plt
from algorithms.fcfs import fcfs
from algorithms.hrrn import hrrn
from algorithms.srt import srt
from algorithms.spn import spn
from algorithms.rr import round_robin
from algorithms.mfq import mlfq as mfq
from algorithms.custom import apsa

# Define the sample inputs
inputs = {
    "All Short Jobs": {
        "arrival_times": [0, 2, 4, 6, 8],
        "service_times": [2, 3, 2, 4, 1],
    },
    "Mixed Job Lengths": {
        "arrival_times": [0, 1, 3, 5, 7],
        "service_times": [1, 8, 2, 7, 3],
    },
    "Heavy Load": {
        "arrival_times": [0, 0, 0, 0, 0],
        "service_times": [10, 2, 8, 6, 4],
    },
    "Light Load With Sporadic Long Jobs": {
        "arrival_times": [0, 5, 10, 15, 20],
        "service_times": [1, 12, 1, 12, 1],
    },
    "Staggered Mix": {
        "arrival_times": [0, 3, 5, 8, 12],
        "service_times": [8, 2, 10, 1, 5],
    },
}

# Define the algorithms
algorithms = {
    "FCFS": fcfs,
    "Round Robin": round_robin,
    "SPN": spn,
    "SRT": srt,
    "HRRN": hrrn,
    "MFQ": mfq,
}

# Define a time quantum for those algorithms that need it
time_quantum1 = 4
time_quantum2 = 8

# Prepare the results table
results_data = {
    "Input Set": [],
    "Algorithm": [],
    "Average Turnaround Time": [],
    "Average Waiting Time": [],
}

# Run the algorithms for each input set and collect results
for input_name, data in inputs.items():
    for algo_name, algo_func in algorithms.items():
        if algo_name == "Round Robin":
            waiting_times, turnaround_times = algo_func(
                data["arrival_times"], data["service_times"], time_quantum1
            )
        elif algo_name == "MFQ":
            waiting_times, turnaround_times = algo_func(
                data["arrival_times"],
                data["service_times"],
                time_quantum1,
                time_quantum2,
            )
        elif algo_name == "APSA":
            waiting_times, turnaround_times = algo_func(
                data["arrival_times"], data["service_times"], 0.5, 10
            )
        else:
            waiting_times, turnaround_times = algo_func(
                data["arrival_times"], data["service_times"]
            )

        avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
        avg_waiting_time = sum(waiting_times) / len(waiting_times)

        results_data["Input Set"].append(input_name)
        results_data["Algorithm"].append(algo_name)
        results_data["Average Turnaround Time"].append(avg_turnaround_time)
        results_data["Average Waiting Time"].append(avg_waiting_time)

# Convert to DataFrame for easy tabular display
results_df = pd.DataFrame(results_data)
print(results_df)

# Plotting the results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
results_df.pivot(
    index="Algorithm", columns="Input Set", values="Average Turnaround Time"
).plot(kind="bar", ax=ax1)
ax1.set_title("Average Turnaround Time by Algorithm")
ax1.set_ylabel("Time Units")

results_df.pivot(
    index="Algorithm", columns="Input Set", values="Average Waiting Time"
).plot(kind="bar", ax=ax2)
ax2.set_title("Average Waiting Time by Algorithm")
ax2.set_ylabel("Time Units")

plt.tight_layout()
plt.show()
