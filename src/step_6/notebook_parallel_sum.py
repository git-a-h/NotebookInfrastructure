# %% [markdown]
## Welcome to this notebook! <br>
# In this step, this notebook will guide you how to use the add function from step_1 <br>
# First, we import all of the necessary packages. <br>
# This is also nice to see that $\lambda$ works in markdown cell.

# %%
print("This is a test notebook for step 6")

# %% [markdown]
# Now, we will import the parallel sum function from step_6 and test it here

# %%
from src.step_6.parallel_sum import parallel_sum  # noqa: E402

xs = list(range(5))
result = parallel_sum(xs)
