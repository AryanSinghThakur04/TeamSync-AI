# TeamSync-AI

TeamSync-AI is a professional, full-stack analytics platform designed to revolutionize team assembly through data-driven insights. By combining Organizational Behavior (Belbin Team Roles) with Social Network Analysis (SNA) and Genetic Algorithm Optimization, this tool helps executives build high-performance, psychologically safe teams with surgical precision.

## Key Features:-

This project provides actionable intelligence through a modern SaaS interface:

## Core Analytics & Visualizations:

1. Strategic Competency Matrix: A multi-dimensional heatmap that identifies technical coverage and behavioral gaps to prevent 'Single Points of Failure' in projects.

2. Cohesion Index (Psychological Safety): A real-time gauge measuring team trust and innovation potential, inspired by Google’s Project Aristotle.

3. Communication Flux (SNA): An interactive, centrality-weighted network graph that visualizes team hierarchy, identifying "Network Leaders" and "Strategic Bridges".

4. Executive Strategic Roster: A polished data view of the optimized team, including Belbin roles, technical skills, and financial impact.

## AI-Driven Team Assembly:

1. Genetic Algorithm Optimization: An AI engine that sifts through a talent pool to assemble the most cost-effective and skilled team based on your specific budget and tech stack.

2. Manual Interchange Mode: A flexible interface for executives to manually swap team members and see the immediate impact on the team's Safety Index and ROI.

## Enterprise-Grade UI/UX:

1. Modern SaaS Aesthetic: A clean, professional Indigo and Slate palette designed for executive presentations and product demos.

2. Interactive Sidebar: Dynamic controls for portfolio budgeting, tech stack selection, and team capacity management.

## Tech Stack:-

1. Backend & Framework: Python, Streamlit

2. Data Science & AI: Pandas, Scikit-learn, Genetic Algorithms

3. Visualizations: Plotly (Heatmaps & Gauges), Pyvis (Network Graphs)

4. Project Logic: Organizational Behavior Mapping (Belbin & Big Five Theory)


## Setup and Installation:-

Prerequisites
Python 3.9+

Git

1. Clone the Repository-
   
git clone https://github.com/your-username/TeamSync-AI.git
cd TeamSync-AI

2. Create and Activate Virtual Environment-
On Windows:

python -m venv venv
venv\Scripts\activate

3. Install Dependencies-
   
pip install -r requirements.txt

4. Directory Structure-
   
main.py: The primary SaaS Dashboard.

src/engine/management_logic.py: Core metrics and role mapping logic.

src/analysis/sna_generator.py: Network graph generation.

5. Run the Application-
   
streamlit run main.py

The application will launch at http://localhost:8501/. Use the Strategic Config sidebar to begin your first AI-driven team optimization.

## New Terminal Quickstart:-

1. cd C:\Path\To\TeamSync-AI
2. venv\Scripts\activate
3. streamlit run app/main.py
