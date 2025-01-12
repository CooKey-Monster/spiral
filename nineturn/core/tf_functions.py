"""Tensorflow specific common functions."""
from typing import List

import tensorflow as tf
from numpy import ndarray


def _to_tensor(arr: ndarray) -> tf.Tensor:
    """Convert a numpy array to tensorflow tensor."""
    return tf.constant(arr)


def nt_layers_list() -> List:
    return []


def reshape_tensor(h: tf.Tensor, new_shape:List[int]) -> tf.Tensor:
    return tf.reshape(h,new_shape)
