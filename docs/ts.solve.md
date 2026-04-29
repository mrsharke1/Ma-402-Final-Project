## ts.solve()
### What Does the Function Do?
The function steps the requested number of timesets. It runs the actual simulation and starts the time stepping. It uses the information from the RHS functions we defined before (and others) to run the problem through each time step.

### The Cython Bridge
It maps the python matrix and jacobian evaluation to the C solver.
* **Python call:** [Github location](https://gitlab.com/petsc/petsc/-/blob/main/src/binding/petsc4py/src/petsc4py/PETSc/TS.pyx?ref_type=heads#L2520) `ts.solve(self, Vec u=None) -> None`
* **Cython wrapper:** [Github location](https://gitlab.com/petsc/petsc/-/blob/main/src/binding/petsc4py/src/petsc4py/PETSc/TS.pyx?ref_type=heads#L2537)` CHKERR(TSSolve(self.ts, uvec))`
* **Underlying C Function:** `TSSolve` found in the cython wrapper

### Parameter Meanings
*The table maps the Python types to the C types used by PETSc

| Parameter | Python Equivalent | C Type | Description |
| :--- | :--- | :--- | :--- |
| **ts** | `self` | `TS` | The `TS` context obtained from `TSCreate()`. |
| **u** | `u` | `Vec` | **The solution vector.** Can be `None` (null) if `TSSetSolution()` was used and `TSSetExactFinalTime(ts, TS_EXACTFINALTIME_MATCHSTEP)` was not used. Otherwise, it must contain the initial conditions and will contain the solution at the final requested time. |
### Source Links
* **C Implementation:** [src/ts/interface/ts.c](https://gitlab.com/petsc/petsc/-/blob/main/src/ts/interface/ts.c?ref_type=heads#L4035)
* **C Header:** [include/petscts.h](https://gitlab.com/petsc/petsc/-/blob/main/include/petscts.h#L514)

### Minimal Working Example
```# 1. Prepares the initial condition vector
# 'model.u' is a PETSc Vec object representing the state (e.g., temperature)
u = model.u  

# 2. Executes the solver
# This advances 'u' from the start time to the final time.
# The Cython bridge updates the values inside the 'u' vector in-place.
ts.solve(u)

# 3. 'u' now contains the final results
print("Solve complete.")

# '.view()' prints the vector data to the terminal in a structured format better than just print
u.view()```

