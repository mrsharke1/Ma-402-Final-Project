# Ma-402-Final-Project
## Ma 402 Final Project: Heat Equation Solver (Time Independent right hand side)
This project uses AI to translate C code to python, by implementing PETSc and petsc4py library. The project solves the 1D heat equation on the interval [0,1] with fixed 0 boundary conditions. It converts a continuous problem into a discrete problem by splitting it up into finite differences, turning it into a matrix problem. The change in time is handled by PETS'cs TS solver and then the new discrete solution is compared to the exact solution at each step.

  * Chosen problem EX 3.c The heat equation https://petsc.org/main/src/ts/tutorials/ex3.c.html
## Project Components:
  * README.md : brief overview of the problem and a reflection on the project
  * tutorial_model.py: Full AI translated code
  * tutorial_presentation.jpynb : Jupyter Notebook that imports my module, runs the simulation, and visualizes the results.
  * Docs Markdown Files for the three docstrings
     * File 1
     * file 2
     * file 3

## Project Reflection
This project was very challenging. Getting VS Code to run the petsc4py library was challenging and time consuming. I had to access the windows powershell to download Linux Subsytem for Windows, to then upload that to VS code, and more steps to get the code to run. Once I got it working I uploaded my selected problem, 3c the heat equation, into chatGPT for it to translate into usable python script. Luckily there was very little debugging required as I have little experience with python prior to this class. To be candid, it was hard to understand if the code was working properly due to my lack of experience in python. However, it returned an output, so I consider that a sucess. COMEBACKTO THIS MEGAN AND FINISH ITTTTTT 
