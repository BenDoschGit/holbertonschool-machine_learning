#!/usr/bin/env python3
"""Module containing the function deep_rnn  that performs forward propagation
for a deep RNN."""

import numpy as np


def deep_rnn(rnn_cells, X, h_0):
    """Function that performs forward propagation for a deep RNN.

    Args:
        rnn_cells (list[RNNCell]): A list of instances of length l that will be
            used for the forward propagation, where l is the number of layers.
        X (numpy.ndarray): A tensor of shape (t, m, i) containing the data to
            be used, where t is the maximum number of time steps, m is the
            batch size, and i is the dimensionality of the data.
        h_0 (numpy.ndarray): A tensor of shape (l, m, h) containing the initial
            hidden state, where l is the number of layers, m is the batch size,
            and h is the dimensionality of the hidden state.

    Returns:
        H (numpy.ndarray): A tensor of shape (t+1, l, m, h) containing all of
            the hidden states, where t is the maximum number of time steps, l
            is the number of layers, m is the batch size, and h is the
            dimensionality of the hidden state.
        Y (numpy.ndarray): A tensor of shape (t, m, o) containing all of the
            outputs, where t is the maximum number of time steps, m is the
            batch size, and o is the dimensionality of the outputs.
    """
    T, _, _ = X.shape
    L, m, h = h_0.shape
    o = rnn_cells[-1].by.shape[1]
    H = np.zeros((T + 1, L, m, h))
    H[0, :, :, :] = h_0[None, ...]
    Y = np.zeros((T, m, o))

    for t in range(T):
        for lay in range(L):
            if (lay == 0):
                x_t = X[t, ...]
            else:
                x_t = H[t + 1, lay - 1, ...]
            h_next, y = rnn_cells[lay].forward(
                h_prev=H[t, lay, ...], x_t=x_t
            )
            H[t + 1, lay, ...] = h_next[None, None, ...]
            if (lay == L - 1):
                Y[t, ...] = y[None, ...]

    return H, Y


# Testing
if __name__ == "__main__":
    # RNNCell = __impo rt__('0-rnn_cell').RNNCell

    np.random.seed(1)
    cell1 = RNNCell(10, 15, 1)
    cell2 = RNNCell(15, 15, 1)
    cell3 = RNNCell(15, 15, 5)
    rnn_cells = [cell1, cell2, cell3]
    for rnn_cell in rnn_cells:
        rnn_cell.bh = np.random.randn(1, 15)
    cell3.by = np.random.randn(1, 5)
    X = np.random.randn(6, 8, 10)
    H_0 = np.zeros((3, 8, 15))
    H, Y = deep_rnn(rnn_cells, X, H_0)
    print(H.shape)
    print(H)
    print(Y.shape)
    print(Y)

