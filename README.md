# Cable Loss for Timesmicrowave LMR Cables. 
## (for now only LMR-400)

### Calculation
Eeasily calculate the cable loss with the distance run lenght(ft) and frequency(MHz) as inputs.

#### Code:
```python
timesmicro.functions.cableLoss(frequency=1500, distance=120, rounded=True)
```
### 2D Plot
Create a 2D plot of the ideal cable loss using the distance run lenght(ft) as input. (start frequency and stop frequency are optional. L-Band by default).

#### Code:
```python
timesmicro.plot2D.cableLoss(distance=120)

timesmicro.plot2D.show()
```

![alt text](https://github.com/ghunshoot/timesmicro/blob/main/CL-LMR400-120ft.png)

### 2D Plot from CSV file
Create a 2D plot from data of a csv file.

The structure of the CSV file should be (headers must be deleted or ignored when formatting the file):
| `Frequency`   | `Attenuation` |
|:-------------:|:-------------:|
| 1000          | 5             |
| 1200          | 5.8           |
| 1400          | 6.2           |
| 1600          | 6.8           |
| ...           | ...           |

[CSV file format example](https://github.com/ghunshoot/timesmicro/blob/main/measured.csv)

#### Code:
```python

timesmicro.plot2D.cableLossFromCSV(path='measured.csv')

timesmicro.plot2D.show()
```

![alt text](https://github.com/ghunshoot/timesmicro/blob/main/CL-CSV-DATA.png)


### Ideal CL vs Measured CL

This example makes a compariative of an ideal graph with a measured graph from CSV file.

```python
import timesmicro.plot2D as plt


plt.cableLossFromCSV(path='measured.csv', color='tab:red')

plt.cableLoss(distance=120, color='tab:blue')

plt.show()
```
![alt text](https://github.com/ghunshoot/timesmicro/blob/main/CL-IDEALvsMEASURED.png)


