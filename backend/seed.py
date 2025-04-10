from app import app, db
from app.models import Distribution
from app.distributions.distributions import *
import json

# DISTRIBUTIONS = [
#     {
#         "name": "normal",
#         "formula": r"f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}",
#         "parameters": {"μ": 0, "σ": 1},
#         "plot_generator": generate_normal_plot,
#     },
#     {
#         "name": "binomial",
#         "formula": r"P(k) = \binom{n}{k} p^k (1-p)^{n-k}",
#         "parameters": {"n": 10, "p": 0.5},
#         "plot_generator": generate_binomial_plot,
#     },
#     {
#         "name": "gamma",
#         "formula": r"f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}",
#         "parameters": {"α": 2, "β": 1},
#         "plot_generator": generate_gamma_plot,
#     },
#     {
#         "name": "beta",
#         "formula": r"f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}",
#         "parameters": {"α": 2, "β": 5},
#         "plot_generator": generate_beta_plot,
#     },
#     {
#         "name": "geometric",
#         "formula": r"P(k) = (1-p)^{k-1} p",
#         "parameters": {"p": 0.3},
#         "plot_generator": generate_geometric_plot,
#     },
#     {
#         "name": "negative_binomial",
#         "formula": r"P(k) = \binom{k+r-1}{k} p^r (1-p)^k",
#         "parameters": {"r": 3, "p": 0.4},
#         "plot_generator": generate_negative_binomial_plot,
#     },
#     {
#         "name": "logistic",
#         "formula": r"f(x) = \frac{e^{-(x-\mu)/s}}{s(1+e^{-(x-\mu)/s})^2}",
#         "parameters": {"μ": 0, "s": 1},
#         "plot_generator": generate_logistic_plot,
#     },
#     {
#         "name": "lognormal",
#         "formula": r"f(x) = \frac{1}{x\sigma\sqrt{2\pi}} e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}",
#         "parameters": {"μ": 0, "σ": 0.5},
#         "plot_generator": generate_lognormal_plot,
#     },
#     {
#         "name": "chi_squared",
#         "formula": r"f(x) = \frac{x^{k/2-1}e^{-x/2}}{2^{k/2}\Gamma(k/2)}",
#         "parameters": {"k": 4},
#         "plot_generator": generate_chi_squared_plot,
#     },
#     {
#         "name": "students_t",
#         "formula": r"f(x) = \frac{\Gamma(\frac{\nu+1}{2})}{\sqrt{\nu\pi}\Gamma(\frac{\nu}{2})} \left(1+\frac{x^2}{\nu}\right)^{-\frac{\nu+1}{2}}",
#         "parameters": {"ν": 5},
#         "plot_generator": generate_students_t_plot,
#     },
#     {
#         "name": "f_distribution",
#         "formula": r"f(x) = \frac{\sqrt{\frac{(d_1 x)^{d_1} d_2^{d_2}}{(d_1 x + d_2)^{d_1+d_2}}}}{x B\left(\frac{d_1}{2}, \frac{d_2}{2}\right)}",
#         "parameters": {"d1": 5, "d2": 15},
#         "plot_generator": generate_f_distribution_plot,
#     },
#     {
#         "name": "pareto",
#         "formula": r"f(x) = \frac{\alpha x_m^\alpha}{x^{\alpha+1}}",
#         "parameters": {"α": 2, "x_m": 1},
#         "plot_generator": generate_pareto_plot,
#     },
#     {
#         "name": "weibull",
#         "formula": r"f(x) = \frac{k}{\lambda} \left(\frac{x}{\lambda}\right)^{k-1} e^{-(x/\lambda)^k}",
#         "parameters": {"λ": 1, "k": 1.5},
#         "plot_generator": generate_weibull_plot,
#     },
# ]

