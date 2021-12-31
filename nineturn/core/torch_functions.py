"""pytorch specific common functions."""

import torch as th
from numpy import ndarray


def _to_tensor(arr: ndarray) -> th.Tensor:
    """Convert a numpy array to torch tensor."""
    return th.from_numpy(arr)
