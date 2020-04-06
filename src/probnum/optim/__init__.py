"""
(Bayesian) Optimization.

Bayesian optimization is a sequential design strategy for global optimization of a (black-box) function (without
requiring derivatives). The optimizer builds an internal model of the function it is optimizing and chooses evaluation
points based on it.
"""

# Public classes and functions. Order is reflected in documentation.

from .objective import *
from .linesearch import *
from .stoppingcriterion import *

__all__ = ["LineSearch", "ConstantLearningRate", "BacktrackingLineSearch",
           "Objective", "Eval",
           "StoppingCriterion", "NormOfGradient", "DiffOfFctValues"]