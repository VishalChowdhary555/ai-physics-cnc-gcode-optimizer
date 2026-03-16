# AI and Physics Based G-Code Optimizer for CNC Routers

A hybrid **AI + physics-driven optimization framework** for CNC machining of Medium-Density Fibreboard (MDF).  
This project combines **physics-based machining models, machine learning (CatBoost), and Genetic Algorithms** to predict machining behavior, optimize cutting parameters, and automatically regenerate CNC G-code for improved machining performance.

This system bridges the gap between **theoretical machining optimization and real-world CNC implementation**.

---
# Project Motivation

Medium-Density Fibreboard (MDF) is widely used in furniture manufacturing and interior applications due to its uniform structure and affordability. However, MDF machining presents several challenges:

rapid tool wear due to abrasive fibres

high cutting forces

elevated cutting temperatures

vibration instability

poor surface finish

Traditional CNC machining often uses aggressive cutting strategies with large depths of cut and high feed rates. While this reduces machining time, it significantly degrades machining quality and tool life.

Existing research has explored optimization methods such as:

•Taguchi optimization
• Regression models
• Response Surface Methodology
• Machine Learning Prediction

However, these approaches typically recommend optimal parameters without directly modifying CNC machining instructions (G-code).

This project addresses that gap by:

• predicting machining responses using physics-informed models and machine learning
• optimizing machining parameters using a Genetic Algorithm
• automatically regenerating optimized CNC G-code for real machine execution


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

                 ┌─────────────────────┐
                 │ Original CNC G-code │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   G-code Parser     │
                 └──────────┬──────────┘
                            │
                            ▼
               ┌─────────────────────────┐
               │ Physics-Based Models    │
               │ Cutting force           │
               │ Surface roughness       │
               │ Tool wear               │
               │ Vibration               │
               │ Temperature             │
               └──────────┬──────────────┘
                          │
                          ▼
              ┌──────────────────────────┐
              │ Synthetic Dataset        │
              │ Generation               │
              └──────────┬───────────────┘
                         │
                         ▼
             ┌───────────────────────────┐
             │ Machine Learning Model    │
             │ CatBoost / Random Forest  │
             └──────────┬────────────────┘
                        │
                        ▼
           ┌─────────────────────────────┐
           │ Genetic Algorithm Optimizer │
           └──────────┬──────────────────┘
                      │
                      ▼
           ┌─────────────────────────────┐
           │ Regenerate Optimized G-code │
           └──────────┬──────────────────┘
                      │
                      ▼
              Optimized CNC Machining


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
# Physics-Based Machining Models

Key machining responses are estimated using physics-informed equations.

1. Cutting Force

   Fc = Cf (vc/120)^αvc (fz/0.08)^αfz ap^αap w^αw
   
Where:

vc = cutting speed
fz = feed per tooth
ap = depth of cut
w = width of cut
D = tool diameter

Additional corrections incorporate:

rake angle

relief angle

helix angle

chip thinning factor

2. Surface Roughness

Surface roughness is estimated using feed per tooth and tool geometry relationships with dynamic corrections for machining conditions.

3. Tool Wear Rate

Tool wear rate is modeled as a function of:

cutting speed

feed per tooth

depth of cut

tool geometry

4. Additional Responses

The system also predicts:

• vibration amplitude
• cutting temperature
• chip load deviation
• spindle power consumption

These responses collectively describe machining stability and tool health.

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

