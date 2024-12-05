# shamir's secret sharing

![un license](https://img.shields.io/github/license/RyosukeDTomita/shamir_secret_sharing)

## INDEX

- [ABOUT](#about)
- [ENVIRONMENT](#environment)
- [PREPARING](#preparing)
- [INSTALL](#install)
- [HOW TO USE](#how-to-use)
- [DEVELOPER MEMO](#developer-memo)

---

## ABOUT

- [A. Shamir, “How to share a secret,” Commun. ACM,vol. 22, no. 11, pp. 612–613, 1979.](https://web.mit.edu/6.857/OldStuff/Fall03/ref/Shamir-HowToShareASecret.pdf)
- [Wikipedia](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing)


## HOW TO USE

```shell
python3 shamir_secret_sharing.py
f(x) = 10 + 44x^1 + 51x^2
D_0 = [1, 105]
D_1 = [2, 302]
D_2 = [3, 601]
D_3 = [4, 1002]
D_4 = [5, 1505]
D_5 = [6, 2110]
random_points D: [[2, 302], [3, 601], [5, 1505]]
f(0) = 10.0 = a0 = 10
----------DONE----------
f(x) = 20 + 63x^1 + 76x^2
D_0 = [1, 159]
D_1 = [2, 450]
D_2 = [3, 893]
D_3 = [4, 1488]
D_4 = [5, 2235]
D_5 = [6, 3134]
random_points D: [[1, 159], [6, 3134], [3, 893]]
f(0) = 20.0 = a0 = 20
----------DONE----------
f(x) = 30 + 44x^1 + 53x^2
D_0 = [1, 127]
D_1 = [2, 330]
D_2 = [3, 639]
D_3 = [4, 1054]
D_4 = [5, 1575]
D_5 = [6, 2202]
random_points D: [[3, 639], [1, 127], [5, 1575]]
f(0) = 30.0 = a0 = 30
----------DONE----------
f(x) = 40 + 86x^1 + 88x^2
D_0 = [1, 214]
D_1 = [2, 564]
D_2 = [3, 1090]
D_3 = [4, 1792]
D_4 = [5, 2670]
D_5 = [6, 3724]
random_points D: [[5, 2670], [3, 1090], [4, 1792]]
f(0) = 40.0 = a0 = 40
```
