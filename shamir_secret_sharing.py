# coding: utf-8
"""_summary_
https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing
"""
import random


def create_random_coefficients(k: int) -> list[int]:
    """_summary_
    create random coefficients for the polynomial
    a1, a2, ..., ak-1

    Args:
        k int: number of shares

    Returns:
        list[int]: random coefficients
    """
    return [random.randint(1, 100) for _ in range(k - 1)]


def print_polynomial(an_list: list[int]) -> None:
    """_summary_
    for debugging, print polynomial

    Args:
        an_list (_type_): _description_
    """
    for i in range(len(an_list)):
        print(f" + {an_list[i]}x^{i}", end="")
    print()
    return


def print_D_n_list(D_n_list: list[int]) -> None:
    """_summary_
    for debugging, print D_n_list

    Args:
        D_n_list (_type_): _description_
    """
    for i in range(len(D_n_list)):
        print(f"D_{i} = {D_n_list[i]}")
    return


def create_points(x: int, an_list) -> list[int]:
    """_summary_

    Args:
        x (_type_): _description_
        an_list (_type_): _description_

    Returns:
        (x, fx) = (x, sum(a0 + a1x + a2x^2 + ... + ak-1x^(k-1)))
    """
    return [x, sum([an_list[i] * x**i for i in range(len(an_list))])]


def cal_lagrange_basis_for_polynomial(D_k_list: list[list[int]]) -> int:
    """_summary_
    Lagrange basis polynomial(ラグランジュ補完)

    Args:
        D_n_list list[int]: list of points D_n

    Returns: f(0) = a0 int: secret data.
    NOTE: f(x)でラグランジュ補完を求めても必要なのはf(0)だけなので最初からf(0)だけ求める
    """
    # l_0(0), l_1(0), ... l_k-1(0)
    l_k_list = []
    for j in range(len(D_k_list)):
        for m in range(len(D_k_list)):
            if m == j:
                continue
            if "tmp" not in locals():
                tmp = (0 - D_k_list[m][0]) / (D_k_list[j][0] - D_k_list[m][0])
            else:
                tmp = tmp * (0 - D_k_list[m][0]) / (D_k_list[j][0] - D_k_list[m][0])
        l_k_list.append(tmp)
        del tmp

    # calculate f(0) = a0
    f0 = 0.0
    for k in range(len(D_k_list)):
        f0 += D_k_list[k][1] * l_k_list[k]

    return f0


def main():
    n = 6  # number of shares
    k = 3  # number of shares required to reconstruct the secret
    test_score_list = [10, 20, 30, 40]  # example secret data
    sum_test_score = sum(test_score_list)
    print(f"sum_test_score: {sum_test_score}")

    for a0 in test_score_list:
        # -----Preparation-----

        # create random coefficients a1, a2, ..., ak-1
        coefficients = create_random_coefficients(k)
        an_list = [a0] + coefficients
        print_polynomial(an_list)

        # create points D(x-1) = (x, f(x))
        D_x_list = []
        # NOTE: D(0) = (1, a0)，D(1) = (2, a0 + a1 * 2)
        for x in range(n):
            D_x_list.append(create_points(x + 1, an_list))
        print_D_n_list(D_x_list)

        # -----Reconstruction-----
        # select k random points(D_x)
        random_points = random.sample(D_x_list, k)
        print(f"random_points D: {random_points}")

        # calcurate f(0) = a0 with Lagrange basis polynomial
        f0 = cal_lagrange_basis_for_polynomial(random_points)
        print(f"f(0) = {f0} = a0 = {a0}")


if __name__ == "__main__":
    main()
