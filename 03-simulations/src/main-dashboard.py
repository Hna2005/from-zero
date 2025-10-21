import streamlit as st
from birthday_problem import probability
from monty_hall import switch, not_switch

# --- Page Title ---
st.title("Simulation Dashboard")

# --- Birthday Problem ---
st.header("Birthday Problem Simulation")

num_trials_birthday = st.slider(
    "Number of simulation trials (Birthday Problem):",
    1_000, 100_000, 10_000, step=1_000,
    key="birthday_trials"
)

group_size = st.number_input(
    "Group size (number of people):",
    min_value=2, max_value=100, value=23,
    key="birthday_group_size"
)

# Compute probability
estimated_prob = probability(group_size, num_trials_birthday)

# Display results
st.subheader("Results")
st.write(f"Simulating for a group of **{group_size}** people...")
st.write(f"Estimated probability of a shared birthday: **{estimated_prob:.2%}**")

# --- Monty Hall Problem ---
st.header("Monty Hall Simulation")

num_trials_monty = st.slider(
    "Number of simulation trials (Monty Hall):",
    1_000, 100_000, 10_000, step=1_000,
    key="monty_trials"
)

# Use checkbox instead of toggle
active_switch = st.toggle("Switch doors")

# Run simulation
if active_switch:
    wins = switch(num_trials_monty)
    st.write(f"Running {num_trials_monty:,} simulations with switching...")
    st.write(f"Wins with switching: {wins} ({(wins / num_trials_monty):.2%})")
else:
    wins = not_switch(num_trials_monty)
    st.write(f"Running {num_trials_monty:,} simulations without switching...")
    st.write(f"Wins without switching: {wins} ({(wins / num_trials_monty):.2%})")
