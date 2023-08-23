import imports.own.will_go_to_start
from imports.own.matrix_start import matrix_start
from imports.own.author_start import author_start
from imports.own.ukraine_start import ukraine_start

def Pictures():

    if imports.own.will_go_to_start.x.lower() == "author": # author (+)
        
        author_start()

    elif imports.own.will_go_to_start.x.lower() == "ukraine": # ukraine (+)

        ukraine_start()

    elif imports.own.will_go_to_start.x.lower() == "matrix": # matrix (+)
        
        matrix_start()