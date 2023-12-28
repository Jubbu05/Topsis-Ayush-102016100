# TOPSIS-Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Jubbu05/Topsis-Ayush-102016100/blob/main/LICENSE.txt)
[![GitHub stars](https://img.shields.io/github/stars/Jubbu05/CV_Parking_Space_Counter.svg)](https://github.com/Jubbu05/Topsis-Ayush-102016100/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Jubbu05/CV_Parking_Space_Counter.svg)](https://github.com/Jubbu05/Topsis-Ayush-102016100/network)

Submitted By: **Ayush Nagpure** <br>
Roll Number: **102016100** <br>
Batch: **3CS10**

***
pypi: <https://pypi.org/project/Topsis-Ayush-102016100>
<br>
***

## Installation
```pip install Topsis-Ayush-102016100```

## What is TOPSIS

**T**echnique for **O**rder **P**reference by **S**imilarity to **I**deal
**S**olution (TOPSIS) originated in the 1980s as a multi-criteria decision
making method. TOPSIS chooses the alternative of shortest Euclidean distance
from the ideal solution, and greatest distance from the negative-ideal
solution. More details at [wikipedia](https://en.wikipedia.org/wiki/TOPSIS).

<br>

## How to use this package:

Topsis-Ayush-102016100  can be run as in the following example:



### In Command Prompt
```
>> topsis data.csv "1,1,1,1" "+,+,-,+" result.csv
```
<br>

### Arguments
| Arguments | Description |
|------------| -----------------|
| input_file |  "CSV/Excel" file path |
| weights | Comma separated numbers |
| impacts | Comma separated '+' or '-' |
| output_file | Output CSV file path |

<br>

## Sample dataset

Consider this sample.csv file  

First column of file is removed by model before processing so follow the following format.  

All other columns of file should not contain any categorical values.

| Model  | P1 | P2 | P3 | P4 | P5 |
| :----: |:--:|:--:|:--:|:--:|:--:|
| M1 |0.85|0.72|4.6|41.5|11.92|
| M2 |0.66|0.44|6.6|49.4|14.28|
| M3 |0.9 |0.81|6.7|66.5|18.73|
| M4 |0.8 |0.64|6.9|69.7|19.51|
| M5 |0.84|0.71|4.7|36.5|10.69|
| M6 |0.91|0.83|3.6|42.3|11.91|
| M7 |0.65|0.42|6.9|38.1|11.52|
| M8 |0.71|0.5 |3.5|60.9|16.4 |

weights vector = [ 1,2,1,2,1 ]

impacts vector = [ +,-,+,+,- ]

### input:

```python
topsis sample.csv "1,2,1,2,1" "+,-,+,+,-" output.csv
```

### output:

output.csv file will contain following data :

| Model | P1 | P2 | P3 | P4 | P5 | Topsis score | Rank |
| :---: |:--:|:--:|:--:|:--:|:--:| :----------: | :--: |
| M1 |0.85|0.72|4.6|41.5|11.92| 0.3267076760116426 | 6 |
| M2 |0.66|0.44|6.6|49.4|14.28| 0.6230956090525585 | 2 |
| M3 |0.9 |0.81|6.7|66.5|18.73| 0.5006083702087599 | 5 |
| M4 |0.8 |0.64|6.9|69.7|19.51| 0.6275096427934269 | 1 |
| M5 |0.84|0.71|4.7|36.5|10.69| 0.3249142875298663 | 7 |
| M6 |0.91|0.83|3.6|42.3|11.91| 0.2715902624653612 | 8 |
| M7 |0.65|0.42|6.9|38.1|11.52| 0.5439263412940541 | 4 |
| M8 |0.71|0.5 |3.5|60.9|16.4 | 0.6166791918077927 | 3 |

The decision matrix (`a`) should be constructed with each row representing a Model alternative, and each column representing a criterion like Accuracy, R<sup>2</sup>, Root Mean Squared Error, Correlation, and many more.

Weights (`w`) is not already normalised will be normalised later in the code.

Information of benefit positive(+) or negative(-) impact criteria should be provided in `I`.

<br>

The rankings are stored in a csv file, with the 1st rank offering us the best decision, and last rank offering the worst decision making, according to TOPSIS method.

## API Usage
### Steps
1. Import topsis function from module topsis
2. Invoke topsis function by passing in data, weights, impacts

> Note: Impacts should be a list of -1 and 1. -1 depicting -ve and 1 depicting +ve impact

Example:
```python
import Topsis_Ayush_102016100 as tp
tp.topsis_score("data.csv" ,"2,2,3,3,4" ,"+,-,+,-,+", "result.csv")
```

## Debugging and Exception Handling
> The program has several assert statements which raise errors with helpful description in the following cases:
> - Wrong dimensions of decision matrix (*not* 2D), weights (*not* 1D)
> - Length of weights and impacts don't match 
> - Weights or impacts don't match number of attributes
> - For command line, number of arguments is less than 3 required
> - File extension must be .csv

## License
Copyright 2023 Ayush Nagpure
<br>
This repository is licensed under the MIT license.
<br>
See LICENSE for details.
[MIT](https://choosealicense.com/licenses/mit/)
