# Ma-402-Final-Project
## Ma 402 Final Project: Heat Equation Solver (Time Independent right hand side)
This project uses AI to translate C code to python, by implementing PETSc and petsc4py library. The project solves the 1D heat equation on the interval [0,1] with fixed 0 boundary conditions. It converts a continuous problem into a discrete problem by splitting it up into finite differences, turning it into a matrix problem. The change in time is handled by PETS'cs TS solver and then the new discrete solution is compared to the exact solution at each step.

  * Chosen problem EX 3.c The heat equation https://petsc.org/main/src/ts/tutorials/ex3.c.html
## Project Components:
  * **[Home Page](./README.md)**: brief overview of the problem and a reflection on the project
  * **[Tutorial Model](./tutorial_model.py)**: Full AI translated code
  * **[Tutorial Presentation](./tutorial_presentation.jpynb)** : Jupyter Notebook that imports my module, runs the simulation, and visualizes the results.
  * Docs Markdown Files for the three docstrings
     * **[ts.setRHSFunction](./ts.setRHSFunction.md)**
     * **[ts.setRHSJacobian](./ts.setRHSJacobian.md)**
     * **[ts.solve](./ts.solve.md)**

## Project Reflection
This project was pretty challenging. I think it was difficult as we had not really done anything like it in class before, and finding all the necesary information and figuring out github was alot. However the most challenging thing was getting VS Code to work. In order to run the petsc4py library I had to access the windows powershell to download Linux Subsytem for Windows, to then upload that to VS code, and more steps to get the code to run. Then after the code ran, I had to change the kernel in vs code to get the jupyter notebook to work, which took about 2 hours (probably due to lack of experience with VS Code. Once I got it working I uploaded my selected problem, 3c the heat equation, into chatGPT for it to translate into usable python script. Luckily there was very little debugging required as I have little experience with python prior to this class. It returned an output for each step in the time step function and the visualization was interesting to see. I included multiple time steps in my graph, which really allows viewers to visualize how the heat difuses, and how the function works. Overall, the project was very challenging, and it felt somewhat disconnected from what we learned in class, but it was interesting to see how to translate code, and how these solvers can work to solve problems I learned in previous classes. I would be interested in learning more to apply to harder differential equations one day.
