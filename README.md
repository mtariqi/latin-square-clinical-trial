# Unified Framework for Clinical-Trial Simulation and Context-Controlled Machine Learning
Author: **Md Tariqul Islam (TARIQ)**

![CI](https://github.com/mtariqi/synthetic-variant-calling-benchmark/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Status](https://img.shields.io/badge/status-active-success)

---

## 📌 Overview

This repository unifies **two major scientific toolkits** built on Latin Square experimental design:

### **1) Clinical-Trial Latin Square Analyzer**

A comprehensive Python toolkit for designing, simulating, and analyzing
**crossover clinical trials** using Latin Square designs.

### **2) COMALLS Scheduler Library**

A model-agnostic machine learning framework that uses
**Latin Square–based structured experimentation**
to replace random batching with **context-controlled learning episodes**.

Both systems rely on the same statistical foundation and are now integrated into one coherent research package.

---


# 📝 Table of Contents

* [Overview](#overview)
* [COMALLS: ML Scheduler](#comalls-ml-scheduler)
* [Clinical-Trial Toolkit](#clinical-trial-toolkit)
* [Installation](#installation)
* [Project Structure](#project-structure)
* [Usage Examples](#usage-examples)

  * COMALLS Scheduler (ML)
  * Clinical-Trial Analyzer (Health Science)
* [Diagrams](#diagrams)
* [Statistical Methods](#statistical-methods)
* [Contributing](#contributing)
* [License](#license)

---

# 🚀 COMALLS: ML Scheduler

### *Context-Controlled ML Training Using Latin Squares*

Modern ML uses stochastic mini-batches, which often confound model improvements with uncontrolled factors (domain shift, noise level, client distribution).
**COMALLS** replaces this randomness with a **designed experiment**:

### ✔ Latin-square–based episode scheduling

✔ Each model appears exactly once per context pairing
✔ Enables ANOVA/mixed-model analysis
✔ Model-agnostic, plug-in compatible with PyTorch, TensorFlow, etc.
✔ Perfect for robustness, noise studies, and federated learning research

---

## 🔧 COMALLS API Example

```python
from comalls import LatinSquareScheduler

scheduler = LatinSquareScheduler(
    models=["ModelA", "ModelB", "ModelC"],
    context1=["LowShift", "MediumShift", "HighShift"],
    context2=["LowNoise", "MidNoise", "HighNoise"],
    seed=42
)

for ep in scheduler:
    print(ep.episode_id, ep.model, ep.context1, ep.context2)
```

### Output

```
Episode 0: ModelA under LowShift & LowNoise
Episode 1: ModelB under LowShift & MidNoise
Episode 2: ModelC under LowShift & HighNoise
...
```

---

# 🏥 Clinical-Trial Toolkit

### *Latin Square Designs for Health Science Research*

A full-featured toolkit for:

* Simulating crossover clinical trial data
* Running ANOVA & paired comparisons
* Visualizing study designs
* Generating publication-ready medical research figures
* Producing full text statistical reports

---

## 🔬 What is a Latin Square Design?

A *k × k* layout where each treatment appears:

* exactly **once per subject row**
* exactly **once per time-period column**

This controls for two independent sources of variation:

* Subject differences
* Period / time effects

---

## 🧪 Clinical Trial Example

```python
from latin_square_analyzer import LatinSquareDesign

treatments = ['Placebo', 'Drug_A', 'Drug_B', 'Drug_C']
trial = LatinSquareDesign(treatments)

design = trial.generate_design(randomize=True)
data = trial.simulate_trial_data({"Placebo":0, "Drug_A":15, "Drug_B":25, "Drug_C":10})
results = trial.analyze_results()

trial.visualize_design()
trial.visualize_results()
trial.generate_report("trial_report.txt")
```

---

# 🧬 Unified Project Structure

```
latin-square-clinical-trial/
│
├── README.md                     ← (this file)
│
├── comalls/                      ← ML scheduler library
│   ├── __init__.py
│   ├── latin_square.py
│   ├── scheduler.py
│   └── episode_runner.py
│
├── latin_square_analyzer.py      ← Clinical trial simulator
├── analyze_real_clinical_data.py
│
├── examples/
│   ├── demo_scheduler.ipynb
│   └── example_real_data.ipynb
│
├── data/
│   ├── sample_simulated.csv
│   └── sample_real.csv
│
└── docs/
    ├── methodology.md
    ├── data_sources.md
    └── comalls_methods.md        ← Ready to paste into a research paper
```

---

# 🔧 Installation

### Requirements

```bash
Python 3.7+
```

### Install dependencies

```bash
pip install numpy pandas matplotlib seaborn scipy
```

### Install COMALLS locally

```bash
pip install -e .
```

---

# 📚 Usage Examples

## 1️⃣ COMALLS ML Experiment (PyTorch Demo)

```python
from comalls import LatinSquareScheduler
import torch, torch.nn as nn

class TinyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 2)

scheduler = LatinSquareScheduler(
    models=["A","B","C"],
    context1=["domain1","domain2","domain3"],
    context2=["noise_low","noise_mid","noise_high"]
)

for ep in scheduler:
    model = TinyNet()
    # load data based on ep.context1 and ep.context2
    # train() model...
    # eval() model...
```

---

## 2️⃣ Clinical Trial Simulation

```python
from latin_square_analyzer import LatinSquareDesign

trial = LatinSquareDesign(['Placebo','DrugA','DrugB','DrugC'])
design = trial.generate_design()
data = trial.simulate_trial_data({'Placebo':0,'DrugA':20,'DrugB':18,'DrugC':10})
trial.generate_report("trial_report.txt")
```

---

# 🧩 Diagrams
```
flowchart TD
    A[Define Models] --> C[Latin Square Scheduler]
    B[Define Context Factors] --> C
    C --> D[Generate Episodes]
    D --> E[Run ML Training/Eval]
    E["Statistical Aggregation (ANOVA / Mixed Models)"] --> F["Meta-Learning Updates"]
```

# 📈 Statistical Methods

Both the clinical-trial and COMALLS frameworks support:

* **ANOVA**
* **Paired t-tests**
* **Effect size estimation**
* **Mixed-effects modeling (optional)**
* **Confidence intervals**
* **Balanced evidence under controlled conditions**

---

# 🤝 Contributing

Pull requests are welcome!

---

# 📝 License

Licensed under the MIT License (see LICENSE file).

---

# 👥 Author

**Md Tariqul Islam**
GitHub: [https://github.com/mtariqi](https://github.com/mtariqi)
Email: [tariqul@scired.com](mailto:tariqul@scired.com)

---

# ⭐ If you find this unified framework helpful, please give the repo a star!

---


Just tell me!
