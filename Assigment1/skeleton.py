import typing
import random
import matplotlib.pyplot as plt
import numpy as np

# python -m venv myenv
# source myenv/bin/activate
# pip3 install package_name

class CellularAutomata:
    """Skeleton CA, you should implement this."""

    def __init__(self, rule_number: int):
        """Intialize the cellular automaton with a given rule number"""
        self.rule_number = rule_number

    def __call__(self, c0: typing.List[int], t: int) -> typing.List[int]:
        """Evaluate for T timesteps. Return Ct for a given C0."""
        currentState = c0.copy()
        result = np.zeros(c0.size, dtype=int)

        longestStringOfZeroesGraph = []
        numberOfZeroesGraph = []
        
        for i in range(t):
            for j in range(1, len(c0) - 1):
                neigbourhood = currentState[j - 1]
                neigbourhood = (neigbourhood << 1) | currentState[j]
                neigbourhood = (neigbourhood << 1) | currentState[j + 1]
                result[j] = (self.rule_number >> neigbourhood) & 1
            currentState = result.copy()

            # number of zero's
            numberOfZeroesGraph.append((i, self.numberOfZeroes(result)))
            # longest string of equal symbols
            longestStringOfZeroesGraph.append((i, self.longestStringOfEqualSymbols(currentState)))
            
        return (result, numberOfZeroesGraph, longestStringOfZeroesGraph)
        # returns list
    
    @classmethod
    def numberOfZeroes(self, array):
        numberOfZeroes = 0
        for i in range(array.size):
            if (array[i] == 0):
                numberOfZeroes += 1
        return numberOfZeroes

    @classmethod
    def longestStringOfEqualSymbols(self, array):
        numberOfEqualCharacters = 0
        longestNumberOfEqualCharacters = 0
        for i in range(1, array.size ):
            if (array[i] == array[1]):
                numberOfEqualCharacters += 1
            else:
                if (numberOfEqualCharacters > longestNumberOfEqualCharacters):
                    longestNumberOfEqualCharacters = numberOfEqualCharacters
                numberOfEqualCharacters = 0
        if (numberOfEqualCharacters > longestNumberOfEqualCharacters):
            longestNumberOfEqualCharacters = numberOfEqualCharacters
        return longestNumberOfEqualCharacters

    @classmethod
    def experiment(cls, rule_number, t=1):
        # Initialize empty lists to accumulate data
        all_longest_strings = []
        all_number_of_zeroes = []
        
        for i in range (0, 5):
            # Initialize an array of random 0s and 1s
            c0 = np.random.choice([0, 1], size=experimentArraySize, replace=True, p=[0.5, 0.5])

            # Ensure at least one element is 1
            if np.sum(c0) == 0:
                # If there are no 1s, set a random element to 1
                random_index = np.random.randint(0, experimentArraySize)
                c0[random_index] = 1
            
            ca = cls(rule_number)
            ct_prime, numberOfZeroesGraphData, longestStringOfZeroesGraphData = ca(c0, t)
            
            all_longest_strings.append(longestStringOfZeroesGraphData)
            all_number_of_zeroes.append(numberOfZeroesGraphData)
        
        # Create a single plot with multiple lines
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

        line_styles = ['-', '--', '-.', ':']
        
        # Plot each element in all_longest_strings as a separate line
        for i, longestStringData in enumerate(all_longest_strings):
            x_values1, y_values1 = zip(*longestStringData)
            ax1.plot(x_values1, y_values1, linewidth=1, linestyle=line_styles[i % 4])

        # Plot each element in all_number_of_zeroes as a separate line
        for i, numberOfZeroesData in enumerate(all_number_of_zeroes):
            x_values2, y_values2 = zip(*numberOfZeroesData)
            ax2.plot(x_values2, y_values2, linewidth=1, linestyle=line_styles[i % 4])

        # Set the y-axis to a logarithmic scale
        # ax1.set_yscale('log')
        ax1.set_xlabel('Timestep T')
        ax1.set_ylabel('Longest String of Equal Symbols')
        ax1.set_title('Longest String of Equal Symbols for Different initial States')
        ax1.grid(True)
        
        # ax2.set_yscale('log')
        ax2.set_xlabel('Timestep T')
        ax2.set_ylabel('Number of Zero Cells')
        ax2.set_title('Number of Zero Cells for Different initial States')
        ax2.grid(True)

        plt.tight_layout()

        # Save the plot as an image file (e.g., PNG)
        plt.savefig('rule_' + str(rule_number) + '_plot.png')

        # Show the plot
        plt.show()
        
        # Clear the current figure
        plt.clf()
        

        
    @classmethod
    def test(cls, rule_number, c0, ct, t=1):
        ca = cls(rule_number)
        ct_prime = ca(c0, t)
        assert all(trial == expected for trial, expected in zip(ct_prime, ct))



if __name__ == "__main__":
    "If the following statements do not produce an error, your CA works correctly."
    experimentArraySize = 60

    numberOfTimeStepsExperiment = 100
    # Wolfram Class I
    WolframClassIRulenumber = 40
    CellularAutomata.experiment(WolframClassIRulenumber, numberOfTimeStepsExperiment)
    
    # Wolfram Class II
    WolframClassIRulenumber = 29
    CellularAutomata.experiment(WolframClassIRulenumber, numberOfTimeStepsExperiment)
    
    # Wolfram Class III
    WolframClassIRulenumber = 30
    CellularAutomata.experiment(WolframClassIRulenumber, numberOfTimeStepsExperiment)
    
    # Wolfram Class IV
    WolframClassIRulenumber = 54
    CellularAutomata.experiment(WolframClassIRulenumber, numberOfTimeStepsExperiment)

    
# 0: [0 0 0 1 0 0 0]

# 1: [0 0 1 1 1 0 0]

# 2: [0 1 1 0 0 1 0]

# t:

# 000 001 010 011 100 101 110 111
#  0   0   0   0   0   0   0   0 


