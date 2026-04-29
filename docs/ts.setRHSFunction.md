## ts.setRHSFunction()
### What Does the Function Do?
To start, note that TS is kind of like the family for the function. It stands for Time Stepping, and 
is used for solving differential equations. Essentially it manages the time integration. It is what allows the simulation to take little steps throughout time.
It is a step by step approach for the time variable, where each step is a different moment in time. This specific function
tells PETSc how to calculate the right hand side of the differential equation$\frac{du}{dt} = f(t, u)$. It sets the TS evaluation into a DMTS (DM stands for data management) which stores
the callbacks into a grid. In short this function computes the discrete Laplacian which represents the rate of heat diffusion at the current state.

### The Cython Bridge
In the `petsc4py` source code (`src/petsc4py/PETSc/TS.pyx`), the Python method `setRHSFunction` wraps the C routine `TSSetRHSFunction`.
* **Python call:** `ts.setRHSFunction(rhs_function, res_vec)`
* **Cython wrapper:** `CHKERR(TSSetRHSFunction(self.ts, res, __ts_rhsfunction__, <void*>cb))`
* **Underlying C Function:** `TSSetRHSFunction`

### Parameter Specifications
| Parameter | Python Type | C Type | Description |
| :--- | :--- | :--- | :--- |
| **f** | `callable` | `PetscErrorCode (*)(TS,PetscReal,Vec,Vec,void*)` | User function to compute the RHS. |
| **r** | `PETSc.Vec` | `Vec` | Vector to store the residual (optional). |

### Source Links
* **C Implementation:** [src/ts/interface/ts.c](https://gitlab.com/petsc/petsc/-/blob/main/src/ts/interface/ts.c)
* **C Header:** [include/petscts.h](https://gitlab.com/petsc/petsc/-/blob/main/include/petscts.h)

### Minimal Working Example
```python
def my_heat_rhs(ts, t, u, f):
    # Compute du/dt = A * u
    model.A.mult(u, f)

ts.setRHSFunction(my_heat_rhs)
