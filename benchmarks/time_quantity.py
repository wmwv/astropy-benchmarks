import numpy as np
from astropy import units as u


def time_quantity_init_scalar():
    3. * u.m / u.s


def time_quantity_init_array():
    np.arange(100000) * u.m / u.s


def time_quantity_ufunc_sin():
    np.sin(np.arange(10000) * u.degree)
