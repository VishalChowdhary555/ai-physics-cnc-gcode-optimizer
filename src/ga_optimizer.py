import random
import numpy as np
from deap import base, creator, tools, algorithms


def optimize(model):

    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()

    toolbox.register("feed", random.uniform, 100, 8000)
    toolbox.register("depth", random.uniform, 1, 10)

    toolbox.register("individual",
        tools.initCycle,
        creator.Individual,
        (toolbox.feed, toolbox.depth),
        n=1
    )

    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    def objective(ind):

        feed, depth = ind

        X = np.array([[12000, feed, depth]])
        preds = model.predict(X)[0]

        cost = sum(preds)

        return (cost,)

    toolbox.register("evaluate", objective)

    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=30)

    algorithms.eaSimple(pop, toolbox,
                        cxpb=0.5,
                        mutpb=0.2,
                        ngen=20,
                        verbose=False)

    best = tools.selBest(pop, 1)[0]

    return best
