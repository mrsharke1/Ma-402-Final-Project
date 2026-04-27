
import sys
import numpy as np

import petsc4py
petsc4py.init(sys.argv)
from petsc4py import PETSc


class Heat1D:
    """
    Solve the 1D heat equation:

        u_t = u_xx,  0 <= x <= 1
        u(0,t) = u(1,t) = 0

    Initial condition:
        u(x,0) = sin(6πx) + 3 sin(2πx)
    """

    def __init__(self, m=60):
        self.m = m
        self.h = 1.0 / (m - 1)

        self.norm2_sum = 0.0
        self.normmax_sum = 0.0

        # PETSc vectors
        self.u = PETSc.Vec().createSeq(m)
        self.exact = self.u.duplicate()

        # Matrix
        self.A = PETSc.Mat().create()
        self.A.setSizes([m, m])
        self.A.setFromOptions()
        self.A.setUp()

    # ---------------------------
    # Initial condition
    # ---------------------------
    def initial_condition(self, u):
        arr = u.getArray()
        for i in range(self.m):
            x = i * self.h
            arr[i] = np.sin(6*np.pi*x) + 3*np.sin(2*np.pi*x)

        # boundary conditions
        arr[0] = 0.0
        arr[-1] = 0.0


    # ---------------------------
    # Exact solution
    # ---------------------------
    def exact_solution(self, t, sol):
        arr = sol.getArray()

        ex1 = np.exp(-36*np.pi*np.pi*t)
        ex2 = np.exp(-4*np.pi*np.pi*t)

        for i in range(self.m):
            x = i * self.h
            arr[i] = (
                np.sin(6*np.pi*x)*ex1 +
                3*np.sin(2*np.pi*x)*ex2
            )


    # ---------------------------
    # RHS function: f(u) = A u
    # ---------------------------
    def rhs_function(self, ts, t, u, f):
        self.A.mult(u, f)

    # ---------------------------
    # Build Laplacian matrix
    # ---------------------------
    def form_rhs_matrix(self):
        h2 = self.h * self.h
        m = self.m

        self.A.zeroEntries()

        # Boundary rows
        self.A.setValue(0, 0, 1.0)
        self.A.setValue(m-1, m-1, 1.0)

        # Interior stencil
        for i in range(1, m-1):
            self.A.setValue(i, i-1, 1.0 / h2)
            self.A.setValue(i, i, -2.0 / h2)
            self.A.setValue(i, i+1, 1.0 / h2)

        self.A.assemblyBegin()
        self.A.assemblyEnd()

    # ---------------------------
    # Monitor (error computation)
    # ---------------------------
    def monitor(self, ts, step, t, u):
        self.exact_solution(t, self.exact)

        err = self.exact.copy()
        err.axpy(-1.0, u)

        norm2 = err.norm(PETSc.NormType.NORM_2) * np.sqrt(self.h)
        normmax = err.norm(PETSc.NormType.NORM_INFINITY)

        dt = ts.getTimeStep()

        print(f"Step {step:3d} | t={t:.5f} | dt={dt:.5e} | "
              f"L2={norm2:.6e} | Linf={normmax:.6e}")

        self.norm2_sum += norm2
        self.normmax_sum += normmax

    # ---------------------------
    # Solve
    # ---------------------------
    def solve(self):
        ts = PETSc.TS().create()
        ts.setProblemType(PETSc.TS.ProblemType.LINEAR)

        # Build matrix
        self.form_rhs_matrix()

        # Set RHS correctly (Python-style)
        ts.setRHSFunction(self.rhs_function)
        ts.setRHSJacobian(self.A, self.A)

        # Initial condition
        self.initial_condition(self.u)

        # Time step
        dt = self.h * self.h / 2.0
        ts.setTimeStep(dt)

        ts.setMaxSteps(100)
        ts.setMaxTime(1.0)
        ts.setExactFinalTime(PETSc.TS.ExactFinalTime.STEPOVER)

        ts.setMonitor(self.monitor)

        ts.setFromOptions()

        # Solve
        ts.solve(self.u)

        steps = ts.getStepNumber()

        print("\nAverage L2 error:", self.norm2_sum / steps)
        print("Average Linf error:", self.normmax_sum / steps)

        return self.u


# ---------------------------
# Run
# ---------------------------
if __name__ == "__main__":
    solver = Heat1D(m=60)
    solver.solve()
