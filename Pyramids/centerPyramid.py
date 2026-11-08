def centerPyramid(n: int):
    "n = int, represents the levels of the pyramid"
    "A pyramid of '*' should be printed from the center,"
    "with the first line being the top of the pyramid"
    #if n is pair, top of pyramid will be two blocks
 # if n is even, top of pyramid will be two blocks
    if n % 2 == 0:
        # range(n-1, -1, -1) and range(n) both generate exactly 'n' steps
        for i, j in zip(range(n - 1, -1, -1), range(n)):
            print(" " * i + "*" * (2 * j + 2))
          
    # if n isn't even, top of pyramid will be one block 
    else: 
        for i, j in zip(range(n - 1, -1, -1), range(n)):
            print(" " * i + "*" * (2 * j + 1))