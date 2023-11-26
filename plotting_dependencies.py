# LIBRARIES
print('Loading libraries...')
import json
import os, sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import matplotlib
import matplotlib.colors as mcolors
import create_colortable
from create_colortable import plot_colortable, hex_to_rgb, rgb_to_dec
import mne
import matplotlib.cm as cm
from mne import io
from mne.datasets import sample
from mne.viz import plot_topomap
from matplotlib.patches import Ellipse
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
import neurodsp #aperiodic.conversions.convert_hurst_exponent
from neurodsp.aperiodic import conversions
print('Libraries loaded')
