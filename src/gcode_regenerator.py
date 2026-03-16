import re


def regenerate_gcode(gcode, new_feed, new_depth):
    optimized = []

    current_z = None

    for line in gcode:
        updated_line = line

        # Replace feed rate values like F8000
        if "F" in updated_line:
            updated_line = re.sub(r"F[-+]?\d*\.?\d+", f"F{new_feed:.2f}", updated_line)

        # Replace Z depth values only on motion lines containing Z
        if "Z" in updated_line:
            updated_line = re.sub(r"Z[-+]?\d*\.?\d+", f"Z{-abs(new_depth):.2f}", updated_line)

        optimized.append(updated_line)

    return optimized
