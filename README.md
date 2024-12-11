# KAIM-W0-EDA-for-Moonlight-Energy-Solutions
Exploratory Data Analysis and Solar Dashboard for MoonLight Energy Solutions.
# Solar Energy Analysis with Streamlit

This project analyzes environmental data to identify high-potential regions for solar energy installations. It includes data preprocessing, exploratory data analysis (EDA), and visualization of key environmental metrics such as solar radiation, temperature, wind speed, and humidity. The findings are presented through an interactive **Streamlit dashboard**, allowing users to explore the data dynamically.

## Project Overview

MoonLight Energy Solutions aims to optimize solar energy investments by using data to select the best regions for solar installations. This project supports the company's goals by identifying patterns in solar radiation, temperature, and wind conditions, and visualizing them in an interactive web application.

### Key Features:
- **Data Upload**: Users can upload their own datasets for analysis.
- **Exploratory Data Analysis (EDA)**: Generates summary statistics, correlation heatmaps, and visualizations like histograms, scatter plots, and wind roses.
- **Time Series Analysis**: Analyze trends in solar radiation and temperature.
- **Interactive Dashboard**: Built with **Streamlit**, users can interact with the data, visualize relationships, and explore regional trends.

## Installation

### Prerequisites

Make sure you have the following installed:
- **Python 3.7+**
- **pip** (Python package manager)

### Step-by-Step Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/solar-energy-analysis.git
    cd solar-energy-analysis
    ```

2. **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit Dashboard**
    ```bash
    streamlit run eda_dashboard.py
    ```

    After running the command, open your browser and go to `http://localhost:8501` to access the dashboard.

### **Dependencies**

The following Python libraries are used:
- `pandas`: Data manipulation and analysis.
- `numpy`: Numerical operations.
- `seaborn`: Data visualization.
- `matplotlib`: Data visualization.
- `streamlit`: Web framework for creating interactive dashboards.

To install all required dependencies, simply run:
```bash
pip install -r requirements.txt

