import numpy as np
import pandas as pd
from .physics_models import *

def generate_dataset(n_samples=5000):

    data = []

    for _ in range(n_samples):

        spindle = np.random.uniform(500, 17000)
        feed = np.random.uniform(100, 8000)
        depth = np.random.uniform(1, 10)

        tool_diameter = 6
        flutes = 3
        width_cut = np.random.uniform(2, 6)

        vc = cutting_speed(tool_diameter, spindle)
        fz = feed_per_tooth(feed, spindle, flutes)

        Fc = cutting_force(vc, fz, depth, width_cut)
        Ra = surface_roughness(fz)
        TWR = tool_wear_rate(vc, fz, depth, width_cut)
        temp = cutting_temperature(Fc, vc, depth, width_cut)
        cld = chip_load_deviation(fz)
        power = power_consumption(Fc, vc)

        data.append([
            spindle, feed, depth,
            Fc, Ra, TWR, temp, cld, power
        ])

    columns = [
        "spindle_speed",
        "feed_rate",
        "depth_of_cut",
        "cutting_force",
        "surface_roughness",
        "tool_wear_rate",
        "temperature",
        "chip_load_deviation",
        "power"
    ]

    return pd.DataFrame(data, columns=columns)
