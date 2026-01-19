# %% [markdown]
## Welcome to this notebook! <br>
# In this step, this notebook will guide you how to use the add function from step_1 <br>
# First, we import all of the necessary packages. <br>
# This is also nice to see that $\lambda$ works in markdown cell.

# %% [markdown]
# Now, we will import the parallel sum function from step_6 and test it here

# %%
import os
import sys

cwd = os.getcwd()
root = os.path.abspath(os.path.join(cwd, "..", ".."))
if root not in sys.path:
    sys.path.append(root)

from src.step_6.parallel_sum import parallel_sum  # noqa: E402

xs = list(range(5))
result = parallel_sum(xs)

# %% [markdown]
# Now, we add a cell, which tests the mpi parallism function and check if the size > 1

# %%
from mpi4py import MPI  # noqa: E402

print(f"I am rank {MPI.COMM_WORLD.rank} of {MPI.COMM_WORLD.size}")
assert 0 > 1
#assert MPI.COMM_WORLD.size > 1
