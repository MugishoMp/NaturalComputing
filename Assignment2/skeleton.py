import ioh
import numpy as np
import statistics 

class RandomSearch:
    def __call__(self, problem: ioh.ProblemType):
        """You should implement (random) search behaviour here"""


class YourAlgorithm:
    
    def __CalculateStartingTemperature (self, problem: ioh.ProblemType, fixed_state):
        # calculate standard deviation of the cost for 200 starting states. 
        # whatever the standard deviation turns out to be will be our starting
        # temperature
        listOfDifferences = []
        temp_state = fixed_state.copy()
        for i in range(1,100):
            temp_state = self.__NextState(temp_state)
            listOfDifferences.append(problem.__call__(temp_state))
        return (statistics.pstdev(listOfDifferences))
    
    
    def __NextState (self, state):
        # Choose a random index in the array
        random_index = np.random.randint(0, len(state) - 1)

        # Flip the value at the chosen index
        state[random_index] = 1 - state[random_index]

        return state
    
    
    # we will use simulated annealing
    def __call__(self, problem: ioh.ProblemType):
        """You should implement search behaviour here"""
        
        # initialize start state
        
        start_state = np.random.choice([0, 1], size=800)
        state = start_state.copy()
        
        
        # starting temperature
        temperature = self.__CalculateStartingTemperature(problem, start_state)
        
        # cooling rate
        cooling_rate = 0.99
        
        freezing_temperature = 0.1
        
        while (temperature > freezing_temperature):
            state
            potential_next_state = self.__NextState(state.copy())
            
            score_state = problem.__call__(state)
            score_potential_next_state = problem.__call__(potential_next_state)
            
            if (score_potential_next_state > score_state):
                #accept this potential next state
                state = potential_next_state
            else:
                score_delta = score_potential_next_state - score_state
                # print(score_delta)
                
                
                probability = 1 / (1 + np.exp(-score_delta / temperature))
                # print(probability)
                random_number = np.random.uniform(1, 0, 1)
                
                if (random_number <= probability):
                    state = potential_next_state
                    
            temperature = temperature * cooling_rate
            print(temperature)
                
        
        
        # generate random states
        # a state should be a list of 800 items state[800]
        
        # writing a cost function: 
        # __call__ is our cost function
        # cost(problem, state)
        
        
        # calculate the number of states or iterations for each temperature
        
        
        
        


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
            
            # Perform multiple optimization runs
            for run in range(n_runs):
                # Make a new instance of you algorithm in every run
                optimizer = alg()
                # Perform the optimization run
                optimizer(problem)
                # Reset the problem such that its state is correct
                problem.reset()
                
                
