def regenerate_gcode(gcode, new_feed, new_depth):

    optimized = []

    for line in gcode:

        if "F" in line:
            line = f"F{new_feed}"

        optimized.append(line)

    return optimized
