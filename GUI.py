import streamlit as st
import pandas as pd
from algorithms.fcfs import fcfs
from algorithms.hrrn import hrrn
from algorithms.srt import srt
from algorithms.spn import spn
from algorithms.rr import round_robin
from algorithms.mfq import mlfq as mfq
from algorithms.custom import apsa


def run_algorithm(
    algo_func,
    arrival_times,
    service_times,
    time_quantum=None,
    waiting_time_factor=None,
    arrival_time_factor=None,
    time_quantum2=None,
):
    service_times1 = service_times.copy()
    arrival_times1 = arrival_times.copy()
    if time_quantum and not time_quantum2:
        waiting_times, turnaround_times = algo_func(
            arrival_times, service_times, time_quantum, print_results=False
        )
    elif time_quantum2:
        waiting_times, turnaround_times = algo_func(
            arrival_times,
            service_times,
            time_quantum,
            time_quantum2,
            print_results=False,
        )
    elif waiting_time_factor and arrival_time_factor:
        waiting_times, turnaround_times = algo_func(
            arrival_times,
            service_times,
            waiting_time_factor,
            arrival_time_factor,
            print_results=False,
        )
    else:
        waiting_times, turnaround_times = algo_func(
            arrival_times, service_times, print_results=False
        )

    # Constructing the table
    process_ids = list(range(1, len(arrival_times) + 1))
    data = {
        "Process": process_ids,
        "Arrival Time": arrival_times1,
        "Service Time": service_times1,
        "Waiting Time": waiting_times,
        "Turnaround Time": turnaround_times,
    }
    df = pd.DataFrame(data)
    st.table(df)

    # Calculate and display averages
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    st.write(f"Average Waiting Time: {avg_waiting_time:.2f}")
    st.write(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


def main():
    st.title("Scheduling Algorithm Simulator")

    # Selection of the algorithm
    algorithm = st.selectbox(
        "Select the scheduling algorithm:",
        ("FCFS", "Round Robin", "SPN", "SRT", "HRRN", "MFQ", "APSA"),
    )

    # Input for processes
    num_processes = st.number_input(
        "Enter the number of processes:",
        min_value=1,
        value=1,
        step=1,
        key="num_processes",
    )

    # Use a form for batch input submission
    form = st.form(key="processes_form")
    arrival_times = []
    service_times = []
    for i in range(num_processes):
        cols = form.columns(2)
        with cols[0]:
            arrival_time = st.number_input(
                f"Process {i+1} - Arrival Time:", min_value=0, key=f"arrival_{i}"
            )
        with cols[1]:
            service_time = st.number_input(
                f"Process {i+1} - Service Time:", min_value=0, key=f"service_{i}"
            )
        arrival_times.append(arrival_time)
        service_times.append(service_time)

    # Conditional input for time quantum if Round Robin or MFQ is selected
    time_quantum = None
    if algorithm in ["Round Robin", "MFQ"]:
        time_quantum = form.number_input(
            "Enter time quantum:", min_value=1, value=1, key="time_quantum"
        )
    time_quantum2 = None
    if algorithm == "MFQ":
        time_quantum2 = form.number_input(
            "Enter time quantum for second queue:",
            min_value=1,
            value=1,
            key="time_quantum2",
        )
    waiting_time_factor = None
    arrival_time_factor = None
    if algorithm == "APSA":
        waiting_time_factor = form.number_input(
            "Enter the waiting time factor for APSA: ",
            min_value=0.0,
            value=0.5,
            key="waiting_time_factor",
        )
        arrival_time_factor = form.number_input(
            "Enter the arrival time factor for APSA: ",
            min_value=0,
            value=10,
            key="arrival_time_factor",
        )
    submit_button = form.form_submit_button(label="Run {}".format(algorithm))

    if submit_button:
        algo_mapping = {
            "FCFS": fcfs,
            "Round Robin": round_robin,
            "SPN": spn,
            "SRT": srt,
            "HRRN": hrrn,
            "MFQ": mfq,
            "APSA": apsa,
        }

        # Call the corresponding algorithm function
        run_algorithm(
            algo_mapping[algorithm],
            arrival_times,
            service_times,
            time_quantum,
            waiting_time_factor,
            arrival_time_factor,
            time_quantum2,
        )


if __name__ == "__main__":
    main()
