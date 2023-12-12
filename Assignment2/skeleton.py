import ioh


class RandomSearch:
    def __call__(self, problem: ioh.ProblemType):
        """You should implement (random) search behaviour here"""


class YourAlgorithm:
    def __call__(self, problem: ioh.ProblemType):
        # we will use simulated annealing
        """You should implement search behaviour here"""


if __name__ == "__main__":
    # These are all the problems we need to test on
    problems = [
        ioh.get_problem(pid, problem_class=ioh.ProblemClass.GRAPH) 
        for pid in [2000, 2001, 2002, 2003, 2004]
    ]

    # Because our algortihm is stochastic we need to perform multiple runs
    n_runs = 10
    
    # We loop over both algorithms
    for alg in (RandomSearch, YourAlgorithm):
        name = alg.__name__
        
        # We instantiate a logger
        logger = ioh.logger.Analyzer(algorithm_name=name, folder_name=name)

        # We loop over all problems
        for problem in problems:
            
            print(problem)
            # Perform multiple optimization runs
            for run in range(n_runs):
                # Make a new instance of you algorithm in every run
                optimizer = alg()
                # Perform the optimization run
                optimizer(problem)
                # Reset the problem such that its state is correct
                problem.reset()
                
                
