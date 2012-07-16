# Tarjan's
# Input is a directed graph, G
# Computes strongly connected components in O(m + n) time,
# where n and m  are the number of nodes and edges, respectively
import sys, resource, time

# Increase recursion limit and stack size
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))

# Establish source of directed graph, G
# Source file has one directed edge per line, e.g. "1 5" is one line
source = "SCC.txt" 
# Number of nodes
n = 875714

def Tarjan(G):
    """ Returns strongly connected components in the form of a dictionary,
    where the key is the node and the value identifies which SCC
    the key belongs to """
    global SCC
    SCC = {}
    DFS_Loop(G)
    g_values = G.values()
    return SCC

def DFS_Loop(G): # Was DFS LOOP
    global index, stack, current_stack, current_index, lowlink, scc_index
    # Initialize all nodes as unexplored
    index = {}
    current_index = 0
    scc_index = 0
    stack = []
    current_stack = {}
    lowlink = {}
    # Explore each adjacent node i (if unexplored)
    for i in range(n,0,-1):
        if i not in index:
            DFS(G,i)
    return

def DFS(G,i):
    global current_index, scc_index
    # Run Depth First Search
    index[i] = current_index
    lowlink[i] = current_index
    current_index += 1
    # Push current value onto stack
    stack.append(i) 
    # For faster search, place values of stack into hash table (dict)
    current_stack[i] = 1 
    # For each arc (i,j) in G, if j is not yet explored, recurse on j
    for j in G[i]:
        # If j not visited, recurse on j
        if j not in index:
            DFS(G,j)
            lowlink[i] = min(lowlink[i],lowlink[j])
        # If j is in stack, it is in the current SCC
        elif j in current_stack:
            lowlink[i] = min(lowlink[i],index[j])
    # If i is a root node, pop the stack and generate SCC
    if lowlink[i] == index[i]:
        # Pop stack until the stack value is i and
        # give the SCC a unique value scc_index
        while stack[-1] != i:
            SCC[stack[-1]] = scc_index
            del current_stack[stack[-1]]
            del stack[-1]
        if stack[-1] == i:
            SCC[stack[-1]] = scc_index
            del current_stack[stack[-1]]
            del stack[-1]
        scc_index += 1
    return
   
def get_graph():
    # Grabs graph from input file
    # Create dictionary with a key for each node
    G = {}
    for i in range(1,n+1):
        G[i] = []
    # Populate dictionary with information from file
    file = open(source)
    for line in file:
        list = line.split()
        i = int(list[0])
        j = int(list[1])
        G[i].append(j)
    file.close()
    return G

def most_common(lst,x):
    # This functions returns the 'x' most common elements from 'lst' 
    from collections import Counter
    c = Counter(lst)
    result = []
    for number,count in c.most_common(x):
        result.append(count)
    return result

if __name__=="__main__":
    start = time.time()
    G = get_graph()
    print "Graph grabbed in", time.time() - start,"seconds"

    start = time.time()
    result = Tarjan(G)
    print "Tarjan's algorithm ran in", time.time() - start,"seconds"

    print "Size of the top 5 strongly connected components:"
    print most_common(result.values(),5)
