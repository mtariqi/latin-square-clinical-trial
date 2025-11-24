![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

### 📝Project Description
A comprehensive Python toolkit for designing, simulating, and analyzing 
crossover clinical trials using Latin Square experimental designs. 
Includes data simulation, statistical analysis (ANOVA, pairwise tests), 
and publication-ready visualizations for health science research.

### 💡 Topics 
- `clinical-trials`
- `latin-square`
- `biostatistics`
- `crossover-design`
- `health-science`
- `python`
- `data-analysis`
- `experimental-design`
- `statistics`

## Project Overview

This project demonstrates Latin Square design analysis for crossover clinical trials:

- **Theoretical Implementation**: Complete simulator with customizable parameters
- **Applied Analysis**: Tools for analyzing real clinical trial data
- **Educational Resources**: Comprehensive methodology documentation

### Two Ways to Use This Project:

1. **Learning & Simulation** (`latin_square_analyzer.py`):
   - Generate custom crossover trial data
   - Test different scenarios
   - Understand methodology

2. **Real Data Analysis** (`analyze_real_clinical_data.py`):
   - Analyze actual clinical trial data
   - Verify Latin Square structure
   - Publication-ready outputs

## **Project Structure:**
```
latin-square-clinical-trial/
│
├── README.md
├── QUICKSTART.md
├── DATA_SOURCES.md                  
│
├── latin_square_analyzer.py         📊 Simulated data (educational)
├── analyze_real_clinical_data.py    🔬 Real data (applied) 
│
├── examples/
│   ├── example_pain_study.py        (simulated)
│   └── example_real_data.ipynb      (real data notebook) 
│
├── data/
│   ├── sample_simulated.csv         (generated data)
│   └── sample_real.csv              (real or realistic data) 
│
└── docs/
    ├── methodology.md
    └── data_sources.md              
    ```
    
# Latin Square Clinical Trial Analyzer

A comprehensive Python toolkit for designing, simulating, and analyzing crossover clinical trials using Latin Square experimental designs in health science research.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

## 📋 Table of Contents

- [Overview](#overview)
- [What is a Latin Square Design?](#what-is-a-latin-square-design)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Example Use Cases](#example-use-cases)
- [Output Files](#output-files)
- [Statistical Methods](#statistical-methods)
- [Contributing](#contributing)
- [License](#license)

## 🔬 Overview

This project provides a complete framework for conducting crossover clinical trials using Latin Square designs. It's particularly useful for comparing multiple treatments (e.g., medications, therapies, interventions) while controlling for:

- **Individual differences** between subjects
- **Time/period effects** (learning, fatigue, disease progression)
- **Carryover effects** from previous treatments

## 🎯 What is a Latin Square Design?

A Latin Square is an experimental design where:
- Each treatment appears exactly **once** in each row (subject)
- Each treatment appears exactly **once** in each column (time period)
- This ensures balanced comparison while controlling for two sources of variation

**Example 4×4 Latin Square:**

| Subject | Period 1 | Period 2 | Period 3 | Period 4 |
|---------|----------|----------|----------|----------|
| Patient 1 | Drug A | Drug B | Drug C | Placebo |
| Patient 2 | Drug B | Drug C | Placebo | Drug A |
| Patient 3 | Drug C | Placebo | Drug A | Drug B |
| Patient 4 | Placebo | Drug A | Drug B | Drug C |

## ✨ Features

- ✅ **Automated Design Generation**: Create balanced Latin Square designs with optional randomization
- ✅ **Data Simulation**: Generate realistic trial data with configurable parameters:
  - Treatment effects
  - Baseline variability
  - Period effects
  - Carryover effects
  - Random noise
- ✅ **Statistical Analysis**:
  - ANOVA (Analysis of Variance)
  - Paired t-tests for treatment comparisons
  - Summary statistics by treatment
- ✅ **Visualization**:
  - Design heatmaps
  - Box plots by treatment
  - Individual subject trajectories
  - Period effect analysis
- ✅ **Report Generation**: Comprehensive text reports with all analysis results
- ✅ **Data Export**: CSV export for further analysis in other tools

## 🚀 Installation

### Prerequisites

```bash
Python 3.7 or higher
```

### Required Packages

```bash
pip install numpy pandas matplotlib seaborn scipy
```

Or use the provided requirements file:

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

```python
from latin_square_analyzer import LatinSquareDesign

# Define treatments
treatments = ['Placebo', 'Drug_A', 'Drug_B', 'Drug_C']

# Create design
trial = LatinSquareDesign(treatments)

# Generate Latin Square
design = trial.generate_design(randomize=True)
print(design)

# Simulate trial data
treatment_effects = {
    'Placebo': 0,
    'Drug_A': 15,
    'Drug_B': 25,
    'Drug_C': 10
}

data = trial.simulate_trial_data(treatment_effects)

# Analyze results
results = trial.analyze_results()
print(results['treatment_summary'])

# Generate visualizations
trial.visualize_design(save_path='design.png')
trial.visualize_results(save_path='results.png')

# Generate report
trial.generate_report('trial_report.txt')
```

### Running the Demo

```bash
python latin_square_analyzer.py
```

This will:
1. Generate a randomized Latin Square design
2. Simulate clinical trial data
3. Perform statistical analysis
4. Create visualizations
5. Export all results to files


## 🏥 Example Use Cases

### 1. Pain Medication Comparison

```python
treatments = ['Placebo', 'Ibuprofen', 'Acetaminophen', 'Aspirin']
treatment_effects = {
    'Placebo': 0,
    'Ibuprofen': 20,
    'Acetaminophen': 15,
    'Aspirin': 18
}
```

### 2. Blood Pressure Monitor Evaluation

```python
treatments = ['Monitor_A', 'Monitor_B', 'Monitor_C', 'Gold_Standard']
# Test across different times and locations
```

### 3. Dietary Intervention Study

```python
treatments = ['Control_Diet', 'Mediterranean', 'DASH', 'Keto']
# Measure effects on cholesterol, blood sugar, weight
```

### 4. Asthma Inhaler Comparison

```python
treatments = ['Inhaler_A', 'Inhaler_B', 'Inhaler_C', 'Inhaler_D']
# Measure peak flow rates, symptom scores
```

## 📊 Output Files

The analyzer generates several output files:

1. **latin_square_design.csv**: The experimental design matrix
2. **trial_data.csv**: Complete trial dataset with all measurements
3. **trial_report.txt**: Comprehensive statistical analysis report
4. **design_heatmap.png**: Visual representation of the design
5. **results_analysis.png**: Multi-panel visualization of results

## 📈 Statistical Methods

### ANOVA (Analysis of Variance)
Tests whether there are significant differences among treatment means:
- **H₀**: All treatments have equal effects
- **H₁**: At least one treatment differs

### Paired t-tests
Compares each pair of treatments:
- Uses paired design (same subjects across treatments)
- Accounts for within-subject correlation

### Effect Size Measures
- Mean differences between treatments
- Standard deviations and confidence intervals

## 🔧 Advanced Configuration

### Custom Parameters

```python
trial.simulate_trial_data(
    treatment_effects=effects,
    baseline_mean=50,          # Average baseline response
    baseline_std=10,           # Variability between subjects
    period_effect=2,           # Time trend per period
    noise_std=5,               # Measurement error
    carryover_effect=0.1       # Proportion of previous effect
)
```

### Sample Size Considerations

```python
# For larger studies, extend the design
trial = LatinSquareDesign(treatments, n_subjects=12)
```

## 🎓 Educational Resources

### Key Concepts

1. **Crossover Design**: Each subject receives multiple treatments
2. **Blocking**: Controlling for known sources of variation
3. **Counterbalancing**: Distributing order effects evenly
4. **Washout Period**: Time between treatments to eliminate carryover

### When to Use Latin Squares

✅ **Good for:**
- Chronic conditions with stable symptoms
- Treatments with reversible effects
- Limited number of available subjects
- Need to control for individual variation

❌ **Avoid when:**
- Treatment has permanent effects (e.g., surgery)
- Long-lasting side effects
- Rapidly progressive disease
- High dropout risk

## 📚 References

1. Jones, B., & Kenward, M. G. (2014). *Design and Analysis of Cross-Over Trials* (3rd ed.). Chapman and Hall/CRC.

2. Senn, S. (2002). *Cross-over Trials in Clinical Research* (2nd ed.). John Wiley & Sons.

3. Fleiss, J. L. (1986). *The Design and Analysis of Clinical Experiments*. John Wiley & Sons.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Md Tariqul Islam** - *Initial work* -

## 🙏 Acknowledgments

- Inspired by classical experimental design principles
- Built for health science researchers and biostatisticians
- Designed to promote reproducible research practices

## 📧 Contact

- GitHub: https://github.com/mtariqi
- Email: tariqul@scired.com
- Project Link: https://github.com/mtariqi/latin-square-clinical-trial
- 

---

**⭐ If you find this project useful, please consider giving it a star!**








