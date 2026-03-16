def parse_gcode(file_path):

    commands = []

    with open(file_path) as f:
        for line in f:
            commands.append(line.strip())

    return commands
