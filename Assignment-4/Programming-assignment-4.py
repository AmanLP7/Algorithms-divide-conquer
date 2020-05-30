##-------- Thanks to - https://gist.github.com/aymanfarhat/6098683
##-------- Thanks to - https://medium.com/@dev.elect.iitd/kargers-algorithm-d8067eb1b790


##---------------------- Karger minimum cut algorithm implementation ----------------------##

# Importing required modules
from random import randint
from re import sub

# Function to import graph from a text file
'''
Input: Text file containing graph
Output: Dictionary containing graph
'''
def importGraph(filename="kargerMinCut.txt"):

  graph = {}

  with open(filename) as file:
    data = file.readlines()

  data = [sub("\\t", " ", x.strip("\n")) for x in data]
  data = list(map(lambda x: x.strip().split(" "), data))
  data = list(map(lambda x: [int(ele) for ele in x], data))

  # Converting list into dictionary
  for elements in data:
    graph[elements[0]] = elements[1:]

  return graph


# Function to get random edge from a graph
'''
Input: Graph as a dictionary
Output: Nodes of an edge as tuple
'''
def getRandomEdge(graph):

  node1 = list(graph.keys())[randint(0, len(graph) - 1)]
  node2 = graph[node1][randint(0, len(graph[node1]) - 1)]

  return (node1, node2)


# Function to perform edge contractions
'''
Input: A random edge from graph
Output: Contracted graph
'''
def contractEdge(graph, edge):

  # merge v2 into v1 and remove v2 from graph
  node1 = graph[edge[0]]
  node1.extend(graph[edge[1]])
  del graph[edge[1]]

  #replace all occurnces of v2 value with v1
  for key, _ in graph.items():
    graph[key] = [edge[0] if x == edge[1] else x for x in graph[key]]

  # Remove all edges of v1 to itself(loops)
  graph[edge[0]] = [x for x in graph[edge[0]] if x != edge[0]]

  return graph


# Function to count minimum cuts in a graph
'''
Input: A graph as a dictionary
Output: Minimum cuts
'''
def findMinimumCut(graph):


  while (len(graph) > 2):
    graph = contractEdge(graph, getRandomEdge(graph))

  return len(list(graph.values())[0])



if __name__ == "__main__":


  minimumCuts = []
  for iteration in range(300):

    # testGraph = {
    #     1: [2, 4],
    #     2: [1, 3, 4],
    #     3: [2, 4],
    #     4: [1,2,3]
    #   }
    graph = importGraph(filename="kargerMinCut.txt")

    minimumCuts.append(findMinimumCut(graph))

  print(min(minimumCuts))





