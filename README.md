# Due date calculator

The main purpose of this project was to calculate the date and time a project needs to be completed by. Two inputs are given: the date and time a task is given to a person and the number of working hours one has for it.

## Usage

In `main.py` file, for the completion of this task, a class called `dueDateCalculator` is initiated. This class has two inputs:
+ Submission date of a task
+ Number working hours a person has time for (turnaround time)

Based on these inputs, it calculates the date and time a task is due to.

## Implementation

There are a couple of rules that was used for the implementation:
+ There are two possible date format for the `submission date` input:
1. `"%Y-%m-%d %H:%M"`
2. `"%d/%m/%Y %H:%M"`
+ Holidays are ignored
+ The *working hours* are set between `9 and 17 Monday to Friday`
+ The turnaround time is defined in *working hours* and it is a *non-negative number*
+ A problem can only be reported during the working hours
+ For testing purposes, `unittest` module has been used