# Expected Output
"""
(7, 3, 8, 15)
[[[[ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   ...
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]]

  [[ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   ...
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]]

  [[ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   ...
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]
   [ 0.          0.          0.         ...  0.          0.
     0.        ]]]


 [[[-0.9995066  -0.54475983 -0.99980187 ... -0.9981234   0.8436619
     0.72444756]
   [ 0.99999999 -0.981389   -0.99980572 ...  0.91639809 -0.99997419
     1.        ]
   [ 0.99998533 -0.9999265   0.25964366 ...  0.92895426 -0.99993341
     0.99999774]
   ...
   [-0.13202896  0.70743056  0.99877835 ... -0.99962931 -0.93742909
    -0.99999975]
   [-0.99892926 -0.99875659  0.51799924 ... -0.999991    0.98251099
    -0.7617567 ]
   [ 0.99996636 -0.78308079 -0.99213832 ...  0.8939096  -0.9997359
     0.99999983]]

  [[ 0.95432168 -0.99999693  0.99067589 ...  0.12449146 -0.54594841
     0.97769541]
   [-0.99999733  1.         -0.37985531 ...  0.99903115  0.98917728
     0.94361255]
   [-0.99999361  0.99999979  0.6005159  ...  0.99991691  0.99753402
    -0.64688369]
   ...
   [ 0.94389742 -0.99259951 -0.99563655 ...  0.99976127 -0.99429302
    -0.50273127]
   [-0.80675686 -0.99840854  0.04544025 ...  0.99998729 -0.99988921
    -0.03066394]
   [-0.99922648  0.99970642  0.66961955 ...  0.9999987   0.99934427
     0.98803279]]

  [[-0.01790862 -0.91742849 -0.49836744 ...  0.65140941  0.99898538
    -0.99999742]
   [ 0.01726477  0.99422619 -0.38202468 ... -0.96444387 -0.99999539
     0.9999445 ]
   [-0.94801405  0.9997973   0.87189817 ... -0.99936869 -0.99313746
     0.99991669]
   ...
   [-0.48045517 -0.99999705  0.98285539 ...  0.99998636  0.36662077
    -0.9996178 ]
   [ 0.86541973 -0.99740734  0.00869462 ...  0.99837633  0.42104904
    -0.999988  ]
   [-0.7975579   0.83590346  0.98216799 ... -0.99891708 -0.99987849
     0.99724211]]]


 [[[-0.9980641  -0.41368498  0.99979681 ... -0.97601732 -0.98943579
     0.01803379]
   [ 0.99542971 -0.98870562  0.0501862  ...  0.9983591  -0.99832705
     0.9558064 ]
   [ 0.99999974 -1.         -0.99999999 ...  0.99999994 -1.
     0.99999919]
   ...
   [ 0.82162121  0.97779526 -0.98913796 ... -1.          0.99570053
    -0.99759039]
   [-0.99998443  0.99993828 -0.84660971 ... -0.99999463  0.9991315
    -0.7872139 ]
   [ 0.99999939  0.98426097  0.59933696 ...  1.         -0.99997523
     0.99599714]]

  [[ 0.96529404 -0.99424376  0.68978719 ...  0.77241698  0.99865472
     0.38736345]
   [-0.99953849 -0.53125088 -0.97258524 ...  0.99956284 -0.73658603
    -0.99969397]
   [-0.51656546 -0.83549988  0.75095902 ... -0.99098107  0.9996017
    -0.50298724]
   ...
   [-0.84691802  1.          0.99981552 ... -0.4316967  -0.99957449
     0.99998619]
   [ 0.91631952 -0.99999819  0.99969456 ... -0.99379118 -0.8852611
     0.66191536]
   [-0.99999786  0.92434309 -0.99861329 ...  0.99998503 -0.61995781
    -0.88508823]]

  [[-0.99982964  0.81881383 -0.97618914 ...  0.95614161  0.99628104
    -0.1014528 ]
   [ 0.89150718 -0.99734886 -0.87727288 ... -0.99834955 -0.98845469
    -0.99547425]
   [-0.32504483  0.99330939  0.87112529 ... -0.99999994  0.99969742
    -0.99999996]
   ...
   [-0.99999612 -0.99994595  0.99848629 ...  0.81039528 -0.9999998
     0.9999948 ]
   [ 0.99844807  0.9945203  -0.98580283 ...  0.9999366   0.9630617
    -0.35887103]
   [-0.07238293 -0.99999167  0.94938268 ... -0.99932639 -0.99999995
     0.84954235]]]


 ...


 [[[-0.99947915  0.99964009 -0.99999989 ...  0.80928852 -0.9999999
     1.        ]
   [ 0.35146905 -0.67898844  0.99729436 ...  0.89958205 -0.9796341
    -0.99988224]
   [-0.74773669  0.99953264  0.92361544 ...  0.74530773 -0.97586586
     0.99900479]
   ...
   [ 0.99999999 -0.99666209 -1.         ... -0.73308587 -0.99999805
    -0.95582565]
   [ 0.98408787  0.98885332  0.91696664 ... -0.99980079 -0.27910526
    -0.9988905 ]
   [-0.99996056  0.97220507 -0.99921378 ... -0.99989835 -0.99845093
     0.99985962]]

  [[ 0.99084888 -0.55400049 -0.83961167 ...  0.93861467 -0.99998753
     0.99050013]
   [-0.5744078  -0.05124999 -0.94835549 ...  0.9999925   0.97962119
    -0.99995116]
   [ 0.61382776  0.9998188  -0.98572451 ...  0.99991434  0.99725885
     0.99764282]
   ...
   [ 0.74271542 -0.88068876  0.99962758 ... -0.88361129  0.99953657
     0.99796104]
   [-0.99982974  0.97582372 -0.99999695 ...  0.99997644 -0.99999985
    -0.99969254]
   [ 0.07381289 -0.99998954  0.9998801  ... -0.81864923  0.9963352
    -0.82881229]]

  [[ 0.99947967  0.99979246 -0.99655212 ...  1.         -0.96620493
     0.98755549]
   [-0.9999987  -0.62880616  0.95115354 ... -0.99735771 -0.99672501
    -0.99940199]
   [-0.98975867 -0.99980388  0.99808498 ... -0.79108976 -0.25690653
     0.99988797]
   ...
   [-1.         -0.9999468   0.99972483 ... -0.92032328  0.99974045
    -0.90587025]
   [ 0.94743309  0.61748223  0.89403632 ...  1.          0.37754781
    -0.92911842]
   [-0.99999992 -0.61507067  0.9616648  ...  0.99881216  0.99999413
    -0.96850797]]]


 [[[-0.99991364  0.99999985 -0.9546453  ...  0.99964714 -0.1917912
    -1.        ]
   [ 0.99989593 -0.99999621  0.38287798 ... -0.74229459  0.14365362
     0.99984167]
   [-0.99998645  0.99991399 -0.66339051 ...  0.99999918  0.99336978
     0.99998347]
   ...
   [ 0.99839757 -0.99991505 -0.98869469 ... -0.99995637 -0.42915296
    -0.92615644]
   [ 0.98617859  0.48416676 -1.         ... -1.         -0.99863239
     0.988555  ]
   [-0.89345728  0.48099174  0.99782737 ... -0.99536045  0.11400054
    -0.99999979]]

  [[-0.99999997  0.31876894  0.50029633 ...  0.99990579  0.96782021
    -0.90112304]
   [-0.31312334  0.99348419  0.77774606 ... -0.34437506  0.99884576
     0.68293999]
   [-0.99999147  0.99999981  0.96770456 ...  0.5650538  -0.99997836
     0.2131233 ]
   ...
   [-0.16898429  1.          0.93916912 ...  0.99999523  0.97369236
     0.99998923]
   [ 0.99863461 -0.99999593  0.99999952 ... -0.95498653  0.95497356
    -0.27796486]
   [ 0.99809363 -0.99462475  0.99290581 ...  0.98199042  0.74182286
     0.59971857]]

  [[-0.99443384  0.5976361  -0.89942179 ...  0.99997448  0.89817197
     0.99999641]
   [-1.         -0.91400493  0.99916708 ... -0.99997062  0.99998214
    -0.89376666]
   [-0.99999999 -0.39356492  0.50677015 ... -0.99999948 -1.
     0.99994265]
   ...
   [-0.99999994 -0.99999953  0.99520627 ... -0.99724342  0.96766492
    -0.61424802]
   [-0.98405844  0.99999944  0.99999987 ... -0.99997939  0.99999969
    -0.99800471]
   [ 0.90736813  0.99999977  0.99369399 ... -0.97398777  0.9999629
    -0.99990044]]]


 [[[-0.88141214 -0.3139027  -0.99999652 ...  0.99338642 -0.99993082
     1.        ]
   [ 0.99999833 -0.99975069  0.67456278 ... -0.81140781 -0.84895359
     0.99999924]
   [-0.97152209  0.05164318 -0.99999972 ...  0.72831401 -0.99997349
     0.99998064]
   ...
   [ 0.99999962 -0.3505002  -0.99702213 ... -0.41569566 -0.9999962
     0.93397099]
   [ 0.9999997  -0.95010731 -0.99997064 ...  0.99441418 -0.99995136
    -0.99848166]
   [ 0.81429807 -0.53926518 -0.99564009 ...  0.62563752 -0.99999052
     0.99997212]]

  [[ 0.71500803  0.9880445   0.99975666 ...  1.         -0.9689944
     1.        ]
   [-0.78893596  0.91633994 -0.99999525 ...  0.99999837  0.91126078
    -0.9999805 ]
   [ 0.56951589 -0.99831252  0.99405195 ...  0.99999994  0.48523026
     0.99993994]
   ...
   [-0.99612319  1.          0.99664299 ...  0.99999999 -0.99986847
     0.99987922]
   [-0.99999158  1.         -0.99745491 ...  0.99997969  0.98921241
     1.        ]
   [-0.99916811  1.         -0.98035792 ...  0.99999953 -0.4311449
     0.99999899]]

  [[-0.99999517 -0.06434706 -0.98861765 ...  0.99973411 -0.9996765
     0.93948961]
   [-0.99999994 -0.63178676  0.99004786 ... -0.95461565  0.99999963
    -0.99999351]
   [-0.98655939 -0.80889697 -0.94872434 ... -0.99081785  0.99996397
    -0.99999998]
   ...
   [-0.9999721  -0.99999997  0.99923268 ... -0.992973   -0.99999995
     0.99998527]
   [-1.         -0.99999999  0.97570606 ... -0.99992896 -0.9999989
    -0.96654555]
   [ 0.99983539  0.69574645  0.37564131 ... -0.99562052 -0.99467679
     0.61155406]]]]
(6, 8, 5)
[[[1.44224035e-01 1.60584387e-02 7.53392071e-02 1.99851645e-01
   5.64526674e-01]
  [5.55726290e-05 6.43089167e-01 3.28344603e-01 1.90653184e-02
   9.44533871e-03]
  [1.25002665e-03 9.93892949e-01 1.12622750e-03 3.71967162e-03
   1.11255123e-05]
  [4.87917500e-04 6.17425597e-02 3.82417096e-05 9.35367574e-01
   2.36370688e-03]
  [4.21726508e-03 1.11212106e-02 5.58725718e-03 9.68424590e-01
   1.06496774e-02]
  [7.44703078e-01 8.45069632e-03 9.10173656e-05 2.39154036e-01
   7.60117156e-03]
  [3.17618228e-01 1.64024221e-02 2.39586075e-02 4.90232880e-01
   1.51787863e-01]
  [5.23193405e-06 1.86666608e-02 3.99251675e-02 9.40384325e-01
   1.01861512e-03]]

 [[8.23397297e-03 7.66007256e-01 1.68248943e-01 4.94358181e-02
   8.07400991e-03]
  [5.00645724e-01 6.85585901e-03 4.83571891e-04 4.80671334e-01
   1.13435110e-02]
  [2.52885629e-01 2.65673990e-01 1.52074608e-02 5.57075428e-02
   4.10525377e-01]
  [2.06162604e-01 9.36788109e-03 2.03522050e-05 7.49240925e-01
   3.52082383e-02]
  [5.70856001e-03 7.19392180e-01 8.56387567e-03 1.79036851e-01
   8.72985338e-02]
  [1.47169411e-02 1.43734283e-01 2.28062662e-02 4.72029820e-01
   3.46712690e-01]
  [1.70952920e-02 6.01970503e-01 2.97139537e-01 3.54368346e-02
   4.83578339e-02]
  [3.67157767e-01 3.34885437e-01 3.52841947e-03 1.84274995e-01
   1.10153381e-01]]

 [[1.56761929e-04 9.65053974e-01 3.71627714e-03 3.02279852e-02
   8.45002073e-04]
  [5.45524307e-02 8.74861986e-01 1.75537334e-03 5.95751560e-02
   9.25505410e-03]
  [1.82284243e-02 1.24631450e-03 9.05160185e-01 1.82866359e-02
   5.70784399e-02]
  [2.71147926e-03 2.57719958e-04 2.89961108e-07 9.96795495e-01
   2.35015476e-04]
  [6.71623717e-03 7.88536463e-02 2.53008069e-03 9.11793570e-01
   1.06466113e-04]
  [3.61611796e-01 6.10827843e-01 6.90427090e-05 2.69738720e-02
   5.17445685e-04]
  [1.78487919e-03 8.12991113e-01 8.95970942e-05 1.85120058e-01
   1.43528633e-05]
  [7.81899275e-02 1.34165235e-04 4.84791223e-03 6.38803398e-02
   8.52947655e-01]]

 [[6.29904417e-05 1.52242728e-01 4.39240298e-03 8.26264622e-01
   1.70372564e-02]
  [5.96539188e-01 2.67669607e-01 8.28943949e-04 1.33117205e-01
   1.84505622e-03]
  [1.64133875e-03 1.35279798e-02 8.37939894e-03 9.74943021e-01
   1.50826142e-03]
  [3.23306537e-04 6.93765577e-02 7.59620514e-07 9.30175022e-01
   1.24354253e-04]
  [3.56940555e-05 1.94948441e-01 8.55324064e-06 8.04805574e-01
   2.01737882e-04]
  [3.04287633e-02 6.50353258e-04 4.73232007e-01 1.99509604e-04
   4.95489367e-01]
  [8.60734109e-01 8.10012506e-02 3.40300230e-03 5.35428974e-02
   1.31874077e-03]
  [7.54722426e-01 1.24458155e-01 1.71752725e-02 1.03551282e-01
   9.28649220e-05]]

 [[7.38951371e-02 2.10394731e-01 1.32196199e-05 7.15471158e-01
   2.25754166e-04]
  [9.88219162e-01 2.06028125e-03 5.99654356e-03 2.05742892e-05
   3.70343853e-03]
  [1.02535492e-01 7.30487648e-01 6.36970136e-04 1.56083023e-01
   1.02568676e-02]
  [9.14812753e-01 1.09434425e-02 1.33472012e-04 4.79847388e-02
   2.61255933e-02]
  [8.53381671e-01 5.72440883e-03 2.51849214e-05 1.40834019e-01
   3.47165953e-05]
  [4.32173689e-01 2.60148760e-02 3.81231875e-02 4.94234591e-01
   9.45365633e-03]
  [6.11621828e-03 8.08390603e-02 7.79617761e-01 1.31102562e-03
   1.32115935e-01]
  [9.27078547e-04 2.59002034e-01 7.39558362e-01 6.36208134e-05
   4.48905141e-04]]

 [[1.12431365e-05 1.49294960e-02 6.14190990e-05 9.84813206e-01
   1.84636133e-04]
  [9.81761316e-01 1.39017705e-02 2.66805604e-03 8.89195759e-05
   1.57993808e-03]
  [6.58151566e-01 6.66213592e-04 3.55818819e-04 2.15802951e-01
   1.25023451e-01]
  [5.09946369e-01 3.58878541e-01 1.76952045e-02 1.05018437e-01
   8.46144909e-03]
  [2.77706985e-03 7.21947913e-01 2.26782323e-01 2.19707152e-02
   2.65219789e-02]
  [1.36993270e-02 2.13529376e-02 9.86700560e-05 9.64384999e-01
   4.64065992e-04]
  [8.79740324e-01 3.14884674e-02 3.24428584e-02 4.53485692e-02
   1.09797815e-02]
  [1.00292729e-02 9.31818286e-01 2.50132538e-02 5.88649467e-04
   3.25505382e-02]]]
"""
