
def earliest_ancestor(ancestors, starting_node):
    

    parents = []
    solution = -1

    

    
    # mientras el starting_node tenga padres

    
    # encontrar padre
    for (x,y) in ancestors:

        


        if y == starting_node:
            # print(x)
            parents.append(x)
            # print(parents)
            # if len(parents) == 0:
            #     solution = -1
            #     starting_node = solution
            #     # print(solution)
            #     earliest_ancestor(ancestors, starting_node)
            #     return solution

            if len(parents) == 1 or len(parents) == 2:
                solution = min(parents)
                # print(solution)
                starting_node = solution
                earliest_ancestor(ancestors, starting_node)
            else:
                solution = -1
                starting_node = solution
                earliest_ancestor(ancestors, starting_node)
            
    print(solution)
    return solution
            
        



        
        

            

    

        # elif len(parents) == 0:
        
        
        

      
            
            
                
        

        # si starting_node no tiene padre, es el earliest ancestor, así que
     
    

        # si tiene varios padres
            # elegir el más pequeño
        # si  tiene un padre
            # convertir padre en starting_node, es decir,
            # volver a ejecutar earliest_ancestor(ancestors,starting_node=padre)





# Driver code 
# if __name__ == '__main__': 

#     ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

  
  
#     starting_node = 7
#     earliest_ancestor(ancestors, starting_node) 