import numpy as np
import scipy
import matplotlib.pyplot as plt
from io import BytesIO
import base64

import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import scipy.special
import math


def generate_normal_plot():
    # Parameters for the standard normal distribution
    mu, sigma = 0, 1
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma**2))

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, pdf, "b-", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_geometric_plot():
    # Parameter for geometric distribution (support k = 1,2,...)
    p = 0.3
    k = np.arange(1, 16)
    pmf = np.array([((1 - p) ** (x - 1)) * p for x in k])

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.stem(k, pmf, basefmt=" ")
    ax.set_xlabel("Trial Number (k)")
    ax.set_ylabel("Probability")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_negative_binomial_plot():
    # Parameters for negative binomial distribution: r = number of successes, p = success probability,
    # where k is the number of failures until the r-th success.
    r, p = 3, 0.4
    k = np.arange(0, 16)
    pmf = np.array(
        [math.comb(k_val + r - 1, k_val) * (p**r) * ((1 - p) ** k_val) for k_val in k]
    )

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.stem(k, pmf, basefmt=" ")
    ax.set_xlabel("Number of Failures")
    ax.set_ylabel("Probability")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_logistic_plot():
    # Parameters for the logistic distribution
    mu, s = 0, 1
    x = np.linspace(mu - 10, mu + 10, 1000)
    pdf = np.exp(-(x - mu) / s) / (s * (1 + np.exp(-(x - mu) / s)) ** 2)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, pdf, "m-", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_lognormal_plot():
    # Parameters for the lognormal distribution: mu and sigma refer to the underlying normal distribution.
    mu, sigma = 0, 0.5
    x = np.linspace(0.001, 3, 1000)  # start near 0 to avoid log(0)
    pdf = (1 / (x * sigma * np.sqrt(2 * np.pi))) * np.exp(
        -((np.log(x) - mu) ** 2) / (2 * sigma**2)
    )

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, pdf, "c-", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_chi_squared_plot():
    # Parameters: k = degrees of freedom
    k = 4
    x = np.linspace(0.001, 15, 1000)
    factor = 1 / (2 ** (k / 2) * math.gamma(k / 2))
    pdf = factor * (x ** (k / 2 - 1)) * np.exp(-x / 2)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, pdf, "orange", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_students_t_plot():
    # Parameter: ν (nu) degrees of freedom
    nu = 5
    x = np.linspace(-10, 10, 1000)
    coeff = math.gamma((nu + 1) / 2) / (np.sqrt(nu * np.pi) * math.gamma(nu / 2))
    pdf = coeff * (1 + (x**2) / nu) ** (-(nu + 1) / 2)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, pdf, "k-", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_f_distribution_plot():
    # Parameters: d1 and d2
    d1, d2 = 5, 15
    x = np.linspace(0.001, 5, 1000)
    # f(x) = sqrt(( (d1*x)^d1 * d2^d2 )/((d1*x + d2)^(d1+d2))) / ( x * B(d1/2, d2/2) )
    B = scipy.special.beta(d1 / 2, d2 / 2)
    numerator = ((d1 * x) ** d1) * (d2**d2)
    denominator = (d1 * x + d2) ** (d1 + d2)
    pdf = np.sqrt(numerator / denominator) / (x * B)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, pdf, "y-", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_pareto_plot():
    # Parameters: α (alpha) and x_m (scale minimum)
    alpha, x_m = 2, 1
    x = np.linspace(x_m, 5, 1000)
    pdf = alpha * (x_m**alpha) / (x ** (alpha + 1))

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, pdf, "b-", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_weibull_plot():
    # Parameters: λ (lambda) and k (shape parameter)
    lam, k = 1, 1.5
    x = np.linspace(0, 5, 1000)
    pdf = (k / lam) * ((x / lam) ** (k - 1)) * np.exp(-((x / lam) ** k))

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, pdf, "g-", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


# Additional common distributions
def generate_exponential_plot():
    # Exponential Distribution: f(x) = λ * exp(-λ*x) for x >= 0
    lam = 1
    x = np.linspace(0, 10, 1000)
    pdf = lam * np.exp(-lam * x)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, pdf, "r-", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_uniform_plot():
    # Uniform Distribution on [a, b]
    a, b = 0, 1
    x = np.linspace(a - 0.1, b + 0.1, 1000)
    pdf = np.where((x >= a) & (x <= b), 1 / (b - a), 0)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, pdf, "m-", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_binomial_plot():
    n, p = 10, 0.5
    k = np.arange(0, n + 1)
    pmf = np.array([math.comb(n, x) * (p**x) * ((1 - p) ** (n - x)) for x in k])

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.stem(k, pmf, basefmt=" ")
    ax.set_xlabel("Number of Successes")
    ax.set_ylabel("Probability")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_gamma_plot():
    alpha, beta = 2, 1
    x = np.linspace(0, 10, 1000)
    y = (beta**alpha) * (x ** (alpha - 1)) * np.exp(-beta * x) / math.gamma(alpha)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, "r-", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


def generate_beta_plot():
    alpha, beta = 2, 5
    x = np.linspace(0, 1, 1000)
    y = (x ** (alpha - 1)) * ((1 - x) ** (beta - 1)) / scipy.special.beta(alpha, beta)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, "g-", lw=2)
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


# def generate_normal_plot():
#     x = np.linspace(-4, 4, 1000)
#     y = 1 / (np.sqrt(2 * np.pi)) * np.exp(-(x**2) / 2)
#
#     fig, ax = plt.subplots(figsize=(8, 4))
#     ax.plot(x, y, "b-", lw=2)
#     ax.set_xlabel("x")
#     ax.set_ylabel("Probability Density")
#     ax.grid(True)
#
#     buf = BytesIO()
#     fig.savefig(buf, format="svg", bbox_inches="tight")
#     plt.close(fig)
#     return buf.getvalue().decode("utf-8")
#
#
# def generate_exponential_plot():
#     x = np.linspace(0, 5, 1000)
#     y = np.exp(-x)
#
#     fig, ax = plt.subplots(figsize=(8, 4))
#     ax.plot(x, y, "r-", lw=2)
#     ax.set_xlabel("x")
#     ax.set_ylabel("Probability Density")
#     ax.grid(True)
#
#     buf = BytesIO()
#     fig.savefig(buf, format="svg", bbox_inches="tight")
#     plt.close(fig)
#     return buf.getvalue().decode("utf-8")
#


def generate_poisson_plot():
    k = np.arange(0, 15)
    λ = 4
    pmf = np.exp(-λ) * (λ**k) / math.factorial(k)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.stem(k, pmf, basefmt=" ")
    ax.set_xlabel("k")
    ax.set_ylabel("Probability Mass")
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="svg", bbox_inches="tight")
    plt.close(fig)
    return buf.getvalue().decode("utf-8")


# def generate_uniform_plot():
#     x = np.linspace(-1, 2, 1000)
#     y = np.piecewise(x, [(x >= 0) & (x <= 1), (x < 0) | (x > 1)], [1, 0])
#
#     fig, ax = plt.subplots(figsize=(8, 4))
#     ax.plot(x, y, "g-", lw=2)
#     ax.set_xlabel("x")
#     ax.set_ylabel("Probability Density")
#     ax.grid(True)
#
#     buf = BytesIO()
#     fig.savefig(buf, format="svg", bbox_inches="tight")
#     plt.close(fig)
#     return buf.getvalue().decode("utf-8")
