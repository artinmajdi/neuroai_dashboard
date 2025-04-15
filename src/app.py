import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from datetime import datetime, timedelta
import random
import os
import sys

# Add the current directory to the path so we can import the utils module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set page configuration
st.set_page_config(
    page_title="NeuroAI Dashboard: EEG Analysis with Attention Visualization",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 26px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 20px;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .highlight-text {
        color: #e74c3c;
        font-weight: bold;
    }
    .info-box {
        background-color: #f8f9fa;
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .patient-card {
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 10px;
    }
    .similar-case {
        background-color: #7f8c8d;
        color: white;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Page header
st.markdown("<div class='main-header'>NeuroAI Dashboard: EEG Analysis with Attention Visualization</div>", unsafe_allow_html=True)

# Sidebar for patient selection and controls
with st.sidebar:
    # Add a radio button for page selection
    page = st.radio("Navigation", ["EEG Dashboard", "Proposed Grants", "Slide Deck (Alignment/Proposed-Contributions)"])

    if page == "EEG Dashboard":
        st.markdown("### Patient Selection")
        patient_search = st.text_input("Search patients...")

        # Sample patient data
        st.markdown("<div class='patient-card'>Patient ID: 28791<br>Status: Post-seizure monitoring</div>", unsafe_allow_html=True)

        st.markdown("### Model Configuration")
        attention_layer = st.selectbox("Attention Visualization", ["Transformer Layer 1", "Transformer Layer 2", "Transformer Layer 3", "Transformer Layer 4"])
        time_window = st.selectbox("Time Window", ["Last 5 minutes", "Last 15 minutes", "Last 30 minutes", "Last 1 hour"])

        st.markdown("### Similar Cases")
        # Create sample similar cases
        similar_cases = [
            {"id": "17382", "similarity": "87%", "selected": True},
            {"id": "29104", "similarity": "72%", "selected": False},
            {"id": "15209", "similarity": "64%", "selected": False}
        ]

        for case in similar_cases:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"<div class='similar-case'>Case #{case['id']}<br>Similarity: {case['similarity']}</div>", unsafe_allow_html=True)
            with col2:
                case["selected"] = st.checkbox("View", value=case["selected"], key=f"case_{case['id']}")

        view_all = st.button("View All Similar Cases")

    elif page == "Proposed Grants":
        st.markdown("### Grant Proposals")
        grant_type = st.radio("Select Grant Type", ["NIH K99/R00", "NSF CAREER", "McKnight Scholars"])

        # Import the TSX renderer utility
        from utils.tsx_renderer import render_tsx_component

        # Render the appropriate TSX file based on selection
        if grant_type == "NIH K99/R00":
            tsx_path = os.path.join(os.path.dirname(__file__), "grants/k99r00-slide-deck.tsx")
            render_tsx_component(tsx_path)
        elif grant_type == "NSF CAREER":
            tsx_path = os.path.join(os.path.dirname(__file__), "grants/nsf-career-slide-deck.tsx")
            render_tsx_component(tsx_path)
        elif grant_type == "McKnight Scholars":
            tsx_path = os.path.join(os.path.dirname(__file__), "grants/mcknight-scholars-slide-deck.tsx")
            render_tsx_component(tsx_path)



# Function to generate synthetic EEG data
def generate_eeg_data(channels, seconds, sample_rate=250):
    """Generate synthetic EEG data for visualization"""
    time = np.arange(0, seconds, 1/sample_rate)
    eeg_data = {}

    base_freqs = {
        'Fp1': 10, 'Fp2': 11, 'F3': 9, 'F4': 10,
        'C3': 12, 'C4': 11, 'P3': 8, 'P4': 9,
        'O1': 10, 'O2': 11, 'T3': 9, 'T4': 10,
        'T5': 12, 'T6': 11
    }

    # Generate synthetic data for each channel
    for channel in channels:
        base_freq = base_freqs.get(channel, 10)  # Hz

        # Base signal (alpha wave)
        signal = np.sin(2 * np.pi * base_freq * time)

        # Add some beta
        signal += 0.3 * np.sin(2 * np.pi * (base_freq*2) * time)

        # Add some theta
        signal += 0.2 * np.sin(2 * np.pi * (base_freq/2) * time)

        # Add noise
        signal += 0.1 * np.random.randn(len(time))

        # Create abnormality in F3 channel between 15-20 seconds (spike and wave)
        if channel == 'F3' and seconds > 20:
            # Add spike-wave pattern
            spike_start = int(15 * sample_rate)
            spike_end = int(20 * sample_rate)

            for i in range(spike_start, spike_end, int(0.3 * sample_rate)):
                if i + int(0.05 * sample_rate) < len(signal):
                    signal[i:i+int(0.05*sample_rate)] = 2 * np.sin(2 * np.pi * 30 * time[0:int(0.05*sample_rate)])

                    # Fix for the shape mismatch error
                    wave_length = int(0.2*sample_rate) - int(0.05*sample_rate)
                    if i + int(0.2*sample_rate) <= len(signal) and wave_length <= len(time):
                        signal[i+int(0.05*sample_rate):i+int(0.2*sample_rate)] = -1 * np.sin(2 * np.pi * 3 * time[0:wave_length])

        eeg_data[channel] = signal

    return time, eeg_data

# Function to generate attention heatmap data
def generate_attention_data(channels, seconds, sample_rate=250):
    """Generate synthetic attention data"""
    # Number of time bins (5 per second)
    time_bins = int(seconds / 0.2)
    attention_data = np.zeros((len(channels), time_bins))

    # Create high attention area in F3
    f3_idx = channels.index('F3') if 'F3' in channels else 0
    f4_idx = channels.index('F4') if 'F4' in channels else 1

    # Add high attention to F3 in the abnormal region
    high_attn_start = int(15 / 0.2)
    high_attn_end = int(20 / 0.2)
    attention_data[f3_idx, high_attn_start:high_attn_end] = np.random.uniform(0.7, 0.9, high_attn_end-high_attn_start)

    # Add medium attention to F4 in the same region
    attention_data[f4_idx, high_attn_start:high_attn_end] = np.random.uniform(0.3, 0.5, high_attn_end-high_attn_start)

    # Add some random low attention
    for i in range(len(channels)):
        for j in range(time_bins):
            if attention_data[i, j] == 0:
                attention_data[i, j] = np.random.uniform(0, 0.3)

    return attention_data

# Main content based on selected page
if page == "EEG Dashboard":

    # Advanced options (collapsible)
    with st.expander("Advanced Analysis Options", expanded=True):
        col_adv1, col_adv2, col_adv3 = st.columns(3)

        with col_adv1:
            st.selectbox("Statistical Test", ["Pearson Correlation", "Spearman Correlation", "Chi-squared", "ANOVA"])
            st.multiselect("Additional Features", ["Heart Rate", "Blood Pressure", "Respiration", "Temperature", "Movement"])

        with col_adv2:
            st.selectbox("Model Type", ["Transformer", "CNN-LSTM", "XGBoost", "Ensemble"])
            st.number_input("Confidence Threshold", min_value=0.5, max_value=0.95, value=0.7, step=0.05)

        with col_adv3:
            st.selectbox("Export Format", ["CSV", "JSON", "PDF Report", "DICOM"])
            st.button("Generate Report")




    # Main content layout with columns
    col1, col2 = st.columns([2, 1])

    # EEG Channels to display
    channels = ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'T3', 'T4']

    # Generate EEG data for 30 seconds
    time_array, eeg_data = generate_eeg_data(channels, seconds=30)

    # Generate attention data
    attention_data = generate_attention_data(channels, seconds=30)

    # EEG plot with attention highlights
    with col1:
        st.markdown("<div class='section-header'>EEG with Attention Highlights</div>", unsafe_allow_html=True)

        # Create EEG visualization with plotly
        fig = make_subplots(rows=len(channels), cols=1, shared_xaxes=True, vertical_spacing=0.01,
                            subplot_titles=channels)

        for i, channel in enumerate(channels):
            # Add EEG trace
            fig.add_trace(
                go.Scatter(
                    x=time_array,
                    y=eeg_data[channel],
                    name=channel,
                    line=dict(color='#2c3e50', width=1),
                ),
                row=i+1, col=1
            )

            # Add highlight for high attention regions (if F3 channel)
            if channel == 'F3':
                fig.add_vrect(
                    x0=15, x1=20,
                    fillcolor="rgba(231, 76, 60, 0.2)",
                    opacity=0.8,
                    layer="below", line_width=0,
                    row=i+1, col=1
                )

                # Add annotation for high attention region
                fig.add_annotation(
                    x=17.5, y=min(eeg_data[channel]),
                    text="High Attention Region",
                    showarrow=False,
                    font=dict(color="rgb(231, 76, 60)"),
                    row=i+1, col=1
                )

        # Update layout
        fig.update_layout(
            height=600,
            showlegend=False,
            margin=dict(l=50, r=20, t=10, b=50),
        )

        fig.update_xaxes(title_text="Time (s)", row=len(channels), col=1)

        st.plotly_chart(fig, use_container_width=True)

        # Channel selection
        st.markdown("**Channels:** Fp1, Fp2, F3, F4, C3, C4, P3, P4, O1, O2, T3, T4, T5, T6")

    # Attention map visualization
    with col2:
        st.markdown("<div class='section-header'>Attention Map</div>", unsafe_allow_html=True)

        # Create heatmap for attention
        fig = px.imshow(
            attention_data,
            labels=dict(x="Time (s)", y="Channel", color="Attention Score"),
            x=[f"{i*0.2:.1f}" for i in range(attention_data.shape[1])],
            y=channels,
            color_continuous_scale='Reds',
            aspect="auto"
        )

        fig.update_layout(
            height=600,
            margin=dict(l=50, r=20, t=10, b=50),
        )

        st.plotly_chart(fig, use_container_width=True)

        # Legend
        cols = st.columns(3)
        with cols[0]:
            st.color_picker("High Attention", "#e74c3c", disabled=True)
            st.markdown("High Attention")
        with cols[1]:
            st.color_picker("Medium Attention", "#fab1a0", disabled=True)
            st.markdown("Medium Attention")
        with cols[2]:
            st.color_picker("Low Attention", "#ffeaa7", disabled=True)
            st.markdown("Low Attention")

    # Clinical variables and model interpretation
    st.markdown("<div class='section-header'>Clinical Variables and Model Interpretation</div>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    # Influential clinical variables
    with col3:
        st.markdown("#### Influential Clinical Variables")

        # Create dataframe for clinical variables
        clinical_vars = pd.DataFrame({
            'Variable': [
                'Prior Seizure History',
                'EEG Abnormalities (F3)',
                'Age',
                'Medications (Levetiracetam)',
                'Sleep Deprivation',
                'Structural Lesion',
                'Genetic Factors'
            ],
            'Importance': [0.72, 0.91, 0.36, 0.48, 0.58, 0.24, 0.17]
        })

        # Create horizontal bar chart
        fig = px.bar(
            clinical_vars,
            x='Importance',
            y='Variable',
            orientation='h',
            color='Importance',
            color_continuous_scale=['#3498db', '#e74c3c'],
            range_color=[0, 1]
        )

        fig.update_layout(
            height=400,
            margin=dict(l=0, r=0, t=10, b=10),
            yaxis=dict(autorange="reversed"),
        )

        st.plotly_chart(fig, use_container_width=True)

    # Case-based reasoning
    with col4:
        st.markdown("#### Case-Based Reasoning")

        st.markdown("<div class='info-box'>", unsafe_allow_html=True)
        st.markdown("**Similar Case #17382:**")
        st.markdown("• 32-year-old male with similar F3 discharge pattern")
        st.markdown("• Developed seizure within 4 hours of recording")
        st.markdown("• Responded to increased Levetiracetam dosage")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='info-box'>", unsafe_allow_html=True)
        st.markdown("**Model Prediction:**")
        st.markdown("<span class='highlight-text'>67% probability of seizure within next 6 hours</span>", unsafe_allow_html=True)
        st.markdown("Confidence interval: 54%-79%")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='info-box'>", unsafe_allow_html=True)
        st.markdown("**Recommended Actions:**")
        st.markdown("1. Increase monitoring frequency")
        st.markdown("2. Consider prophylactic medication adjustment")
        st.markdown("</div>", unsafe_allow_html=True)

    # Additional interactive elements
    st.markdown("<div class='section-header'>Interactive Analysis</div>", unsafe_allow_html=True)

    col5, col6 = st.columns(2)

    # Add time slider for EEG navigation
    with col5:
        st.markdown("#### EEG Navigation")
        time_slider = st.slider("Navigate EEG timeline (seconds)", 0, 120, 30)

        # Seizure risk over time
        st.markdown("#### Seizure Risk Prediction Over Time")

        # Generate risk prediction data
        hours = list(range(24))
        base_risk = [0.2, 0.25, 0.3, 0.4, 0.55, 0.67, 0.72, 0.65, 0.6, 0.5, 0.45, 0.4,
                    0.35, 0.3, 0.28, 0.25, 0.23, 0.2, 0.18, 0.15, 0.14, 0.13, 0.12, 0.1]

        # Add confidence intervals
        ci_lower = [max(0, r - 0.12) for r in base_risk]
        ci_upper = [min(1, r + 0.12) for r in base_risk]

        # Create the line chart with confidence interval
        fig = go.Figure([
            go.Scatter(
                name='Upper Bound',
                x=hours,
                y=ci_upper,
                mode='lines',
                marker=dict(color="#444"),
                line=dict(width=0),
                showlegend=False
            ),
            go.Scatter(
                name='Lower Bound',
                x=hours,
                y=ci_lower,
                marker=dict(color="#444"),
                line=dict(width=0),
                mode='lines',
                fillcolor='rgba(231, 76, 60, 0.2)',
                fill='tonexty',
                showlegend=False
            ),
            go.Scatter(
                name='Seizure Risk',
                x=hours,
                y=base_risk,
                mode='lines',
                line=dict(color='rgb(231, 76, 60)'),
                showlegend=True
            )
        ])

        fig.update_layout(
            height=300,
            title='Predicted Seizure Risk',
            yaxis_title='Probability',
            xaxis_title='Hours from Now',
            hovermode="x",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

        st.plotly_chart(fig, use_container_width=True)

    # Feature correlation matrix
    with col6:
        st.markdown("#### Feature Correlation Analysis")

        # Generate correlation data
        features = ['Age', 'Seizure History', 'F3 Spikes', 'Sleep Dep.', 'Med. Adherence', 'Lesion Size']
        corr_matrix = np.array([
            [1.0, 0.2, 0.15, 0.1, 0.05, 0.25],
            [0.2, 1.0, 0.45, 0.3, 0.15, 0.4],
            [0.15, 0.45, 1.0, 0.6, 0.3, 0.5],
            [0.1, 0.3, 0.6, 1.0, 0.2, 0.1],
            [0.05, 0.15, 0.3, 0.2, 1.0, 0.05],
            [0.25, 0.4, 0.5, 0.1, 0.05, 1.0]
        ])

        # Create heatmap
        fig = px.imshow(
            corr_matrix,
            labels=dict(x="Feature", y="Feature", color="Correlation"),
            x=features,
            y=features,
            color_continuous_scale='RdBu_r',
            zmin=-1.0, zmax=1.0
        )

        fig.update_layout(
            height=300,
            margin=dict(l=10, r=10, t=10, b=10),
        )

        st.plotly_chart(fig, use_container_width=True)

        # Add interactive threshold selector for attention visualization
        st.markdown("#### Attention Threshold Adjustment")
        attention_threshold = st.slider("Highlight threshold for attention scores", 0.0, 1.0, 0.5, 0.05)
        st.markdown(f"Regions with attention scores above **{attention_threshold}** will be highlighted")


    # Footer with sample metrics
    st.markdown("---")
    metric_cols = st.columns(4)

    with metric_cols[0]:
        st.metric(label="Model Accuracy", value="83%", delta="1.2%")

    with metric_cols[1]:
        st.metric(label="Prediction Time", value="1.2 sec", delta="-0.3 sec")

    with metric_cols[2]:
        st.metric(label="False Positive Rate", value="12%", delta="-2.4%")

    with metric_cols[3]:
        st.metric(label="Data Points Analyzed", value="24,892", delta="1,204")


elif page == "Proposed Grants":
    st.markdown("<div class='main-header'>Grant Proposals</div>", unsafe_allow_html=True)

    if grant_type == "NIH K99/R00":
        # K99/R00 Grant Content
        st.markdown("<div class='section-header'>NIH BRAIN Initiative K99/R00 Pathway to Independence Award</div>", unsafe_allow_html=True)

        # Title section with blue styling
        st.markdown("""
        <div style="background: linear-gradient(to right, #1a5276, #2980b9); color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
            <h2 style="margin: 0;">NIH BRAIN Initiative K99/R00</h2>
            <h3 style="margin: 10px 0;">Pathway to Independence Award</h3>
            <p style="font-style: italic; margin: 0;">A Funding Strategy for NeuroAI Research</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Program Description")
            st.markdown("• Facilitates transition from postdoctoral research to independent faculty position")
            st.markdown("• Two phases: mentored (K99) followed by independent research (R00)")
            st.markdown("• Special emphasis on diversity in NIH BRAIN Initiative version")
            st.markdown("• Focus on innovative approaches in NeuroAI")

        with col2:
            st.markdown("### Key Benefits")
            st.markdown("• Substantial funding: Up to $250,000/year during R00 phase")
            st.markdown("• Career stability during critical transition period")
            st.markdown("• Enhanced visibility within neuroscience community")
            st.markdown("• Protected research time (75% effort commitment)")

        # Add eligibility criteria section from the TSX file
        st.markdown("### Eligibility & Requirements")
        col_elig1, col_elig2 = st.columns(2)

        with col_elig1:
            st.markdown("#### Eligibility Criteria")
            st.markdown("• Postdoctoral researchers with ≤5 years experience")
            st.markdown("• Must be in mentored position at application time")
            st.markdown("• U.S. citizenship not required for standard K99")
            st.markdown("• U.S. citizenship/permanent residency required for BRAIN diversity K99")

        with col_elig2:
            st.markdown("#### Application Components")
            st.markdown("• Research plan integrating K99 and R00 phases")
            st.markdown("• Career development plan")
            st.markdown("• Strong mentorship team with expertise in NeuroAI")
            st.markdown("• Institutional commitment letters")

        st.markdown("### Alignment with NeuroAI Center")
        st.markdown("""
        - **Multimodal Data Integration:** Proposed K99/R00 would focus on developing transformer-based architectures for integrating EEG, EHR, and neuroimaging data—directly supporting work on HyperEnsemble learning.
        - **Explainable AI:** Will incorporate SHAP values and attention mechanisms to make models interpretable for clinicians, addressing a key center priority.
        - **Clinical Translation:** Focuses on prognostic models for coma recovery, aligning with clinical research priorities.
        - **Institutional Strength:** MGH's strong NIH funding track record enhances competitiveness for this award.
        """)

        st.markdown("### Timeline & Strategy")
        col3, col4 = st.columns(2)

        with col3:
            st.markdown("#### Key Dates")
            st.markdown("• Feb 13, 2025: Next standard application deadline")
            st.markdown("• June 13, 2025: BRAIN Initiative diversity K99/R00 deadline")
            st.markdown("• 7-9 months: Review timeline from submission to award")
            st.markdown("• Up to 5 years: Total award duration (K99: 1-2 years; R00: 3 years)")

        with col4:
            st.markdown("#### Expected Outcomes")
            st.markdown("• Novel transformer architecture for multimodal neural data")
            st.markdown("• Clinical validation of prognostic models")
            st.markdown("• Open-source software and datasets")
            st.markdown("• 3-4 high-impact publications")

        # Add application strategy from TSX file
        st.markdown("#### Application Strategy")
        st.markdown("• Develop proposal in first 3-6 months at NeuroAI Center")
        st.markdown("• Leverage center's unique datasets and computational resources")
        st.markdown("• Incorporate mentorship from both Dr. Rosenthal and Dr. Zabihi")
        st.markdown("• Include preliminary results from initial projects at the center")

    elif grant_type == "NSF CAREER":
        # NSF CAREER Grant Content
        st.markdown("<div class='section-header'>NSF CAREER Award: Advancing NeuroAI through Integrated Research and Education</div>", unsafe_allow_html=True)

        # Title section with green styling
        st.markdown("""
        <div style="background: linear-gradient(to right, #145a32, #27ae60); color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
            <h2 style="margin: 0;">NSF CAREER Award</h2>
            <h3 style="margin: 10px 0;">Advancing NeuroAI through Integrated Research and Education</h3>
            <p style="font-style: italic; margin: 0;">A Five-Year Research and Education Plan</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Award Description")
            st.markdown("• NSF's most prestigious award for early-career faculty")
            st.markdown("• Supports those with potential to serve as academic role models")
            st.markdown("• Integrates research and education activities")
            st.markdown("• Builds foundation for lifetime of leadership")

        with col2:
            st.markdown("### Award Details")
            st.markdown("• 5-year project period")
            st.markdown("• Minimum award of $400,000 total")
            st.markdown("• Cognitive Neuroscience program average: $175,000-$225,000 per year")
            st.markdown("• Annual submission deadline in July")

        st.markdown("### Proposed Research Plan")
        st.markdown("#### NeuroAI-Based Self-Supervised Learning for Neurological Prognostication")
        st.markdown("""
        - **Research Goal:** Develop novel self-supervised learning approaches for neurophysiological data that require minimal labeled examples while maintaining clinical interpretability.
        - **Approach:** Implement contrastive learning techniques on unlabeled EEG and physiological data, creating foundation models that can be fine-tuned for specific clinical applications.
        - **Technical Innovation:** Design neurophysiology-specific data augmentation techniques that preserve clinically relevant signal characteristics while creating diverse training examples.
        - **Clinical Applications:** Apply these techniques to develop prognostic models for neurological recovery with a focus on interpretable predictions that can guide clinical decision-making.
        - **Broader Impact:** Address the persistent challenge of limited labeled data in clinical neuroscience while making AI systems more accessible to non-AI specialists.
        """)

        st.markdown("### Alignment with NeuroAI Center")
        st.markdown("""
        - **Research Focus:** Self-supervised learning for neurophysiological data directly complements Dr. Zabihi's work on multimodal data integration while extending the center's capabilities to handle limited labeled data scenarios.
        - **Clinical Translation:** Interpretability focus aligns with Dr. Rosenthal's emphasis on clinically relevant biomarker development and deployment of AI in neurological care.
        - **Educational Synergy:** NeuroAI Bootcamp can leverage the center's expertise and infrastructure, potentially becoming an annual program that enhances the center's educational mission.
        - **External Visibility:** NSF CAREER award would enhance the center's national profile in AI education and bring additional resources for educational initiatives.
        """)

        st.markdown("### Integrated Education Plan")
        col3, col4 = st.columns(2)

        with col3:
            st.markdown("#### Educational Goals")
            st.markdown("Bridge the gap between neuroscience and AI education")
            st.markdown("Increase diversity in NeuroAI workforce")
            st.markdown("Develop interdisciplinary curriculum materials")
            st.markdown("Engage clinicians in AI literacy")

        with col4:
            st.markdown("#### Key Activities")
            st.markdown("Develop 'NeuroAI Bootcamp' for underrepresented students")
            st.markdown("Create open educational resources for clinician AI literacy")
            st.markdown("Establish mentored research program for first-gen college students")
            st.markdown("Develop K-12 outreach program with brain-computer interface demos")

        # Add eligibility and requirements from TSX file
        st.markdown("### Eligibility & Requirements")
        col_elig1, col_elig2 = st.columns(2)

        with col_elig1:
            st.markdown("#### Eligibility Criteria")
            st.markdown("• Tenure-track (or equivalent) Assistant Professor")
            st.markdown("• Untenured at time of application")
            st.markdown("• Educational activities must be integrated with research")
            st.markdown("• Need departmental support letter")

        with col_elig2:
            st.markdown("#### Proposal Components")
            st.markdown("• Innovative research plan")
            st.markdown("• Integrated education plan (not just a list of activities)")
            st.markdown("• Departmental letter confirming support")
            st.markdown("• Prior NSF research results (if applicable)")

        st.markdown("### 5-Year Research & Education Roadmap")
        st.markdown("""
        <div style="background-color: #e8f8f5; padding: 15px; border-radius: 5px;">
            <p><strong>Year 1:</strong> Develop foundational self-supervised learning framework; launch pilot NeuroAI Bootcamp</p>
            <p><strong>Year 2:</strong> Extend framework to multimodal data; create open educational resources</p>
            <p><strong>Year 3:</strong> Implement clinical validation; expand mentored research program</p>
            <p><strong>Year 4:</strong> Develop interpretability tools; establish K-12 outreach program</p>
            <p><strong>Year 5:</strong> Deploy integrated system in clinical environment; assess educational outcomes</p>
        </div>
        """, unsafe_allow_html=True)

    elif grant_type == "McKnight Scholars":
        # McKnight Scholars Grant Content
        st.markdown("<div class='section-header'>McKnight Scholars Award: Explainable NeuroAI for Neural Circuit Understanding</div>", unsafe_allow_html=True)

        # Title section with purple styling
        st.markdown("""
        <div style="background: linear-gradient(to right, #4a235a, #8e44ad); color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
            <h2 style="margin: 0;">McKnight Scholars Award</h2>
            <h3 style="margin: 10px 0;">Explainable NeuroAI for Neural Circuit Understanding</h3>
            <p style="font-style: italic; margin: 0;">A Three-Year Research Proposal</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Program Description")
            st.markdown("• Prestigious award for early-career neuroscientists")
            st.markdown("• Supports exceptional scientists establishing independent labs")
            st.markdown("• Emphasis on impactful neuroscience research")
            st.markdown("• Values diversity, equity, and inclusion in science")

        with col2:
            st.markdown("### Award Details")
            st.markdown("• $225,000 total funding over three years ($75,000/year)")
            st.markdown("• Flexible use of funds (equipment, salary, supplies, etc.)")
            st.markdown("• No indirect costs allowed")
            st.markdown("• 10 awardees selected annually")

        st.markdown("### Proposed Research")
        st.markdown("#### Neural Circuit Decoding through Explainable NeuroAI")
        st.markdown("""
        - **Research Goal:** Develop neuroscience-informed AI architectures that reveal underlying neural circuit mechanisms while maintaining clinical interpretability.
        - **Innovative Approach:** Create circuit-inspired attention mechanisms that mimic known neurological processes, enabling both improved predictions and mechanistic insights into brain function.
        - **Technical Framework:** Implement dual-path neural networks where one path maximizes predictive performance while the second generates interpretable circuit models that neurologists can validate.
        - **Clinical Applications:** Focus on neurological recovery mechanisms after acute brain injury, identifying circuit-level biomarkers that predict recovery trajectories.
        """)

        st.markdown("### Research Specific Aims")
        st.markdown("""
        <div style="background-color: #f5eef8; padding: 15px; border-radius: 5px; margin-bottom: 15px;">
            <h4 style="color: #8e44ad; margin-top: 0;">Aim 1: Circuit-Inspired Neural Network Architecture</h4>
            <ul>
                <li>Develop attention mechanisms modeled after known neural circuit principles</li>
                <li>Incorporate hierarchical processing inspired by brain structure</li>
                <li>Validate architecture on publicly available EEG datasets</li>
            </ul>
        </div>

        <div style="background-color: #f5eef8; padding: 15px; border-radius: 5px; margin-bottom: 15px;">
            <h4 style="color: #8e44ad; margin-top: 0;">Aim 2: Mechanistic Interpretability Framework</h4>
            <ul>
                <li>Create visualization tools that map model activations to neural circuit components</li>
                <li>Develop circuit reconstruction algorithms from model weights</li>
                <li>Test interpretations against existing neurophysiological knowledge</li>
            </ul>
        </div>

        <div style="background-color: #f5eef8; padding: 15px; border-radius: 5px;">
            <h4 style="color: #8e44ad; margin-top: 0;">Aim 3: Clinical Validation and Application</h4>
            <ul>
                <li>Apply framework to predict recovery from traumatic brain injury and coma</li>
                <li>Identify circuit-level biomarkers predictive of outcomes</li>
                <li>Validate findings through clinical collaboration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Expected Outcomes & Impact")
        col3, col4 = st.columns(2)

        with col3:
            st.markdown("#### Scientific Contributions")
            st.markdown("• Novel circuit-inspired neural network architectures")
            st.markdown("• Framework for extracting mechanistic insights from AI models")
            st.markdown("• New understanding of circuit mechanisms in recovery")
            st.markdown("• 3-5 high-impact publications")

        with col4:
            st.markdown("#### Broader Impact")
            st.markdown("• Bridge between AI performance and neuroscientific understanding")
            st.markdown("• Improved clinical prognostication tools")
            st.markdown("• Open-source software and educational resources")
            st.markdown("• Mentorship of diverse trainees in NeuroAI")

        # Add alignment section from TSX file
        st.markdown("### Strategic Fit with Center's Mission")
        st.markdown("""
        - **Research Synergy:** Directly complements Dr. Zabihi's work on EEG signal processing and Dr. Rosenthal's research on physiologic biomarkers for brain monitoring.
        - **Explainable AI Focus:** Addresses the center's need for interpretable AI models that clinicians can understand and trust, especially in critical care settings.
        - **Clinical Translation:** Practical applications align with MGH's clinical mission while advancing fundamental neuroscience understanding.
        - **Collaborative Potential:** Leverages MGH's unique datasets and clinical expertise while bringing novel AI approaches to existing problems.
        - **DEI Commitment:** Proposal includes specific plans for inclusive lab environment and outreach, matching McKnight Foundation's increased emphasis on diversity.
        """)

        # Add eligibility and timeline from TSX file
        st.markdown("### Eligibility & Timeline")
        col_elig1, col_elig2 = st.columns(2)

        with col_elig1:
            st.markdown("#### Eligibility Requirements")
            st.markdown("• Assistant Professors with less than 5 years at that rank")
            st.markdown("• At non-profit research institutions in U.S.")
            st.markdown("• Demonstrated commitment to inclusive lab environment")
            st.markdown("• Cannot be tenured or hold another McKnight award")

        with col_elig2:
            st.markdown("#### Key Dates (2026 Cycle)")
            st.markdown("• August 2025: Application period opens")
            st.markdown("• January 2026: Application deadline")
            st.markdown("• April 2026: Finalist notifications")
            st.markdown("• May 2026: Interviews")
            st.markdown("• July 1, 2026: Funding begins")

        # Add McKnight Scholar Community information
        st.markdown("### McKnight Scholar Community")
        st.markdown("The McKnight Scholar award provides not just funding, but access to a prestigious community of neuroscientists that continues throughout one's career:")
        st.markdown("• **Annual Conference:** McKnight Scholars attend the annual McKnight Conference on Neuroscience for three years after receiving the award, then return every three years.")
        st.markdown("• **Networking Opportunities:** Connect with leading neuroscientists across career stages and research areas.")
        st.markdown("• **Collaborative Potential:** Many McKnight Scholars develop collaborations with other awardees, leading to innovative cross-disciplinary research.")
        st.markdown("• **Career-Long Affiliation:** Being a McKnight Scholar provides a prestigious affiliation that continues throughout one's career.")
        st.markdown("• **Mentorship:** Senior McKnight Scholars often mentor junior awardees, creating a supportive community.")


elif page == 'Slide Deck (Alignment/Proposed-Contributions)':
    st.markdown("### Slide Deck (Alignment/Proposed-Contributions)")


    # Embed Gamma presentation
    st.markdown("""
    <iframe src="https://gamma.app/embed/7dr2nf8b2ruqwtp"
            style="width: 1000px; max-width: 100%; height: 650px"
            allow="fullscreen"
            title="NeuroAI Job Interview">
    </iframe>
    """, unsafe_allow_html=True)
