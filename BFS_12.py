"""
Coursera - BFS, and connected components
"""

EX_GRAPH0 = {0: set([1,2]),
             1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
EX_GRAPH2 = {0: set([1,4,5]),
             1: set([2,6]),
             2: set([3,7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1,2]),
             9: set([0,3,4,5,6,7])}

EX_GRAPH3 = {0: set([]),
             1: set([2]),
             2: set([3]),
             3: set([5]),
             4: set([2,3]),
             5: set([]),
             6: set([]),
             7: set([8]),
             8: set([])}

def bfs_visited(ugraph, start_node):
    """
    the set of all nodes visited by algorythm
    """
    visited = set([start_node])

    queue = [start_node]
  
    while len(queue) > 0 :
        node = queue.pop(0)
        neighbors = ugraph[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
 
    return visited

def if_nodes_in_set(list_of_nodes, list_of_node_sets):
    """
    funkcja sprawdza czy istnieje set w ktorym jest szukany node:
    
    
    funckja zwraca:
    (is_in_set, set) 
    is_in_set is true when node in set
    set - set where was node we were searching for 
    """
 
    #print list_of_nodes,list_of_node_sets
    
    #list of all set that have at least one number from 
    #list_of_nodes
    common_sets = []
    
    if list_of_node_sets ==[]:
        return False, []
    is_node_in_set = False
    for node in list_of_nodes:
        for set_of_nodes in list_of_node_sets:
            if node in set_of_nodes:
                is_node_in_set = True
                if set_of_nodes not in common_sets:
                    common_sets.append(set_of_nodes)
                
    return is_node_in_set, common_sets

def cc_visited(ugraph):
    """
    return the list of sets - connected component in graph
    """
    remaning = list(ugraph)

    connected_comp = []
   
    while len(remaning) > 0 :
        node = remaning.pop(0)

        visited_by_bfs = bfs_visited(ugraph, node)

        # is_connected = (True/False, (list of connected sets))
        is_connected =  if_nodes_in_set(visited_by_bfs, connected_comp)

        if is_connected[0] == False:
            connected_comp.append(visited_by_bfs)
        else:
            big_set = set(visited_by_bfs)
            for connected_set in is_connected[1]:
                #print "connected_set ", connected_set
                connected_comp.remove(connected_set)
                big_set = big_set.union(connected_set)
            connected_comp.append(big_set)    
#    print "-----#---"
#    print connected_comp   
    
    return connected_comp

def largest_cc_size(ugraph):
    """
    return the size of largest connected component
    """
    connected_comp = cc_visited(ugraph)
    max_set = 0
    for set_of_nodes in connected_comp:
        len_of_set = len(set_of_nodes)
        if len_of_set > max_set:
            max_set = len_of_set
    return max_set    


def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, 
    a list of nodes attack_order
    and iterates through the nodes in attack_order.
    For each node in the list, 
    the function removes the given node
    and its edges from the graph
    and then computes the size of the 
    largest connected component for the resulting graph
    
    The function should return a list
    whose k+1th entry is the size of the largest connected component
    in the graph after the removal
    of the first k nodes in attack_order.
    The first entry (indexed by zero) is the size of the largest connected component in the original graph.
    
    """
    new_ugraph = dict(ugraph)
    return_list = [largest_cc_size(new_ugraph)]
    
    
    for node_to_remove in attack_order:
        del new_ugraph[node_to_remove]
        
        for node_set in new_ugraph:
            if node_to_remove in new_ugraph[node_set]:
                new_ugraph[node_set].difference_update(set([node_to_remove]))

        
        #print "new_ugraph", new_ugraph
        return_list.append(largest_cc_size(new_ugraph))
        
        
    return   return_list  
    
    
def run_test():  
    """
    "do testowania
    """
    
    #print bfs_visited(EX_GRAPH1, 0)
    ugraph = EX_GRAPH3
    
    print "largest" , largest_cc_size(ugraph)
    
    attack_order = [3,7,2]
    print "compute_resilience", compute_resilience(ugraph, attack_order)
    return cc_visited(ugraph)



#print run_test()