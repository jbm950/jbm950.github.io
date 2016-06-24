# Solar Thermal Collector Mk1 Experiment 1 Page

[Link to Solar Thermal General Notes Page](./solar_thermal_mk1.html)

### Objective

The goal of this experiment is to practice setting up and running an experiment
on my own in addition to trying to tie experimental results to theoretical
learning.

This specific experiment will approximate the energy added to the bucket of
water over the course of an hour.

### Applicable Theory

(Collection of equations)

(Energy Harvested) => $\dot{Q}_{c} = \dot{m}c_{p}(T_{f,o} - T_{f,i})$ 

Need to do energy balances for control volumes to come up with some applicable
theory

$m_{tank}c\frac{dT}{dt} = -\dot{W}_{pump} + \dot{m}c(T_{in} - T_{tank})$

- Gotten from page 208 of Fundamentals of Engineering Thermodynamics

> __Bucket Volume Calculation__

<div align="center">
<table class="image">
<tr><td><img src="./img/bucket_calc.svg"
alt="Bucket Graphic" title="Bucket Graphic"/>
</td></tr>
</table>
</div>

> &nbsp;&nbsp;&nbsp;&nbsp;For the experiments I decided to only fill up
> the bucket halfway. I am going to approximate the water volume by
> determining the volume of a cylinder with a radius matching the radius
> of the bucket at half of the water height (1/4 overall height). Thus the volume can be calculated by the following steps:

> 1. Determine the angle $\theta$ from the side wall to vertical
>       - $\theta = sin^{-1}(0.75/14.5)$
> 1. Determine the radius at the half height of the water
> 1. Determine the vertical height of the water
> 1. Solve the formula of volume of a cylinder

> Slightly different result if halving the vertical height instead of thewall height

### Procedure

Will need a control test where just the bucket is used for the experiment

Collect

> _At beginning_

> - Voltage of batteries
> - Make sure the water hits a specific line on the bucket (same volume)

> _During_ (5 min intervals)

> - Water temp in bucket
> - Current air temp 

> _End_

> - Voltage of batteries

### Data

> [Raw csv file](./solar_therm_mk1_experiment1.csv)

#Graph of Control 1
#Graph of Control 2
#Graph of Control 3
#Control Avg Graph
#Graph of Experiment 1
#Graph of Experiment 2
#Graph of Experiment 3
#Experiment Avg Graph

#Chart comparing energy input between controls, experiments and averages
### Conclusions and Observations
