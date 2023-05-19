from board import Board
from minmax import MinMax
from alphabeta import AlphaBeta
import time
import matplotlib.pyplot as plt

initial_state = Board()


# Measure the performance of the minimax algorithm
def run_minimax(initial_state):
    start_time = time.time()
    minmax= MinMax(depth=5)
    best_move = minmax.get_move(initial_state)
    end_time = time.time()
    execution_time = end_time - start_time
    return best_move, execution_time

# Measure the performance of the alphabeta algorithm
def run_alphabeta(initial_state):
    start_time = time.time()
    alphabeta = AlphaBeta(depth=5)
    best_move = alphabeta.get_move(initial_state)
    end_time = time.time()
    execution_time = end_time - start_time
    return best_move, execution_time


best_move_minimax, time_minimax = run_minimax(initial_state)
print("Best move with minimax:", best_move_minimax)
print("Execution time with minimax:", time_minimax)

best_move_alphabeta, time_alphabeta = run_alphabeta(initial_state)
print("Best move with alphabeta:", best_move_alphabeta)
print("Execution time with alphabeta:", time_alphabeta)


# Define the x-axis labels
labels = ["Minimax", "Alphabeta"]

# Define the y-axis values
values = [time_minimax, time_alphabeta]

# Create a bar chart to compare the execution times
plt.bar(labels, values)

# Add a title and axis labels
plt.title("Execution times of Minimax and Alphabeta algorithms")
plt.xlabel("Algorithm")
plt.ylabel("Execution time (seconds)")

# Show the chart
plt.show()