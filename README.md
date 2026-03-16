# AI and Physics Based G-Code Optimizer for CNC Routers

A hybrid **AI + physics-driven optimization framework** for CNC machining of Medium-Density Fibreboard (MDF).  
This project combines **physics-based machining models, machine learning (CatBoost), and Genetic Algorithms** to predict machining behavior, optimize cutting parameters, and automatically regenerate CNC G-code for improved machining performance.

This system bridges the gap between **theoretical machining optimization and real-world CNC implementation**.

---

# Problem Statement

CNC machining of MDF often uses aggressive strategies with:

- high feed rates
- large depth of cut
- fewer machining passes

While these approaches improve machining speed, they often lead to:

- excessive cutting forces
- rapid tool wear
- high vibration
- poor surface finish
- increased energy consumption

Many optimization studies recommend improved machining parameters but **do not translate these results into executable CNC instructions (G-code)**.

This project solves that problem by:

- predicting machining behavior
- optimizing machining parameters
- automatically regenerating CNC G-code for real machining use

---

# Key Features

- Physics-based machining response modeling
- Synthetic machining dataset generation
- Machine learning trend prediction using **CatBoost**
- Multi-objective optimization using **Genetic Algorithms**
- Automatic **CNC G-code parsing**
- Automatic **G-code regeneration with optimized parameters**
- Experimental validation on a real CNC router

---

# System Architecture
The optimization pipeline follows this workflow:

Original G-code
↓
Parse machining parameters and toolpath
↓
Physics-based machining models
↓
Synthetic dataset generation
↓
Machine learning model training (CatBoost)
↓
Genetic Algorithm optimization
↓
Optimized machining parameters
↓
Regenerate optimized G-code
↓
Run optimized machining process


---

# Machining Responses Modeled

The system predicts the following machining responses:

- Cutting Force
- Surface Roughness
- Tool Wear Rate
- Vibration Amplitude
- Cutting Temperature
- Chip Load Deviation
- Power Consumption

These responses are modeled using **physics-informed equations combined with machine learning trend prediction**.

---

# Machine Learning Model

Machine learning models are trained on synthetic machining data generated from physics-based equations.

Algorithms used:

- CatBoost Regressor
- Random Forest Regressor

These models predict machining response trends for different machining parameters.

---

# Optimization Method

A **Genetic Algorithm (GA)** is used to optimize machining parameters.

The optimization minimizes a multi-objective cost function:

Cost = w1 * CuttingForce
+ w2 * SurfaceRoughness
+ w3 * ToolWearRate
+ w4 * Temperature
+ w5 * VibrationAmplitude


The algorithm optimizes:

- Feed Rate
- Depth of Cut
- Spindle Speed (when allowed)

---

# G-Code Regeneration

The optimized parameters are automatically embedded into CNC toolpaths by:

1. Parsing the original G-code
2. Extracting machining segments
3. Breaking deep cuts into safer passes
4. Replacing feed rate and depth values
5. Generating new optimized G-code

This allows the optimized strategy to be **directly executed on CNC machines**.

---

# Experimental Setup

Machining validation was performed on a physical CNC router.

**Machine:**  
Zura CNC Router

**Material:**  
Medium-Density Fibreboard (MDF)

**Tool:**  
6 mm diameter, 3-flute flat end mill

**Controller:**  
DSP A-11 Controller

---

# Results

The optimized G-code strategy was compared with the original machining strategy.

| Metric | Original | Optimized | Improvement |
|------|------|------|------|
| Surface Roughness (Ra) | 20.5 µm | 13.4 µm | **34% better surface finish** |
| Cutting Force | 654 → 202 | | **69% reduction per pass** |
| Tool Wear Rate | 2.8×10⁻⁵ | 1.8×10⁻⁵ | **36% reduction** |
| Vibration Amplitude | 0.0046 | 0.0033 | **28% reduction** |
| Power Consumption | 4111 | 1272 | **69% reduction per pass** |
| Tool Life | ~200 pockets | ~1000 pockets | **5× improvement** |

The optimized strategy distributes the cutting load across multiple passes, significantly improving machining stability and tool life.

---
Future Work

Potential improvements include:

real-time sensor feedback integration

reinforcement learning for adaptive machining control

deployment on industrial CNC controllers

extension to metal machining

cloud-based optimization service for CNC workflows

---

Author

G.J Vishal Chowdhary
B.Tech Mechatronics and Automation
Vellore Institute of Technology

---
Keywords

CNC Machining
Machine Learning
G-Code Optimization
Genetic Algorithms
CatBoost
Manufacturing AI
Physics-Informed Modeling








The optimization pipeline follows this workflow:

