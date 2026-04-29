## ts.setRHSJacobian()
### What Does the Function Do?
The function sets a time stepping jacobian evaluation function into a dmts. It sets the function for computing the Jacobian of the RHS function. In the heat equation since the problem is linear it is a matrix. This function tells PETSc how to build or update the matrix during the steps in the TS.

### The Cython Bridge
It maps the python matrix and jacobian evaluation to the C solver.
* **Python call:** [Github location](https://gitlab.com/petsc/petsc/-/blob/main/src/binding/petsc4py/src/petsc4py/PETSc/TS.pyx?ref_type=heads#L633) `ts.setRHSJacobian(jacobian, J=None, P=None, args=None, kargs=None)`
* **Cython wrapper:** [Github location](https://gitlab.com/petsc/petsc/-/blob/main/src/binding/petsc4py/src/petsc4py/PETSc/TS.pyx?ref_type=heads#L671)`CHKERR(TSSetRHSJacobian(self.ts, Jmat, Pmat, TS_RHSJacobian, <void*>context))
        else:
            CHKERR(TSSetRHSJacobian(self.ts, Jmat, Pmat, NULL, NULL))`
* **Underlying C Function:** `TSSetRHSJacobian` found in the cython wrapper

### Parameter Meanings
*The table maps the Python types to the C types used by PETSc

| Parameter | Python Equivalent | C Type | Description |
| :--- | :--- | :--- | :--- |
| **ts** | `self` | `TS` | The `TS` context obtained from `TSCreate()`. |
| **f** | `jacobian` | `TSRHSJacobianFn` | The right-hand side function. |
| **Amat** | `J` | `Mat` | The Jacobian Matrix. |
| **Pmat** | `P` | `Mat` | The matrix from which preconditioner is to be constructed (usually the same as `Amat`. |
| **ctx** | `args` | `PetscCtx` | Additional positional arguments for `jacobian`. |
| **ctx** | `kargs` | `PetscCtx` | Additional keyword arguments for `jacobian`. |
### Source Links
* **C Implementation:** [src/ts/interface/ts.c](https://gitlab.com/petsc/petsc/-/blob/main/src/ts/interface/ts.c?ref_type=heads#L1119)
* **C Header:** [include/petscts.h](https://gitlab.com/petsc/petsc/-/blob/main/include/petscts.h#L610)

### Minimal Working Example
```python
# 1. Define the variables/objects
ts = PETSc.TS().create()
A  = model.A  # Assuming 'model.A' is your pre-constructed Heat Equation matrix
u  = model.u  # Your solution vector

# 2. Define the routine
def my_heat_jacobian(ts, t, u, J, P):
    """
    ts: The solver context
    t:  The current time
    u:  The current state (input)
    J:  The Jacobian matrix (output)
    P:  The Preconditioning matrix (output)
    """
    # If the matrix is linear and already filled, we don't need 
    # any complex 'J.' code here. We just ensure it's ready for PETSc.
    J.assemble()

# 3. Register the Jacobian
# We tell PETSc: "Use 'my_heat_jacobian' to update the matrices J and P"
ts.setRHSJacobian(my_heat_jacobian, J=A, P=A)```
