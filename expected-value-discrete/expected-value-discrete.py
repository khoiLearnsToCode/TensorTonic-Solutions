import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    E = 0
    cumulative_p = 0
    for i in range(len(x)):
        cumulative_p += p[i]
        if (cumulative_p > 1.0):
            raise ValueError("ValueError")
        E += x[i]*p[i]

    if (cumulative_p < 1.0):
        raise ValueError("ValueError")
        
    return E
