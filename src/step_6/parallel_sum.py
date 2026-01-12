from mpi4py import MPI

T = int | float | complex


def parallel_sum(xs: list[T]) -> T:
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    local_xs = xs[rank::size]
    local_sum = sum(local_xs)

    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
    return total_sum
