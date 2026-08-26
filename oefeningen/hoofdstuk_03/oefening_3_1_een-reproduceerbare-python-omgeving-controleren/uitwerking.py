import platform

import sys

import numpy as np

import pandas as pd

assert sys.version_info >= (3, 10), "Python 3.10 of hoger is vereist"

print("Python:", sys.version.split()[0])

print("Platform:", platform.platform())

print("NumPy:", np.__version__)

print("Pandas:", pd.__version__)
