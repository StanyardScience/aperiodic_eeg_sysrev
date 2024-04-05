# aperiodic_eeg_sysrev
Aperiodic and Hurst Exponent Systematic Review: Plotting Figures

This repository is the code reference platform for the plotting functions used in the paper "Aperiodic and Hurst EEG exponents across early human brain development: a systematic review" by Stanyard et al (2024), submitted to Developmental and Cognitive Neuroscience (DOI: TBA). The functions provided here are for a number of bespoke plotting functions capable of creating ellipsoids and points which map the variability in age and another defining feature, such as in this case, the aperiodic exponent for each dataset. 

**Access to the original data used in the paper**

Being able to visualise the variation in both dimensions is incredibly helpful, and not something to my knowledge was available in existing python tools at the time of creation. Please note that due to restrictions in data sharing agreements for the datasets the paper utilises, we cannot provided the original data. However, please see our paper for references to the individual sources, some of which are available freely. 

**Individual colours for each study plotted**

The functions provided can be modified for use with your own dataset and colour palettes. In an earlier version of this tool, each study had a unique HEX code to identify individual studies. Reference to this in the relevant functions has been retained, but these individual colours are overridden in the newer implementation (the first published version). Please feel free to edit this if individual plotting is useful for you. Likewise, we provide the function and code to generate each plot as a complete .py file as opposed to an imported function used for each study in the hopes this is more accessible for users who are new to python. 

Shown below is Figure 2A and 2B from our paper, for which the relevant code is contained in this repository (along with Figure 3A, 3B, and Supplementary Figure VA, B). 

![NBBR_FIG2_REVISED](https://github.com/StanyardScience/aperiodic_eeg_sysrev/assets/54684253/e25fe47b-f3f1-4920-ae8b-7fd126f4533a)

Given the potential novelty of this tool, we make this freely accessible to support the community, and as a companion tool to our paper. 
For improvement suggestions, collaboration or paper-related questions, please contact me directly at stanyardscience@gmail.com

Ryan,
November 2023 
