import random
import numpy as np
from deap import base, creator, tools, algorithms


def optimize(model, scaler, fixed_spindle_speed=12000):
    # Avoid re-creating DEAP classes if script is run multiple times
    if not hasattr(creator, "FitnessMin"):
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    if not hasattr(creator, "Individual"):
        creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()

    toolbox.register("feed", random.uniform, 100, 8000)
    toolbox.register("depth", random.uniform, 1, 10)

    toolbox.register(
        "individual",
        tools.initCycle,
        creator.Individual,
        (toolbox.feed, toolbox.depth),
        n=1
    )

    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def objective(individual):
        feed, depth = individual

        X_raw = np.array([[fixed_spindle_speed, feed, depth]])
        X_scaled = scaler.transform(X_raw)

        preds = model.predict(X_scaled)[0]

        # Expected prediction order:
        # cutting_force, surface_roughness, tool_wear_rate,
        # temperature, chip_load_deviation, power
        cutting_force = preds[0]
        surface_roughness = preds[1]
        tool_wear = preds[2]
        temperature = preds[3]
        chip_load_dev = preds[4]
        power = preds[5]

        # Weighted objective
        cost = (
            0.25 * cutting_force +
            0.25 * surface_roughness +
            0.20 * tool_wear +
            0.15 * temperature +
            0.10 * chip_load_dev +
            0.05 * power
        )

        return (cost,)

    toolbox.register("evaluate", objective)
    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=200, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    population = toolbox.population(n=30)

    algorithms.eaSimple(
        population,
        toolbox,
        cxpb=0.5,
        mutpb=0.2,
        ngen=25,
        verbose=False
    )

    best = tools.selBest(population, 1)[0]
    return best
