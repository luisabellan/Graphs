
def earliest_ancestor(ancestors, starting_node):
    
    # si starting_node no tiene padre, es el earliest ancestor, así que
    # return starting_node

    # mirar si starting_node tiene padres
        # si tiene varios padres
            # elegir el más pequeño
        # si  tiene un padre
            # convertir padre en starting_node, es decir,
            # volver a ejecutar earliest_ancestor(ancestors,starting_node=padre)





# Driver code 
if __name__ == '__main__': 

    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

  
  
    starting_node = 6
    earliest_ancestor(ancestors, starting_node) 