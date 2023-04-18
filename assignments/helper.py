import numpy as np
import matplotlib.pyplot as plt


# plot feasible region based on linear constraints A, upper bounds b_ub
def compute_region_lin(A, b_ub, x1, x2):
    """Compute feasible region for linear constraints.

    :param A: linear constraints
    :param b_ub: upper bounds for linear constraints
    :param x1: x1 grid
    :param x2: x2 grid
    :return: feasible region
    """
    region = np.zeros_like(x1)
    for i in range(len(A)):
        region += (A[i][0] * x1 + A[i][1] * x2 <= b_ub[i]).astype(int)
    # if all constraints are satisfied, then the point is in the feasible region
    return (region == len(A)).astype(int)


# plot feasible region based on non-linear constraints G, upper bounds b_ub
def compute_region_nonlin(G, b_ub, x1, x2):
    """Compute feasible region for non-linear constraints.

    :param G: non-linear constraints
    :param b_ub: upper bounds for non-linear constraints
    :param x1: x1 grid
    :param x2: x2 grid
    :return: feasible region
    """
    region = np.zeros(shape=(len(x1), len(x2)))

    # check if constraint is satisfied at each point in the grid
    for j in range(len(x1)):
        for k in range(len(x2)):
            for i in range(len(G)):
                if G[i](x1[j, k], x2[j, k]) <= b_ub[i]:
                    region[j, k] += 1

    # if all constraints are satisfied, then the point is in the feasible region
    return (region == len(G)).astype(int)


# plot constraints as contour lines (both linear and non-linear)
def plot_constraints(G, b_ub, x1, x2, zorder=0):
    """Plot constraints as contour lines.

    :param G: non-linear constraints
    :param b_ub: upper bounds for non-linear constraints
    :param x1: x1 grid
    :param x2: x2 grid
    :param zorder: zorder for contour lines
    """
    for i in range(len(G)):
        # plot constraint as contour lines
        cnt = plt.contour(
            x1, x2, G[i](x1, x2), levels=[b_ub[i]], colors="k", zorder=zorder
        )
        # label constraints
        plt.clabel(cnt, inline=True, fontsize=10, fmt={0: f"g{i+1}(x)"})
