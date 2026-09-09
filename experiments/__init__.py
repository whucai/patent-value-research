"""Experiment package for the patent innovation-capability measurement paper.

E1--E7 implement the experiment suite described in ``experiments/README.md``.
Modules are import-safe: heavy dependencies (numpy/pandas/scipy/sklearn) are
imported lazily so that ``import experiments.<module>`` succeeds even on a
minimal Python; running a step requires the real environment (``conda activate
lzz`` or any env with the scientific stack).
"""
