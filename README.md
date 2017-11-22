# market-basket-analysis-with-instacart-data

![mba.png](/mba.png)

|     | antecedants                                           | consequents                                           |    support |   confidence |     lift |    leverage |   conviction |
|----:|:------------------------------------------------------|:------------------------------------------------------|-----------:|-------------:|---------:|------------:|-------------:|
|   0 | Bag of Organic Bananas                                | Organic Whole Milk                                    | 0.0135135  |    0.101538  |  1.77112 | 0.00588359  |      1.0492  |
|   1 | Organic Whole Milk                                    | Bag of Organic Bananas                                | 0.0135135  |    0.235714  |  1.77112 | 0.00588359  |      1.13428 |
|   2 | Banana                                                | Unsweetened Original Almond Breeze Almond Milk        | 0.00573301 |    0.0292887 |  1.93305 | 0.00276723  |      1.01456 |
|   3 | Unsweetened Original Almond Breeze Almond Milk        | Banana                                                | 0.00573301 |    0.378378  |  1.93305 | 0.00276723  |      1.29381 |
|   4 | Banana                                                | Organic Avocado                                       | 0.0159705  |    0.08159   |  1.45433 | 0.00498913  |      1.02775 |
|   5 | Organic Avocado                                       | Banana                                                | 0.0159705  |    0.284672  |  1.45433 | 0.00498913  |      1.12432 |
|   6 | Organic Cucumber                                      | Organic Hass Avocado                                  | 0.00859951 |    0.2625    |  3.35615 | 0.0060372   |      1.24988 |
|   7 | Organic Hass Avocado                                  | Organic Cucumber                                      | 0.00859951 |    0.109948  |  3.35615 | 0.0060372   |      1.08672 |
|   8 | Bag of Organic Bananas                                | Organic Large Extra Fancy Fuji Apple                  | 0.00819001 |    0.0615385 |  2.38535 | 0.00475654  |      1.03808 |
|   9 | Organic Large Extra Fancy Fuji Apple                  | Bag of Organic Bananas                                | 0.00819001 |    0.31746   |  2.38535 | 0.00475654  |      1.27013 |
|  10 | Limes                                                 | Organic Yellow Onion                                  | 0.00532351 |    0.0962963 |  1.9761  | 0.00262956  |      1.05263 |
|  11 | Organic Yellow Onion                                  | Limes                                                 | 0.00532351 |    0.109244  |  1.9761  | 0.00262956  |      1.06058 |
|  12 | Michigan Organic Kale                                 | Banana                                                | 0.00737101 |    0.305085  |  1.55861 | 0.0026418   |      1.15735 |
|  13 | Banana                                                | Michigan Organic Kale                                 | 0.00737101 |    0.0376569 |  1.55861 | 0.0026418   |      1.01402 |
|  14 | Bag of Organic Bananas                                | Organic Granny Smith Apple                            | 0.00655201 |    0.0492308 |  1.93906 | 0.00317304  |      1.02508 |
|  15 | Organic Granny Smith Apple                            | Bag of Organic Bananas                                | 0.00655201 |    0.258065  |  1.93906 | 0.00317304  |      1.16845 |
|  16 | Organic Hass Avocado                                  | Limes                                                 | 0.00900901 |    0.115183  |  2.08354 | 0.00468511  |      1.0677  |
|  17 | Limes                                                 | Organic Hass Avocado                                  | 0.00900901 |    0.162963  |  2.08354 | 0.00468511  |      1.10125 |
|  18 | Organic Hass Avocado                                  | Organic Garnet Sweet Potato (Yam)                     | 0.00614251 |    0.078534  |  3.09323 | 0.00415671  |      1.05767 |
|  19 | Organic Garnet Sweet Potato (Yam)                     | Organic Hass Avocado                                  | 0.00614251 |    0.241935  |  3.09323 | 0.00415671  |      1.21597 |
|  20 | Organic Hass Avocado                                  | Organic Strawberries                                  | 0.0200655  |    0.256545  |  2.54667 | 0.0121864   |      1.20957 |
|  21 | Organic Strawberries                                  | Organic Hass Avocado                                  | 0.0200655  |    0.199187  |  2.54667 | 0.0121864   |      1.15106 |
|  22 | Bag of Organic Bananas                                | Fresh Cauliflower                                     | 0.00696151 |    0.0523077 |  1.82479 | 0.00314655  |      1.02495 |
|  23 | Fresh Cauliflower                                     | Bag of Organic Bananas                                | 0.00696151 |    0.242857  |  1.82479 | 0.00314655  |      1.14498 |
|  24 | Organic Hass Avocado                                  | Organic Garlic                                        | 0.00614251 |    0.078534  |  2.10747 | 0.00322788  |      1.04479 |
|  25 | Organic Garlic                                        | Organic Hass Avocado                                  | 0.00614251 |    0.164835  |  2.10747 | 0.00322788  |      1.10372 |
|  26 | Organic Yellow Onion                                  | Large Lemon                                           | 0.00900901 |    0.184874  |  3.52705 | 0.00645475  |      1.1625  |
|  27 | Large Lemon                                           | Organic Yellow Onion                                  | 0.00900901 |    0.171875  |  3.52705 | 0.00645475  |      1.1487  |
|  28 | Banana                                                | Organic Red Bell Pepper                               | 0.00573301 |    0.0292887 |  1.25479 | 0.00116411  |      1.00613 |
|  29 | Organic Red Bell Pepper                               | Banana                                                | 0.00573301 |    0.245614  |  1.25479 | 0.00116411  |      1.06611 |
|  30 | Bag of Organic Bananas                                | Organic Zucchini                                      | 0.00941851 |    0.0707692 |  1.80019 | 0.00418656  |      1.03385 |
|  31 | Organic Zucchini                                      | Bag of Organic Bananas                                | 0.00941851 |    0.239583  |  1.80019 | 0.00418656  |      1.14005 |
|  32 | Organic Hass Avocado                                  | Organic Yellow Onion                                  | 0.00900901 |    0.115183  |  2.36368 | 0.00519757  |      1.0751  |
|  33 | Organic Yellow Onion                                  | Organic Hass Avocado                                  | 0.00900901 |    0.184874  |  2.36368 | 0.00519757  |      1.13085 |
|  34 | Organic Hass Avocado                                  | Organic Raspberries                                   | 0.0110565  |    0.141361  |  2.53827 | 0.00670058  |      1.09977 |
|  35 | Organic Raspberries                                   | Organic Hass Avocado                                  | 0.0110565  |    0.198529  |  2.53827 | 0.00670058  |      1.15012 |
|  36 | Limes                                                 | Organic Baby Spinach                                  | 0.00859951 |    0.155556  |  1.79182 | 0.0038002   |      1.0814  |
|  37 | Organic Baby Spinach                                  | Limes                                                 | 0.00859951 |    0.0990566 |  1.79182 | 0.0038002   |      1.04859 |
|  38 | Organic Blackberries                                  | Banana                                                | 0.00819001 |    0.392157  |  2.00345 | 0.00410205  |      1.32314 |
|  39 | Banana                                                | Organic Blackberries                                  | 0.00819001 |    0.041841  |  2.00345 | 0.00410205  |      1.02187 |
|  40 | Banana                                                | Cucumber Kirby                                        | 0.013104   |    0.0669456 |  1.5872  | 0.00484793  |      1.02654 |
|  41 | Cucumber Kirby                                        | Banana                                                | 0.013104   |    0.31068   |  1.5872  | 0.00484793  |      1.16674 |
|  42 | Yellow Onions                                         | Organic Baby Spinach                                  | 0.00532351 |    0.188406  |  2.17022 | 0.00287053  |      1.12518 |
|  43 | Organic Baby Spinach                                  | Yellow Onions                                         | 0.00532351 |    0.0613208 |  2.17022 | 0.00287053  |      1.03523 |
|  44 | Organic Strawberries                                  | Organic Baby Spinach                                  | 0.015561   |    0.154472  |  1.77934 | 0.00681562  |      1.08002 |
|  45 | Organic Baby Spinach                                  | Organic Strawberries                                  | 0.015561   |    0.179245  |  1.77934 | 0.00681562  |      1.09565 |
|  46 | Banana                                                | 100% Whole Wheat Bread                                | 0.00900901 |    0.0460251 |  1.70293 | 0.00371871  |      1.01991 |
|  47 | 100% Whole Wheat Bread                                | Banana                                                | 0.00900901 |    0.333333  |  1.70293 | 0.00371871  |      1.20639 |
|  48 | Seedless Red Grapes                                   | Strawberries                                          | 0.00573301 |    0.212121  |  3.54795 | 0.00411714  |      1.19335 |
|  49 | Strawberries                                          | Seedless Red Grapes                                   | 0.00573301 |    0.0958904 |  3.54795 | 0.00411714  |      1.07617 |
|  50 | Banana                                                | Strawberries                                          | 0.020475   |    0.104603  |  1.74958 | 0.00877223  |      1.05005 |
|  51 | Strawberries                                          | Banana                                                | 0.020475   |    0.342466  |  1.74958 | 0.00877223  |      1.22314 |
|  52 | Organic Garlic                                        | Organic Strawberries                                  | 0.00573301 |    0.153846  |  1.5272  | 0.00197908  |      1.06277 |
|  53 | Organic Strawberries                                  | Organic Garlic                                        | 0.00573301 |    0.0569106 |  1.5272  | 0.00197908  |      1.02083 |
|  54 | Organic Strawberries                                  | Organic Raspberries                                   | 0.0126945  |    0.126016  |  2.26273 | 0.00708426  |      1.08046 |
|  55 | Organic Raspberries                                   | Organic Strawberries                                  | 0.0126945  |    0.227941  |  2.26273 | 0.00708426  |      1.16476 |
|  56 | Bag of Organic Bananas,Organic Hass Avocado           | Organic Strawberries                                  | 0.00859951 |    0.375     |  3.72256 | 0.0062894   |      1.43882 |
|  57 | Bag of Organic Bananas,Organic Strawberries           | Organic Hass Avocado                                  | 0.00859951 |    0.328125  |  4.19519 | 0.00654966  |      1.37196 |
|  58 | Organic Hass Avocado,Organic Strawberries             | Bag of Organic Bananas                                | 0.00859951 |    0.428571  |  3.22022 | 0.00592904  |      1.5171  |
|  59 | Bag of Organic Bananas                                | Organic Hass Avocado,Organic Strawberries             | 0.00859951 |    0.0646154 |  3.22022 | 0.00592904  |      1.04763 |
|  60 | Organic Hass Avocado                                  | Bag of Organic Bananas,Organic Strawberries           | 0.00859951 |    0.109948  |  4.19519 | 0.00654966  |      1.09408 |
|  61 | Organic Strawberries                                  | Bag of Organic Bananas,Organic Hass Avocado           | 0.00859951 |    0.0853659 |  3.72256 | 0.0062894   |      1.06826 |
|  62 | Banana                                                | Organic Raspberries                                   | 0.013923   |    0.0711297 |  1.2772  | 0.00302178  |      1.01662 |
|  63 | Organic Raspberries                                   | Banana                                                | 0.013923   |    0.25      |  1.2772  | 0.00302178  |      1.07235 |
|  64 | Organic Cucumber                                      | Organic Strawberries                                  | 0.00819001 |    0.25      |  2.48171 | 0.00488986  |      1.19902 |
|  65 | Organic Strawberries                                  | Organic Cucumber                                      | 0.00819001 |    0.0813008 |  2.48171 | 0.00488986  |      1.05284 |
|  66 | Organic Lemon                                         | Organic Baby Spinach                                  | 0.00532351 |    0.151163  |  1.74122 | 0.00226617  |      1.07581 |
|  67 | Organic Baby Spinach                                  | Organic Lemon                                         | 0.00532351 |    0.0613208 |  1.74122 | 0.00226617  |      1.02781 |
|  68 | Bag of Organic Bananas                                | Organic Grape Tomatoes                                | 0.00778051 |    0.0584615 |  1.58626 | 0.00287556  |      1.02295 |
|  69 | Organic Grape Tomatoes                                | Bag of Organic Bananas                                | 0.00778051 |    0.211111  |  1.58626 | 0.00287556  |      1.0989  |
|  70 | Organic Hass Avocado                                  | Organic Large Extra Fancy Fuji Apple                  | 0.00532351 |    0.0680628 |  2.63824 | 0.00330568  |      1.04535 |
|  71 | Organic Large Extra Fancy Fuji Apple                  | Organic Hass Avocado                                  | 0.00532351 |    0.206349  |  2.63824 | 0.00330568  |      1.16145 |
|  72 | Organic Zucchini                                      | Organic Baby Spinach                                  | 0.00532351 |    0.135417  |  1.55985 | 0.00191067  |      1.05622 |
|  73 | Organic Baby Spinach                                  | Organic Zucchini                                      | 0.00532351 |    0.0613208 |  1.55985 | 0.00191067  |      1.02345 |
|  74 | Bunched Cilantro                                      | Banana                                                | 0.00532351 |    0.302326  |  1.54452 | 0.00187679  |      1.15277 |
|  75 | Banana                                                | Bunched Cilantro                                      | 0.00532351 |    0.0271967 |  1.54452 | 0.00187679  |      1.00986 |
|  76 | Banana                                                | Gala Apples                                           | 0.00532351 |    0.0271967 |  2.45979 | 0.00315929  |      1.01659 |
|  77 | Gala Apples                                           | Banana                                                | 0.00532351 |    0.481481  |  2.45979 | 0.00315929  |      1.55107 |
|  78 | Organic Hass Avocado                                  | Organic Whole Milk                                    | 0.00778051 |    0.0994764 |  1.73515 | 0.00329646  |      1.0468  |
|  79 | Organic Whole Milk                                    | Organic Hass Avocado                                  | 0.00778051 |    0.135714  |  1.73515 | 0.00329646  |      1.06653 |
|  80 | Organic Red Onion                                     | Organic Baby Spinach                                  | 0.00573301 |    0.208955  |  2.40693 | 0.00335113  |      1.1544  |
|  81 | Organic Baby Spinach                                  | Organic Red Onion                                     | 0.00573301 |    0.0660377 |  2.40693 | 0.00335113  |      1.04133 |
|  82 | Asparagus                                             | Banana                                                | 0.00532351 |    0.282609  |  1.44379 | 0.00163632  |      1.12109 |
|  83 | Banana                                                | Asparagus                                             | 0.00532351 |    0.0271967 |  1.44379 | 0.00163632  |      1.00859 |
|  84 | Bag of Organic Bananas                                | Organic Hass Avocado                                  | 0.022932   |    0.172308  |  2.20301 | 0.0125226   |      1.11368 |
|  85 | Organic Hass Avocado                                  | Bag of Organic Bananas                                | 0.022932   |    0.293194  |  2.20301 | 0.0125226   |      1.22652 |
|  86 | Bag of Organic Bananas                                | Organic Raspberries                                   | 0.0151515  |    0.113846  |  2.04421 | 0.00773959  |      1.06563 |
|  87 | Organic Raspberries                                   | Bag of Organic Bananas                                | 0.0151515  |    0.272059  |  2.04421 | 0.00773959  |      1.19091 |
|  88 | 100% Whole Wheat Bread                                | Organic Strawberries                                  | 0.00532351 |    0.19697   |  1.95528 | 0.00260088  |      1.11984 |
|  89 | Organic Strawberries                                  | 100% Whole Wheat Bread                                | 0.00532351 |    0.0528455 |  1.95528 | 0.00260088  |      1.02726 |
|  90 | Organic Garlic                                        | Large Lemon                                           | 0.00655201 |    0.175824  |  3.3544  | 0.00459875  |      1.14974 |
|  91 | Large Lemon                                           | Organic Garlic                                        | 0.00655201 |    0.125     |  3.3544  | 0.00459875  |      1.10027 |
|  92 | Banana                                                | Organic Garnet Sweet Potato (Yam)                     | 0.00696151 |    0.0355649 |  1.4008  | 0.00199183  |      1.01055 |
|  93 | Organic Garnet Sweet Potato (Yam)                     | Banana                                                | 0.00696151 |    0.274194  |  1.4008  | 0.00199183  |      1.10809 |
|  94 | Organic Baby Carrots                                  | Organic Strawberries                                  | 0.00614251 |    0.230769  |  2.29081 | 0.00346113  |      1.16904 |
|  95 | Organic Strawberries                                  | Organic Baby Carrots                                  | 0.00614251 |    0.0609756 |  2.29081 | 0.00346113  |      1.03659 |
|  96 | Organic Italian Parsley Bunch                         | Organic Baby Spinach                                  | 0.00614251 |    0.227273  |  2.61792 | 0.00379618  |      1.18177 |
|  97 | Organic Baby Spinach                                  | Organic Italian Parsley Bunch                         | 0.00614251 |    0.0707547 |  2.61792 | 0.00379618  |      1.04706 |
|  98 | Limes                                                 | Yellow Onions                                         | 0.00573301 |    0.103704  |  3.67021 | 0.00417097  |      1.08418 |
|  99 | Yellow Onions                                         | Limes                                                 | 0.00573301 |    0.202899  |  3.67021 | 0.00417097  |      1.18519 |
| 100 | Bag of Organic Bananas                                | Organic D'Anjou Pears                                 | 0.00696151 |    0.0523077 |  2.66115 | 0.00434553  |      1.03445 |
| 101 | Organic D'Anjou Pears                                 | Bag of Organic Bananas                                | 0.00696151 |    0.354167  |  2.66115 | 0.00434553  |      1.34232 |
| 102 | Organic Cilantro                                      | Organic Strawberries                                  | 0.00573301 |    0.215385  |  2.13809 | 0.00305163  |      1.14612 |
| 103 | Organic Strawberries                                  | Organic Cilantro                                      | 0.00573301 |    0.0569106 |  2.13809 | 0.00305163  |      1.03212 |
| 104 | Original Hummus                                       | Organic Strawberries                                  | 0.00614251 |    0.254237  |  2.52377 | 0.00370864  |      1.20583 |
| 105 | Organic Strawberries                                  | Original Hummus                                       | 0.00614251 |    0.0609756 |  2.52377 | 0.00370864  |      1.03921 |
| 106 | Bag of Organic Bananas                                | Organic Lemon                                         | 0.00859951 |    0.0646154 |  1.83478 | 0.00391256  |      1.03143 |
| 107 | Organic Lemon                                         | Bag of Organic Bananas                                | 0.00859951 |    0.244186  |  1.83478 | 0.00391256  |      1.14699 |
| 108 | Bag of Organic Bananas                                | Organic Garlic                                        | 0.00819001 |    0.0615385 |  1.65139 | 0.00323056  |      1.02587 |
| 109 | Organic Garlic                                        | Bag of Organic Bananas                                | 0.00819001 |    0.21978   |  1.65139 | 0.00323056  |      1.11111 |
| 110 | Strawberries                                          | Raspberries                                           | 0.00532351 |    0.0890411 |  4.83196 | 0.00422178  |      1.07752 |
| 111 | Raspberries                                           | Strawberries                                          | 0.00532351 |    0.288889  |  4.83196 | 0.00422178  |      1.32217 |
| 112 | Organic Strawberries                                  | Extra Virgin Olive Oil                                | 0.00532351 |    0.0528455 |  2.68852 | 0.00334341  |      1.03504 |
| 113 | Extra Virgin Olive Oil                                | Organic Strawberries                                  | 0.00532351 |    0.270833  |  2.68852 | 0.00334341  |      1.23327 |
| 114 | Banana                                                | Clementines, Bag                                      | 0.00532351 |    0.0271967 |  1.70293 | 0.00219742  |      1.01154 |
| 115 | Clementines, Bag                                      | Banana                                                | 0.00532351 |    0.333333  |  1.70293 | 0.00219742  |      1.20639 |
| 116 | Bag of Organic Bananas                                | Organic Baby Spinach                                  | 0.018018   |    0.135385  |  1.55948 | 0.00646414  |      1.05618 |
| 117 | Organic Baby Spinach                                  | Bag of Organic Bananas                                | 0.018018   |    0.207547  |  1.55948 | 0.00646414  |      1.09396 |
| 118 | Banana                                                | Organic Baby Spinach                                  | 0.023751   |    0.121339  |  1.39769 | 0.00675793  |      1.03929 |
| 119 | Organic Baby Spinach                                  | Banana                                                | 0.023751   |    0.273585  |  1.39769 | 0.00675793  |      1.10716 |
| 120 | Half & Half                                           | Organic Strawberries                                  | 0.00532351 |    0.19697   |  1.95528 | 0.00260088  |      1.11984 |
| 121 | Organic Strawberries                                  | Half & Half                                           | 0.00532351 |    0.0528455 |  1.95528 | 0.00260088  |      1.02726 |
| 122 | Green Beans                                           | Banana                                                | 0.00655201 |    0.516129  |  2.63679 | 0.00406717  |      1.66213 |
| 123 | Banana                                                | Green Beans                                           | 0.00655201 |    0.0334728 |  2.63679 | 0.00406717  |      1.0215  |
| 124 | Large Lemon                                           | Organic Strawberries                                  | 0.00737101 |    0.140625  |  1.39596 | 0.00209077  |      1.04642 |
| 125 | Organic Strawberries                                  | Large Lemon                                           | 0.00737101 |    0.0731707 |  1.39596 | 0.00209077  |      1.02239 |
| 126 | Apple Honeycrisp Organic                              | Organic Yellow Onion                                  | 0.00532351 |    0.158537  |  3.25333 | 0.00368718  |      1.13049 |
| 127 | Organic Yellow Onion                                  | Apple Honeycrisp Organic                              | 0.00532351 |    0.109244  |  3.25333 | 0.00368718  |      1.08494 |
| 128 | Limes                                                 | Large Lemon                                           | 0.010647   |    0.192593  |  3.67431 | 0.00774932  |      1.17361 |
| 129 | Large Lemon                                           | Limes                                                 | 0.010647   |    0.203125  |  3.67431 | 0.00774932  |      1.18553 |
| 130 | Banana                                                | Organic Fuji Apple                                    | 0.0167895  |    0.0857741 |  2.52362 | 0.0101366   |      1.05664 |
| 131 | Organic Fuji Apple                                    | Banana                                                | 0.0167895  |    0.493976  |  2.52362 | 0.0101366   |      1.58937 |
| 132 | Limes                                                 | Jalapeno Peppers                                      | 0.00532351 |    0.0962963 |  7.34861 | 0.00459908  |      1.09206 |
| 133 | Jalapeno Peppers                                      | Limes                                                 | 0.00532351 |    0.40625   |  7.34861 | 0.00459908  |      1.5911  |
| 134 | Bag of Organic Bananas                                | Organic Italian Parsley Bunch                         | 0.00614251 |    0.0461538 |  1.70769 | 0.00254554  |      1.02005 |
| 135 | Organic Italian Parsley Bunch                         | Bag of Organic Bananas                                | 0.00614251 |    0.227273  |  1.70769 | 0.00254554  |      1.12189 |
| 136 | Organic Garnet Sweet Potato (Yam)                     | Organic Baby Spinach                                  | 0.00696151 |    0.274194  |  3.1584  | 0.00475738  |      1.25817 |
| 137 | Organic Baby Spinach                                  | Organic Garnet Sweet Potato (Yam)                     | 0.00696151 |    0.0801887 |  3.1584  | 0.00475738  |      1.05958 |
| 138 | Limes                                                 | Organic Avocado                                       | 0.00819001 |    0.148148  |  2.64071 | 0.00508857  |      1.10805 |
| 139 | Organic Avocado                                       | Limes                                                 | 0.00819001 |    0.145985  |  2.64071 | 0.00508857  |      1.10621 |
| 140 | Organic Yellow Onion                                  | Organic Zucchini                                      | 0.00655201 |    0.134454  |  3.42017 | 0.00463631  |      1.10992 |
| 141 | Organic Zucchini                                      | Organic Yellow Onion                                  | 0.00655201 |    0.166667  |  3.42017 | 0.00463631  |      1.14152 |
| 142 | Organic Avocado                                       | Cucumber Kirby                                        | 0.00737101 |    0.131387  |  3.11502 | 0.00500473  |      1.1027  |
| 143 | Cucumber Kirby                                        | Organic Avocado                                       | 0.00737101 |    0.174757  |  3.11502 | 0.00500473  |      1.14378 |
| 144 | Cucumber Kirby                                        | Organic Baby Spinach                                  | 0.00737101 |    0.174757  |  2.01301 | 0.00370932  |      1.10657 |
| 145 | Organic Baby Spinach                                  | Cucumber Kirby                                        | 0.00737101 |    0.0849057 |  2.01301 | 0.00370932  |      1.04669 |
| 146 | Banana                                                | Organic Grape Tomatoes                                | 0.00982801 |    0.0502092 |  1.36234 | 0.00261396  |      1.01406 |
| 147 | Organic Grape Tomatoes                                | Banana                                                | 0.00982801 |    0.266667  |  1.36234 | 0.00261396  |      1.09672 |
| 148 | Banana                                                | Yellow Onions                                         | 0.00859951 |    0.0439331 |  1.55485 | 0.00306874  |      1.0164  |
| 149 | Yellow Onions                                         | Banana                                                | 0.00859951 |    0.304348  |  1.55485 | 0.00306874  |      1.15612 |
| 150 | Bag of Organic Bananas                                | Organic Blueberries                                   | 0.00614251 |    0.0461538 |  1.34176 | 0.00156455  |      1.01232 |
| 151 | Organic Blueberries                                   | Bag of Organic Bananas                                | 0.00614251 |    0.178571  |  1.34176 | 0.00156455  |      1.05537 |
| 152 | Organic Strawberries                                  | Organic Whole String Cheese                           | 0.00737101 |    0.0731707 |  2.88198 | 0.00481339  |      1.05155 |
| 153 | Organic Whole String Cheese                           | Organic Strawberries                                  | 0.00737101 |    0.290323  |  2.88198 | 0.00481339  |      1.26714 |
| 154 | Banana                                                | Bartlett Pears                                        | 0.00614251 |    0.0313808 |  2.25388 | 0.0034172   |      1.01802 |
| 155 | Bartlett Pears                                        | Banana                                                | 0.00614251 |    0.441176  |  2.25388 | 0.0034172   |      1.4392  |
| 156 | Organic Hass Avocado                                  | Organic Lemon                                         | 0.00900901 |    0.115183  |  3.27067 | 0.00625452  |      1.09038 |
| 157 | Organic Lemon                                         | Organic Hass Avocado                                  | 0.00900901 |    0.255814  |  3.27067 | 0.00625452  |      1.23865 |
| 158 | Limes                                                 | Banana                                                | 0.0159705  |    0.288889  |  1.47587 | 0.00514944  |      1.13099 |
| 159 | Banana                                                | Limes                                                 | 0.0159705  |    0.08159   |  1.47587 | 0.00514944  |      1.02864 |
| 160 | Organic Garlic                                        | Organic Yellow Onion                                  | 0.0110565  |    0.296703  |  6.08865 | 0.00924059  |      1.35259 |
| 161 | Organic Yellow Onion                                  | Organic Garlic                                        | 0.0110565  |    0.226891  |  6.08865 | 0.00924059  |      1.24528 |
| 162 | Bag of Organic Bananas                                | Organic Tomato Cluster                                | 0.00696151 |    0.0523077 |  1.99587 | 0.00347354  |      1.02754 |
| 163 | Organic Tomato Cluster                                | Bag of Organic Bananas                                | 0.00696151 |    0.265625  |  1.99587 | 0.00347354  |      1.18048 |
| 164 | Total 2% Lowfat Greek Strained Yogurt With Blueberry  | Total 2% with Strawberry Lowfat Greek Strained Yogurt | 0.00532351 |    0.5       | 45.2222  | 0.00520579  |      1.97789 |
| 165 | Total 2% with Strawberry Lowfat Greek Strained Yogurt | Total 2% Lowfat Greek Strained Yogurt With Blueberry  | 0.00532351 |    0.481481  | 45.2222  | 0.00520579  |      1.90804 |
| 166 | Organic Garlic                                        | Organic Baby Spinach                                  | 0.00737101 |    0.197802  |  2.27846 | 0.00413592  |      1.13836 |
| 167 | Organic Baby Spinach                                  | Organic Garlic                                        | 0.00737101 |    0.0849057 |  2.27846 | 0.00413592  |      1.05206 |
| 168 | Honeycrisp Apple                                      | Banana                                                | 0.0118755  |    0.402778  |  2.05771 | 0.00610427  |      1.34667 |
| 169 | Banana                                                | Honeycrisp Apple                                      | 0.0118755  |    0.0606695 |  2.05771 | 0.00610427  |      1.0332  |
| 170 | Banana                                                | Organic Strawberries                                  | 0.0241605  |    0.123431  |  1.22528 | 0.00444212  |      1.02589 |
| 171 | Organic Strawberries                                  | Banana                                                | 0.0241605  |    0.239837  |  1.22528 | 0.00444212  |      1.05801 |
| 172 | Organic Yellow Onion                                  | Carrots                                               | 0.00655201 |    0.134454  |  4.26411 | 0.00501546  |      1.11891 |
| 173 | Carrots                                               | Organic Yellow Onion                                  | 0.00655201 |    0.207792  |  4.26411 | 0.00501546  |      1.20078 |
| 174 | Organic Raspberries                                   | Organic Baby Spinach                                  | 0.00737101 |    0.132353  |  1.52456 | 0.00253615  |      1.05249 |
| 175 | Organic Baby Spinach                                  | Organic Raspberries                                   | 0.00737101 |    0.0849057 |  1.52456 | 0.00253615  |      1.03192 |
| 176 | Banana                                                | Large Lemon                                           | 0.0167895  |    0.0857741 |  1.63641 | 0.00652954  |      1.03649 |
| 177 | Large Lemon                                           | Banana                                                | 0.0167895  |    0.320312  |  1.63641 | 0.00652954  |      1.18328 |
| 178 | Organic Gala Apples                                   | Organic Strawberries                                  | 0.00655201 |    0.242424  |  2.4065  | 0.00382938  |      1.18703 |
| 179 | Organic Strawberries                                  | Organic Gala Apples                                   | 0.00655201 |    0.0650407 |  2.4065  | 0.00382938  |      1.04066 |
| 180 | Organic Blueberries                                   | Organic Strawberries                                  | 0.00819001 |    0.238095  |  2.36353 | 0.00472485  |      1.18028 |
| 181 | Organic Strawberries                                  | Organic Blueberries                                   | 0.00819001 |    0.0813008 |  2.36353 | 0.00472485  |      1.05105 |
| 182 | Organic Hass Avocado                                  | Organic Baby Spinach                                  | 0.00941851 |    0.120419  |  1.38709 | 0.00262838  |      1.03821 |
| 183 | Organic Baby Spinach                                  | Organic Hass Avocado                                  | 0.00941851 |    0.108491  |  1.38709 | 0.00262838  |      1.03396 |
| 184 | Organic Strawberries                                  | Organic Yellow Peaches                                | 0.00614251 |    0.0609756 |  6.20427 | 0.00515246  |      1.05447 |
| 185 | Organic Yellow Peaches                                | Organic Strawberries                                  | 0.00614251 |    0.625     |  6.20427 | 0.00515246  |      2.39803 |
| 186 | Banana                                                | Broccoli Crown                                        | 0.00819001 |    0.041841  |  2.83821 | 0.00530439  |      1.02828 |
| 187 | Broccoli Crown                                        | Banana                                                | 0.00819001 |    0.555556  |  2.83821 | 0.00530439  |      1.80958 |
| 188 | Large Lemon                                           | Cucumber Kirby                                        | 0.00573301 |    0.109375  |  2.59314 | 0.00352217  |      1.07545 |
| 189 | Cucumber Kirby                                        | Large Lemon                                           | 0.00573301 |    0.135922  |  2.59314 | 0.00352217  |      1.09664 |
| 190 | Organic Avocado                                       | Organic Zucchini                                      | 0.00532351 |    0.0948905 |  2.41378 | 0.00311804  |      1.06141 |
| 191 | Organic Zucchini                                      | Organic Avocado                                       | 0.00532351 |    0.135417  |  2.41378 | 0.00311804  |      1.09174 |
| 192 | Bag of Organic Bananas                                | Organic Gala Apples                                   | 0.00655201 |    0.0492308 |  1.82154 | 0.00295504  |      1.02335 |
| 193 | Organic Gala Apples                                   | Bag of Organic Bananas                                | 0.00655201 |    0.242424  |  1.82154 | 0.00295504  |      1.14432 |
| 194 | Bag of Organic Bananas                                | Organic Avocado                                       | 0.00941851 |    0.0707692 |  1.26145 | 0.00195209  |      1.01578 |
| 195 | Organic Avocado                                       | Bag of Organic Bananas                                | 0.00941851 |    0.167883  |  1.26145 | 0.00195209  |      1.04182 |
| 196 | Organic Garlic                                        | Organic Red Onion                                     | 0.00532351 |    0.142857  |  5.20682 | 0.0043011   |      1.13466 |
| 197 | Organic Red Onion                                     | Organic Garlic                                        | 0.00532351 |    0.19403   |  5.20682 | 0.0043011   |      1.19451 |
| 198 | Banana                                                | Organic Whole String Cheese                           | 0.00737101 |    0.0376569 |  1.4832  | 0.00240133  |      1.01275 |
| 199 | Organic Whole String Cheese                           | Banana                                                | 0.00737101 |    0.290323  |  1.4832  | 0.00240133  |      1.13327 |
| 200 | Bag of Organic Bananas                                | Carrots                                               | 0.00737101 |    0.0553846 |  1.75648 | 0.00317455  |      1.02525 |
| 201 | Carrots                                               | Bag of Organic Bananas                                | 0.00737101 |    0.233766  |  1.75648 | 0.00317455  |      1.13139 |
| 202 | Bag of Organic Bananas                                | Organic Small Bunch Celery                            | 0.00532351 |    0.04      |  1.65559 | 0.00210804  |      1.0165  |
| 203 | Organic Small Bunch Celery                            | Bag of Organic Bananas                                | 0.00532351 |    0.220339  |  1.65559 | 0.00210804  |      1.11191 |
| 204 | Organic Blueberries                                   | Organic Baby Spinach                                  | 0.00532351 |    0.154762  |  1.78268 | 0.00233727  |      1.08039 |
| 205 | Organic Baby Spinach                                  | Organic Blueberries                                   | 0.00532351 |    0.0613208 |  1.78268 | 0.00233727  |      1.02868 |
| 206 | Banana                                                | Orange Bell Pepper                                    | 0.00655201 |    0.0334728 |  1.81646 | 0.00294498  |      1.01557 |
| 207 | Orange Bell Pepper                                    | Banana                                                | 0.00655201 |    0.355556  |  1.81646 | 0.00294498  |      1.24799 |
| 208 | Organic Peeled Whole Baby Carrots                     | Banana                                                | 0.00655201 |    0.280702  |  1.43405 | 0.00198311  |      1.11812 |
| 209 | Banana                                                | Organic Peeled Whole Baby Carrots                     | 0.00655201 |    0.0334728 |  1.43405 | 0.00198311  |      1.01048 |
| 210 | Banana                                                | Red Vine Tomato                                       | 0.00655201 |    0.0334728 |  1.81646 | 0.00294498  |      1.01557 |
| 211 | Red Vine Tomato                                       | Banana                                                | 0.00655201 |    0.355556  |  1.81646 | 0.00294498  |      1.24799 |
| 212 | Bag of Organic Bananas                                | Organic Cucumber                                      | 0.011466   |    0.0861538 |  2.62985 | 0.00710606  |      1.05843 |
| 213 | Organic Cucumber                                      | Bag of Organic Bananas                                | 0.011466   |    0.35      |  2.62985 | 0.00710606  |      1.33371 |
| 214 | Organic Grape Tomatoes                                | Organic Baby Spinach                                  | 0.00655201 |    0.177778  |  2.0478  | 0.00335247  |      1.11063 |
| 215 | Organic Baby Spinach                                  | Organic Grape Tomatoes                                | 0.00655201 |    0.0754717 |  2.0478  | 0.00335247  |      1.04177 |
| 216 | Bag of Organic Bananas                                | 100% Whole Wheat Bread                                | 0.00655201 |    0.0492308 |  1.82154 | 0.00295504  |      1.02335 |
| 217 | 100% Whole Wheat Bread                                | Bag of Organic Bananas                                | 0.00655201 |    0.242424  |  1.82154 | 0.00295504  |      1.14432 |
| 218 | Organic Red Onion                                     | Organic Zucchini                                      | 0.00532351 |    0.19403   |  4.93563 | 0.00424492  |      1.19196 |
| 219 | Organic Zucchini                                      | Organic Red Onion                                     | 0.00532351 |    0.135417  |  4.93563 | 0.00424492  |      1.12489 |
| 220 | Banana                                                | Organic Reduced Fat Milk                              | 0.00532351 |    0.0271967 |  1.79498 | 0.00235773  |      1.01238 |
| 221 | Organic Reduced Fat Milk                              | Banana                                                | 0.00532351 |    0.351351  |  1.79498 | 0.00235773  |      1.2399  |
| 222 | Organic Cucumber                                      | Organic Whole Milk                                    | 0.00614251 |    0.1875    |  3.27054 | 0.00426437  |      1.16021 |
| 223 | Organic Whole Milk                                    | Organic Cucumber                                      | 0.00614251 |    0.107143  |  3.27054 | 0.00426437  |      1.08331 |
| 224 | Strawberries                                          | Cucumber Kirby                                        | 0.00573301 |    0.0958904 |  2.27344 | 0.00321127  |      1.05941 |
| 225 | Cucumber Kirby                                        | Strawberries                                          | 0.00573301 |    0.135922  |  2.27344 | 0.00321127  |      1.08811 |
| 226 | Fresh Cauliflower                                     | Organic Zucchini                                      | 0.00532351 |    0.185714  |  4.72411 | 0.00419662  |      1.17979 |
| 227 | Organic Zucchini                                      | Fresh Cauliflower                                     | 0.00532351 |    0.135417  |  4.72411 | 0.00419662  |      1.12347 |
| 228 | Banana                                                | Original Hummus                                       | 0.00573301 |    0.0292887 |  1.21225 | 0.0010038   |      1.00528 |
| 229 | Original Hummus                                       | Banana                                                | 0.00573301 |    0.237288  |  1.21225 | 0.0010038   |      1.05447 |
| 230 | Organic Grape Tomatoes                                | Organic Strawberries                                  | 0.00655201 |    0.177778  |  1.76477 | 0.00283934  |      1.0937  |
| 231 | Organic Strawberries                                  | Organic Grape Tomatoes                                | 0.00655201 |    0.0650407 |  1.76477 | 0.00283934  |      1.03015 |
| 232 | Organic Strawberries                                  | Green Bell Pepper                                     | 0.00532351 |    0.0528455 |  2.38979 | 0.0030959   |      1.03245 |
| 233 | Green Bell Pepper                                     | Organic Strawberries                                  | 0.00532351 |    0.240741  |  2.38979 | 0.0030959   |      1.1844  |
| 234 | Bag of Organic Bananas                                | Organic Yellow Onion                                  | 0.0102375  |    0.0769231 |  1.57854 | 0.00375208  |      1.03054 |
| 235 | Organic Yellow Onion                                  | Bag of Organic Bananas                                | 0.0102375  |    0.210084  |  1.57854 | 0.00375208  |      1.09747 |
| 236 | Large Lemon                                           | Organic Avocado                                       | 0.00900901 |    0.171875  |  3.06364 | 0.00606839  |      1.1398  |
| 237 | Organic Avocado                                       | Large Lemon                                           | 0.00900901 |    0.160584  |  3.06364 | 0.00606839  |      1.12886 |
| 238 | Organic Yellow Onion                                  | Organic Strawberries                                  | 0.0102375  |    0.210084  |  2.08547 | 0.00532854  |      1.13843 |
| 239 | Organic Strawberries                                  | Organic Yellow Onion                                  | 0.0102375  |    0.101626  |  2.08547 | 0.00532854  |      1.05888 |
| 240 | Large Lemon                                           | Organic Baby Spinach                                  | 0.011466   |    0.21875   |  2.51975 | 0.00691556  |      1.16888 |
| 241 | Organic Baby Spinach                                  | Large Lemon                                           | 0.011466   |    0.132075  |  2.51975 | 0.00691556  |      1.09178 |
| 242 | Bunched Cilantro                                      | Limes                                                 | 0.00532351 |    0.302326  |  5.46873 | 0.00435006  |      1.3541  |
| 243 | Limes                                                 | Bunched Cilantro                                      | 0.00532351 |    0.0962963 |  5.46873 | 0.00435006  |      1.08707 |
| 244 | Organic Avocado                                       | Organic Baby Spinach                                  | 0.00859951 |    0.153285  |  1.76567 | 0.0037291   |      1.0785  |
| 245 | Organic Baby Spinach                                  | Organic Avocado                                       | 0.00859951 |    0.0990566 |  1.76567 | 0.0037291   |      1.04768 |
| 246 | Bag of Organic Bananas                                | Organic Whole String Cheese                           | 0.00655201 |    0.0492308 |  1.93906 | 0.00317304  |      1.02508 |
| 247 | Organic Whole String Cheese                           | Bag of Organic Bananas                                | 0.00655201 |    0.258065  |  1.93906 | 0.00317304  |      1.16845 |
| 248 | Banana                                                | Carrots                                               | 0.00778051 |    0.039749  |  1.26061 | 0.00160849  |      1.00856 |
| 249 | Carrots                                               | Banana                                                | 0.00778051 |    0.246753  |  1.26061 | 0.00160849  |      1.06772 |
| 250 | Banana                                                | Extra Virgin Olive Oil                                | 0.00573301 |    0.0292887 |  1.49006 | 0.00188551  |      1.00992 |
| 251 | Extra Virgin Olive Oil                                | Banana                                                | 0.00573301 |    0.291667  |  1.49006 | 0.00188551  |      1.13542 |
| 252 | Honeycrisp Apple                                      | Organic Strawberries                                  | 0.00614251 |    0.208333  |  2.06809 | 0.00317237  |      1.13591 |
| 253 | Organic Strawberries                                  | Honeycrisp Apple                                      | 0.00614251 |    0.0609756 |  2.06809 | 0.00317237  |      1.03354 |
| 254 | Bag of Organic Bananas                                | Organic Cilantro                                      | 0.00532351 |    0.04      |  1.50277 | 0.00178104  |      1.01394 |
| 255 | Organic Cilantro                                      | Bag of Organic Bananas                                | 0.00532351 |    0.2       |  1.50277 | 0.00178104  |      1.08364 |
| 256 | Bag of Organic Bananas                                | Organic Peeled Whole Baby Carrots                     | 0.00573301 |    0.0430769 |  1.84551 | 0.00262654  |      1.02062 |
| 257 | Organic Peeled Whole Baby Carrots                     | Bag of Organic Bananas                                | 0.00573301 |    0.245614  |  1.84551 | 0.00262654  |      1.14916 |
| 258 | Organic Italian Parsley Bunch                         | Organic Strawberries                                  | 0.00532351 |    0.19697   |  1.95528 | 0.00260088  |      1.11984 |
| 259 | Organic Strawberries                                  | Organic Italian Parsley Bunch                         | 0.00532351 |    0.0528455 |  1.95528 | 0.00260088  |      1.02726 |
| 260 | Organic Yellow Onion                                  | Organic Whole Milk                                    | 0.00614251 |    0.12605   |  2.19868 | 0.00334878  |      1.07863 |
| 261 | Organic Whole Milk                                    | Organic Yellow Onion                                  | 0.00614251 |    0.107143  |  2.19868 | 0.00334878  |      1.06542 |
| 262 | Organic Red Onion                                     | Large Lemon                                           | 0.00614251 |    0.223881  |  4.27122 | 0.00470439  |      1.22093 |
| 263 | Large Lemon                                           | Organic Red Onion                                     | 0.00614251 |    0.117187  |  4.27122 | 0.00470439  |      1.10166 |
| 264 | Boneless Skinless Chicken Breasts                     | Banana                                                | 0.00614251 |    0.348837  |  1.78213 | 0.00269579  |      1.23511 |
| 265 | Banana                                                | Boneless Skinless Chicken Breasts                     | 0.00614251 |    0.0313808 |  1.78213 | 0.00269579  |      1.01422 |
| 266 | Seedless Red Grapes                                   | Banana                                                | 0.0110565  |    0.409091  |  2.08996 | 0.00576621  |      1.36105 |
| 267 | Banana                                                | Seedless Red Grapes                                   | 0.0110565  |    0.0564854 |  2.08996 | 0.00576621  |      1.03122 |
| 268 | Organic Zucchini                                      | Organic Strawberries                                  | 0.00655201 |    0.166667  |  1.65447 | 0.00259183  |      1.07912 |
| 269 | Organic Strawberries                                  | Organic Zucchini                                      | 0.00655201 |    0.0650407 |  1.65447 | 0.00259183  |      1.02752 |
| 270 | Bag of Organic Bananas                                | Apple Honeycrisp Organic                              | 0.00941851 |    0.0707692 |  2.10754 | 0.00494956  |      1.04002 |
| 271 | Apple Honeycrisp Organic                              | Bag of Organic Bananas                                | 0.00941851 |    0.280488  |  2.10754 | 0.00494956  |      1.20486 |
| 272 | Organic Whole Milk                                    | Organic Baby Spinach                                  | 0.00819001 |    0.142857  |  1.64555 | 0.00321295  |      1.06538 |
| 273 | Organic Baby Spinach                                  | Organic Whole Milk                                    | 0.00819001 |    0.0943396 |  1.64555 | 0.00321295  |      1.04086 |
| 274 | Organic Garlic                                        | Organic Italian Parsley Bunch                         | 0.00614251 |    0.164835  |  6.0989  | 0.00513536  |      1.16501 |
| 275 | Organic Italian Parsley Bunch                         | Organic Garlic                                        | 0.00614251 |    0.227273  |  6.0989  | 0.00513536  |      1.24589 |
| 276 | Organic Hass Avocado                                  | Organic Cilantro                                      | 0.00655201 |    0.0837696 |  3.14716 | 0.00447013  |      1.06238 |
| 277 | Organic Cilantro                                      | Organic Hass Avocado                                  | 0.00655201 |    0.246154  |  3.14716 | 0.00447013  |      1.22278 |
| 278 | Organic Hass Avocado                                  | Apple Honeycrisp Organic                              | 0.00819001 |    0.104712  |  3.11838 | 0.00556364  |      1.07945 |
| 279 | Apple Honeycrisp Organic                              | Organic Hass Avocado                                  | 0.00819001 |    0.243902  |  3.11838 | 0.00556364  |      1.21914 |
| 280 | Banana                                                | Small Hass Avocado                                    | 0.00532351 |    0.0271967 |  1.38363 | 0.00147601  |      1.00775 |
| 281 | Small Hass Avocado                                    | Banana                                                | 0.00532351 |    0.270833  |  1.38363 | 0.00147601  |      1.10298 |
| 282 | Organic Avocado                                       | Organic Grape Tomatoes                                | 0.00573301 |    0.10219   |  2.77275 | 0.00366538  |      1.07277 |
| 283 | Organic Grape Tomatoes                                | Organic Avocado                                       | 0.00573301 |    0.155556  |  2.77275 | 0.00366538  |      1.11777 |
| 284 | Organic Hass Avocado                                  | Organic Tomato Cluster                                | 0.00737101 |    0.0942408 |  3.59588 | 0.00532116  |      1.07511 |
| 285 | Organic Tomato Cluster                                | Organic Hass Avocado                                  | 0.00737101 |    0.28125   |  3.59588 | 0.00532116  |      1.28248 |
| 286 | Bag of Organic Bananas                                | Limes                                                 | 0.00982801 |    0.0738462 |  1.33579 | 0.00247059  |      1.02004 |
| 287 | Limes                                                 | Bag of Organic Bananas                                | 0.00982801 |    0.177778  |  1.33579 | 0.00247059  |      1.05435 |
| 288 | Bag of Organic Bananas                                | Organic Kiwi                                          | 0.00737101 |    0.0553846 |  2.81769 | 0.00475503  |      1.03782 |
| 289 | Organic Kiwi                                          | Bag of Organic Bananas                                | 0.00737101 |    0.375     |  2.81769 | 0.00475503  |      1.38706 |
| 290 | Organic Baby Arugula                                  | Organic Baby Spinach                                  | 0.00573301 |    0.259259  |  2.98637 | 0.00381328  |      1.2328  |
| 291 | Organic Baby Spinach                                  | Organic Baby Arugula                                  | 0.00573301 |    0.0660377 |  2.98637 | 0.00381328  |      1.04703 |
| 292 | Organic Lemon                                         | Organic Strawberries                                  | 0.00737101 |    0.209302  |  2.07771 | 0.00382335  |      1.1373  |
| 293 | Organic Strawberries                                  | Organic Lemon                                         | 0.00737101 |    0.0731707 |  2.07771 | 0.00382335  |      1.04095 |
| 294 | Bag of Organic Bananas                                | Organic Strawberries                                  | 0.026208   |    0.196923  |  1.95482 | 0.0128012   |      1.11977 |
| 295 | Organic Strawberries                                  | Bag of Organic Bananas                                | 0.026208   |    0.260163  |  1.95482 | 0.0128012   |      1.17176 |
| 296 | Organic Lemon                                         | Organic Garlic                                        | 0.00532351 |    0.151163  |  4.05648 | 0.00401116  |      1.13418 |
| 297 | Organic Garlic                                        | Organic Lemon                                         | 0.00532351 |    0.142857  |  4.05648 | 0.00401116  |      1.12558 |
| 298 | Organic Baby Arugula                                  | Banana                                                | 0.00532351 |    0.240741  |  1.22989 | 0.000995076 |      1.05927 |
| 299 | Banana                                                | Organic Baby Arugula                                  | 0.00532351 |    0.0271967 |  1.22989 | 0.000995076 |      1.00523 |
| 300 | Organic Avocado                                       | Organic Strawberries                                  | 0.00941851 |    0.167883  |  1.66655 | 0.003767    |      1.08069 |
| 301 | Organic Strawberries                                  | Organic Avocado                                       | 0.00941851 |    0.0934959 |  1.66655 | 0.003767    |      1.04125 |
| 302 | Limes                                                 | Organic Strawberries                                  | 0.00696151 |    0.125926  |  1.25005 | 0.0013925   |      1.02882 |
| 303 | Organic Strawberries                                  | Limes                                                 | 0.00696151 |    0.0691057 |  1.25005 | 0.0013925   |      1.01485 |
| 304 | Organic Hass Avocado                                  | Organic Ginger Root                                   | 0.00655201 |    0.0837696 |  3.58887 | 0.00472636  |      1.06595 |
| 305 | Organic Ginger Root                                   | Organic Hass Avocado                                  | 0.00655201 |    0.280702  |  3.58887 | 0.00472636  |      1.28151 |
| 306 | Apple Honeycrisp Organic                              | Organic Strawberries                                  | 0.00900901 |    0.268293  |  2.6633  | 0.00562635  |      1.22899 |
| 307 | Organic Strawberries                                  | Apple Honeycrisp Organic                              | 0.00900901 |    0.0894309 |  2.6633  | 0.00562635  |      1.06134 |
| 308 | Organic Whole Milk                                    | Organic Strawberries                                  | 0.0143325  |    0.25      |  2.48171 | 0.00855725  |      1.19902 |
| 309 | Organic Strawberries                                  | Organic Whole Milk                                    | 0.0143325  |    0.142276  |  2.48171 | 0.00855725  |      1.09904 |

