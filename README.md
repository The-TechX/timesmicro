# Cable Loss for Timesmicrowave LMR Cables. (for now only LMR-400)

### Calculation
Eeasily calculate the cable loss with the distance run lenght(ft) and frequency(MHz) as inputs.

```python
timesmicro.functions.cableLoss(frequency=1500, distance=120, rounded=True)
```
### 2D Plot
Create a 2D plot of the ideal cable loss using the distance run lenght(ft) as input. (start frequency and stop frequency are optional. L-Band by default).

```python
timesmicro.plot2D.cableLoss(distance=120)

timesmicro.plot2D.show()
```

![alt text](https://github.com/ghunshoot/timesmicro/blob/main/CL-LMR400-120ft.png)
