import math

def calculate_pi_errors(approx_pi):
    """
    Calculate the absolute and relative errors of a given approximation of pi.

    :param approx_pi: The approximated value of pi
    :return: A tuple containing the absolute error and relative error percentage
    """
    true_pi = math.pi  # The true value of pi
    absolute_error = abs(approx_pi - true_pi)
    relative_error = (absolute_error / true_pi) * 100
    return absolute_error, relative_error

# Example usage
approximations = [3.14, 22/7, 3.1416, 3.14159]
for approx in approximations:
    abs_error, rel_error = calculate_pi_errors(approx)
    print(f"Approximation: {approx}")
    print(f"  Absolute Error: {abs_error:.10f}")
    print(f"  Relative Error: {rel_error:.10f}%\n")
