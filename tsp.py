from nodes_generator import NodeGenerator
from simulated_annealing import SimulatedAnnealing


def main():
    '''set the simulated annealing algorithm params'''
    temp = 1000
    stopping_temp = 0.00000001
    alpha = 0.9995
    stopping_iter = 10000000

    '''set the dimensions of the grid'''
    size_width = 400
    size_height = 400

    '''set the number of nodes'''
    population_size = 9

    '''generate random list of nodes'''
    nodes = NodeGenerator(size_width, size_height).generate()
    #nodes = ([[1, 2], [5, 6] [7, 3], [8, 4]])
    print(nodes)
    print("Type: ",type(nodes))

    '''run simulated annealing algorithm with 2-opt'''
    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
    sa.anneal()

    '''animate'''
    sa.animateSolutions()

    '''show the improvement over time'''
    sa.plotLearning()


if __name__ == "__main__":
    main()
