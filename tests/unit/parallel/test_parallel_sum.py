from src.step_6.parallel_sum import parallel_sum
from mpi4py import MPI


def test_parallel_sum():
    xs = list(range(5))
    result = parallel_sum(xs)
    if MPI.COMM_WORLD.Get_rank() == 0:
        assert result == sum(xs)