DISTRIBUTIONS = [
    {
        "name": "normal",
        "formula": r"f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}",
        "parameters": {"μ": 0, "σ": 1},
        "plot_generator": generate_normal_plot,
    },
    {
        "name": "binomial",
        "formula": r"P(k) = \binom{n}{k} p^k (1-p)^{n-k}",
        "parameters": {"n": 10, "p": 0.5},
        "plot_generator": generate_binomial_plot,
    },
    {
        "name": "gamma",
        "formula": r"f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}",
        "parameters": {"α": 2, "β": 1},
        "plot_generator": generate_gamma_plot,
    },
    {
        "name": "beta",
        "formula": r"f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}",
        "parameters": {"α": 2, "β": 5},
        "plot_generator": generate_beta_plot,
    },
    {
        "name": "geometric",
        "formula": r"P(k) = (1-p)^{k-1} p",
        "parameters": {"p": 0.3},
        "plot_generator": generate_geometric_plot,
    },
    {
        "name": "negative_binomial",
        "formula": r"P(k) = \binom{k+r-1}{k} p^r (1-p)^k",
        "parameters": {"r": 3, "p": 0.4},
        "plot_generator": generate_negative_binomial_plot,
    },
    {
        "name": "logistic",
        "formula": r"f(x) = \frac{e^{-(x-\mu)/s}}{s(1+e^{-(x-\mu)/s})^2}",
        "parameters": {"μ": 0, "s": 1},
        "plot_generator": generate_logistic_plot,
    },
    {
        "name": "lognormal",
        "formula": r"f(x) = \frac{1}{x\sigma\sqrt{2\pi}} e^{-\frac{(\ln x-\mu)^2}{2\sigma^2}}",
        "parameters": {"μ": 0, "σ": 0.5},
        "plot_generator": generate_lognormal_plot,
    },
    {
        "name": "chi_squared",
        "formula": r"f(x) = \frac{x^{k/2-1} e^{-x/2}}{2^{k/2} \Gamma(k/2)}",
        "parameters": {"k": 4},
        "plot_generator": generate_chi_squared_plot,
    },
    {
        "name": "students_t",
        "formula": r"f(x) = \frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi}\,\Gamma\left(\frac{\nu}{2}\right)} \left(1+\frac{x^2}{\nu}\right)^{-\frac{\nu+1}{2}}",
        "parameters": {"ν": 5},
        "plot_generator": generate_students_t_plot,
    },
    {
        "name": "f_distribution",
        "formula": r"f(x) = \frac{\sqrt{\frac{(d_1 x)^{d_1}d_2^{d_2}}{(d_1 x+d_2)^{d_1+d_2}}}}{x B\left(\frac{d_1}{2}, \frac{d_2}{2}\right)}",
        "parameters": {"d1": 5, "d2": 15},
        "plot_generator": generate_f_distribution_plot,
    },
    {
        "name": "pareto",
        "formula": r"f(x) = \frac{\alpha x_m^\alpha}{x^{\alpha+1}}",
        "parameters": {"α": 2, "x_m": 1},
        "plot_generator": generate_pareto_plot,
    },
    {
        "name": "weibull",
        "formula": r"f(x) = \frac{k}{\lambda}\left(\frac{x}{\lambda}\right)^{k-1} e^{-(x/\lambda)^k}",
        "parameters": {"λ": 1, "k": 1.5},
        "plot_generator": generate_weibull_plot,
    },
    {
        "name": "exponential",
        "formula": r"f(x) = \lambda e^{-\lambda x} \quad (x \ge 0)",
        "parameters": {"λ": 1},
        "plot_generator": generate_exponential_plot,
    },
    {
        "name": "uniform",
        "formula": r"f(x) = \frac{1}{b-a} \quad (a \le x \le b)",
        "parameters": {"a": 0, "b": 1},
        "plot_generator": generate_uniform_plot,
    },
]


# def seed_distributions():
#     with app.app_context():
#         db.create_all()
#
#         for dist_data in DISTRIBUTIONS:
#             exists = Distribution.query.filter_by(name=dist_data["name"]).first()
#             if not exists:
#                 svg_content = dist_data["plot_generator"]()
#                 new_dist = Distribution(
#                     name=dist_data["name"],
#                     svg=svg_content,
#                     formula=dist_data["formula"],
#                     parameters=json.dumps(
#                         dist_data["parameters"]
#                     ),  # Convert dict to JSON string
#                 )
#                 db.session.add(new_dist)
#
#         db.session.commit()
#     print("Database seeded successfully!")
#
from sqlalchemy import select


def seed_distributions():
    with app.app_context():
        # Tables are managed by Alembic, so we skip creating them here.
        with db.session() as session:
            with session.begin():
                for dist_data in DISTRIBUTIONS:
                    stmt = select(Distribution).filter_by(name=dist_data["name"])
                    exists = session.execute(stmt).scalar_one_or_none()
                    if not exists:
                        svg_content = dist_data["plot_generator"]()
                        new_dist = Distribution(
                            name=dist_data["name"],
                            svg=svg_content,
                            formula=dist_data["formula"],
                            parameters=json.dumps(dist_data["parameters"]),
                        )
                        session.add(new_dist)
    print("Database seeded successfully!")


if __name__ == "__main__":
    seed_distributions()
