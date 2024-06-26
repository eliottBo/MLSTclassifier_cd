# MLSTclassifier_cd

## Table of Contents

- [Overview](#overview)

- [Installation](#installation)

- [Usage](#usage)

- [Output](#output)

## Overview

Enhance your clade prediction process with MLSTclassifier_cd, a powerful machine learning tool that employs K-Nearest Neighbors (KNN) algorithm. Designed specifically for Multi-Locus Sequence Type (MLST) analysis of _C. difficile_ strains, including cryptic variants, this tool streamlines and accelerates clade prediction. MLSTclassifier_cd achieves a prediction accuracy of approximately 92%.

StatQuest methodology was used to build the model (https://www.youtube.com/watch?v=q90UDEgYqeI&t=3327s). Powered by the Scikit-learn library, MLSTclassifier_cd is a good tool to have a first classification of your _C. difficile_ strains including cryptic ones.

The model was trained using data from PubMLST (May 2023): https://pubmlst.org/bigsdb?db=pubmlst_cdifficile_seqdef&page=downloadProfiles&scheme_id=1. Cryptic strains for training were assessed manually using phylogenetic tree construction, fastbaps and popPUNK to refine clustering.

GitHub repo: https://github.com/eliottBo/MLSTclassifier_cd

## Installation:

It is recommended to use a virtual environment.

**Install PyPI package:**
`pip install mlstclassifier-cd`

https://pypi.org/project/mlstclassifier-cd/

## Usage:


The first argument is a path to a directory containing ".mlst" (like the ones optained from PubMLST) or ".fastmlst" files from [FastMLST](https://github.com/EnzoAndree/FastMLST). The second argument is a path to the output directory where the output files will be.

### Basic Command:
`MLSTclassifier_cd [input directory path] [output directory path]`

Example: `MLSTclassifier_cd /Desktop/input_directory_name /Desktop/output_directory_name/`

## Output:

After running MLSTclassifier_cd, the result file contain a column named "predicted_clade".
It also creates the following files:

- "pie_chart.html" plot representing the proportions of the different clades found.
- "count.csv" a csv file containing the raw value count of your predicted clades for you to generate your own graphs!