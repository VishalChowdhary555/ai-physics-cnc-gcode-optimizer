# src/config.py

# MDF material constants
MDF_DENSITY = 750
IDEAL_CHIP_LOAD = 0.08

# Machine limits
MAX_SPINDLE_SPEED = 18000
MIN_SPINDLE_SPEED = 500

MAX_FEED_RATE = 8000
MIN_FEED_RATE = 100

MAX_DEPTH_OF_CUT = 10
MIN_DEPTH_OF_CUT = 1

# Genetic algorithm weights
WEIGHTS = {
    "cutting_force": 0.25,
    "surface_roughness": 0.25,
    "tool_wear": 0.2,
    "temperature": 0.15,
    "vibration": 0.15
}
