import numpy as np


def entropy(probs):
    """Assumes that input is a numpy array and that it is a valid prob vector."""
    entropy_value= -(probs * np.log(probs))
    return entropy_value

if __name__ == "__main__":
    pass
