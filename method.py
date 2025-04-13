import time

# Algorithms

def cube_root(num : float, epsilon : float = 0.01) -> dict:
    """
    Calculate the cube root of a given number.
    Using Bisection Method.
    
    Args:
        number (float): The number to calculate the cube root of.

    Returns:
        float: The cube root of the given number.
    """
    sign = -1 if num < 0 else 1 # To account for negative numbers
    low, high = 0, abs(num)
    
    guess = 0
    steps = 0

    begin = time.time()  # Get time at start of loop

    while high - low > epsilon:
        guess = (low + high)/2  # Using bisection method to find the centre of each of the numbers

        if guess**3 < num:
            #This accounts for cases after bisection when the number has not gotten close to the value
            low = guess
        elif guess**3 > num:
            #This changes the high value to the guess and indicates that yu are getting closer to the value so it keeps bisecting till we get to the value.
            high = guess
        else:
        #This gives us the value of guess.
            break
        
        steps += 1
        
    finish = time.time()  # Get time at end of loop
    return {'ans': guess*sign, 'steps': steps, 'time-taken': finish - begin}


def exhaustive__cube_root(num : float) -> dict:
    """
    Finds the cube root of numbers correct to 2 decimal places
    Exhaustive search method
    """
    i = 0
    steps = 1
    state = num
    num = abs(num)
    start = time.time()
    while i <= num:
        if i**3 > num:
            for j in range(10):
                if (i-1+j/10)**3 > num:
                    for k in range(10):
                        steps += 1
                        if (i-1+(j-1)/10 + k/100)**3 > num:
                            res = i-1+(j-1)/10 + (k-1)/100
                            if state < 0:
                                res = res*-1
                            end = time.time()
                            return {'ans': res, 'steps': steps, 'time-taken': end - start }
                else:
                    steps += 1
        else:
            steps += 1
        i += 1

def is_prime(number : int) -> str:
    if number % 2 == 0:
        #Checking if factor is 2
        return False
    for factors in range(3, int(number/2), 2):
        # Checks from all numbers from 3 to half of the number with an increment of a number to check if they are factors
        if number % factors == 0:
            # If a factor is found, the number is not prime
            return False    
    return True