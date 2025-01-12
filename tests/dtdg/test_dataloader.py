#!/usr/bin/env python
# flake8: noqa
"""Tests `nineturn.dtdg.dataloader` package."""

import numpy as np
from tests.core.common_functions import *


def test_ogb_dataset_tf():
    clear_background()
    """Test that citation graph could support different backend."""
    from nineturn.core.config import set_backend
    from nineturn.core.backends import TENSORFLOW

    set_backend(TENSORFLOW)
    from nineturn.dtdg.dataloader import ogb_dataset, supported_ogb_datasets

    data_to_test = supported_ogb_datasets()[1]
    this_graph = ogb_dataset(data_to_test)
    for s in range(len(this_graph)):
        this_graph.dispatcher(s)


def test_ogb_dataset_torch():
    clear_background()
    """Test that citation graph could support different backend."""
    from nineturn.core.config import set_backend
    from nineturn.core.backends import PYTORCH

    set_backend(PYTORCH)
    from nineturn.dtdg.dataloader import ogb_dataset, supported_ogb_datasets

    data_to_test = supported_ogb_datasets()[1]
    this_graph = ogb_dataset(data_to_test)
    for s in range(len(this_graph)):
        this_graph.dispatcher(s)
