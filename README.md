# Cable Loss for Timesmicrowave LMR Cables. (for now only LMR-400)

Eeasily calculate the cable loss with the distance and frequency as inputs.

```python
timesmicro.functions.cableLoss(frequency=1500, distance=120, rounded=True)
```
Or plot the ideal function for the cable loss of a cable with the distance as input. (start frequency and stop frequency are optional. L-Band by default).

```python
timesmicro.plot2D.cableLoss(distance=120)

timesmicro.plot2D.show()
```

![alt text](https://github.com/ghunshoot/timesmicro/blob/main/CL-LMR400-120ft.png)
