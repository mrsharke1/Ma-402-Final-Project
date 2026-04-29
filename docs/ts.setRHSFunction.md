## ts.setRHSFunction()
### What Does the Function Do?
To start, note that TS is kind of like the family for the function. It stands for Time Stepping, and is used for solving differential equations. Essentially it manages the time integration. It is what allows the simulation to take little steps throughout time. It is a step by step approach for the time variable, where each step is a different moment in time. This specific function
tells PETSc how to calculate the right hand side of the differential equation $\frac{du}{dt} = f(t, u)$, which is how heat spreads over time. It sets the TS evaluation into a DMTS (DM stands for data management) which stores the callbacks into a grid. In short this function computes the discrete Laplacian which represents the rate of heat diffusion at the current state.

### The Cython Bridge
In the `petsc4py` source code (`src/petsc4py/PETSc/TS.pyx`), the Python method `setRHSFunction` wraps the C routine `TSSetRHSFunction`.
* **Python call:** [Github location](https://gitlab.com/petsc/petsc/-/blob/main/src/binding/petsc4py/src/petsc4py/PETSc/TS.pyx?ref_type=heads#L596) `ts.setRHSFunction(function, f=None, args=None, kargs=None)`
* **Cython wrapper:** [Github location](https://gitlab.com/petsc/petsc/-/blob/main/src/binding/petsc4py/src/petsc4py/PETSc/TS.pyx?ref_type=heads#L629)`CHKERR(TSSetRHSFunction(self.ts, fvec, TS_RHSFunction, <void*>context))
        else:
            CHKERR(TSSetRHSFunction(self.ts, fvec, NULL, NULL))`
* **Underlying C Function:** `TSSetRHSFunction` found in the cython wrapper

### Parameter Meanings
*The table maps the Python types to the C types used by PETSc

| Parameter | Python Type | C Type | Description (from C Source) |
| :--- | :--- | :--- | :--- |
| **ts** | `PETSc.TS` | `TS` | The Time-Stepping context (the solver object). Obtained from TSCreate() |
| **function** | `callable` | `TSRHSFunctionFn*` | The RHS function $f(t,u)$. |
| **f** | `PETSc.Vec` | `Vec` | Vector used to store the computed RHS results (internal workspace) routine for evaluating right hand side function. |
| **args** | `tuple` | `PetscCtx` | Optional positional arguments for function. |
| **kargs** | `dict` | `PetscCtx` | Optional keyword arguments for function. |
| **r** | `f` (Vector) | `Vec` | Vector to put the computed right-hand side (or `NULL` to have it created). |
| **ctx** | `args` / `kargs` | `PetscCtx` | [optional] User-defined context for private data for the function evaluation routine. |
### Source Links
* **C Implementation:** [src/ts/interface/ts.c]( https://gitlab.com/petsc/petsc/-/blob/main/src/ts/interface/ts.c?ref_type=heads#L1003)
* **C Header:** [include/petscts.h](https://gitlab.com/petsc/petsc/-/blob/main/include/petscts.h#L608)

### Minimal Working Example
```python
# 'f' (Routine): The physics function calculating the discrete Laplacian
def my_heat_rhs(ts, t, u, f):
    """
    ts: The TS solver context
    t:  The current time step
    u:  The current solution state (input)
    f:  The vector 'r' where the RHS result is stored (output)
    """
    # Compute du/dt = A * u (where A is the system matrix)
    # This modifies 'f' in-place as required by the C API
    model.A.mult(u, f)

# 'ts': The TS context created via PETSc.TS().create()
# Registering the function:
ts.setRHSFunction(my_heat_rhs)```
