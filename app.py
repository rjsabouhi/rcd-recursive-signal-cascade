
import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Recursive Signal Cascade", layout="wide")
st.title("🔁 Recursive Signal Cascade")
st.markdown("""
This tool models how symbolic signals (ideas, traumas, concepts) recursively cascade through identity layers. 
Use the controls to simulate amplification, damping, and collapse behavior of signal trajectories.
""")

# Sidebar input controls
st.sidebar.header("Signal Parameters")
num_layers = st.sidebar.slider("Recursive Depth (Layers)", 3, 20, 10)
initial_amplitude = st.sidebar.slider("Initial Signal Strength", 0.1, 5.0, 1.0)
damping_factor = st.sidebar.slider("Damping Coefficient", 0.0, 1.0, 0.1)
feedback_gain = st.sidebar.slider("Recursive Feedback Gain", 0.0, 2.0, 1.0)
noise_level = st.sidebar.slider("Symbolic Noise", 0.0, 0.5, 0.1)

# Simulate the cascade
signal = [initial_amplitude]
for i in range(1, num_layers):
    prev = signal[-1]
    noise = np.random.normal(0, noise_level)
    new = feedback_gain * prev * (1 - damping_factor) + noise
    signal.append(new)

# Display results
layers = list(range(1, num_layers + 1))
fig = px.line(x=layers, y=signal, labels={"x": "Layer", "y": "Signal Strength"},
              title="Recursive Signal Strength Across Identity Layers")
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Interpretation")
st.markdown("""
This cascade simulates how an initial symbolic signal evolves as it passes recursively through identity filters.
- **Damping** reduces signal persistence.
- **Feedback Gain** amplifies self-reinforcing loops.
- **Noise** introduces instability or mutation.

Use this to explore conditions for signal amplification, dissipation, or symbolic overload.
""")
