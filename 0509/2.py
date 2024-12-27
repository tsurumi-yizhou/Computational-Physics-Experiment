import math

def calculate_pi_errors(approximations):
    """
    Calculate the absolute and relative errors for given approximations of pi.

    :param approximations: A list of tuples (numerator, denominator) or integers
    :return: None (prints the results)
    """
    true_pi = math.pi
    for approx in approximations:
        # Determine the approximate value of pi
        if isinstance(approx, tuple):  # If it's a fraction
            approx_value = approx[0] / approx[1]
            approx_str = f"{approx[0]}/{approx[1]}"
        else:  # If it's an integer
            approx_value = approx
            approx_str = str(approx)

        # Calculate errors
        absolute_error = abs(approx_value - true_pi)
        relative_error = (absolute_error / true_pi) * 100

        # Print results
        print(f"Approximation: {approx_str}")
        print(f"  Approximate Value: {approx_value}")
        print(f"  Absolute Error: {absolute_error:.10f}")
        print(f"  Relative Error: {relative_error:.10f}%\n")

# List of approximations: (numerator, denominator) for fractions, integers for whole numbers
approximations = [(22, 7), (223, 71), (355, 113)]
calculate_pi_errors(approximations)
