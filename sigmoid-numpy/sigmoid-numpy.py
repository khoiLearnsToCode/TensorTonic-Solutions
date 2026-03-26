import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    Handles scalars, lists, and NumPy arrays.
    """
    # Convert input to a NumPy array to ensure element-wise operations work safely
    x = np.array(x) 
    
    return 1 / (1 + np.exp(-x))