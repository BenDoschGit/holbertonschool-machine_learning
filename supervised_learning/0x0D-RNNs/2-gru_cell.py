#!/usr/bin/env python3
"""Module containing the class GRUCell that represents a gated recurrent
unit."""

import numpy as np


class GRUCell():
    """Class that represents a gated recurrent unit.
    """

    def __init__(self, i, h, o):
        """Class constructor that creates the public instance attributes
        Wz, Wr, Wh, Wy, bz, br, bh, by that represent the weights and biases of
        the cell. Wz and bz are for the update gate. Wr and br are for the
        reset gate. Wh and bh are for the intermediate hidden state. Wy and by
        are for the output. The weights are initialized using a random normal
        distribution in the order listed previously. The weights will be used
        on the right side for matrix multiplication. The biases are initialized
        as zeros.

        Args:
            i (int): The dimensionality of the data.
            h (int): The dimensionality of the hidden state.
            o (int): The dimensionality of the outputs.
        """
        pass

    def forward(self, h_prev, x_t):
        """Public instance method that performs forward propagation for one
        time step.

        Args:
            h_prev (numpy.ndarray): A tensor of shape (m, h) containing the
                previous hidden state, where m is the batche size for the data
                and i is the dimensionality of the data.
            x_t (numpy.ndarray): A tensor of shape (m, i) that contains the
                data input for the cell, where m is the batche size for the
                data and i is the dimensionality of the data.


        Returns:
            h_next (numpy.ndarray): A tensor of shape ( , ) containing the
                next hidden state.
            y (numpy.ndarray): A tensor of shape ( , ) containing the output
                of the cell.
        """
        pass


# Testing
if __name__ == "__main__":
    np.random.seed(2)
    gru_cell = GRUCell(10, 15, 5)
    print("Wz:", gru_cell.Wz)
    print("Wr:", gru_cell.Wr)
    print("Wh:", gru_cell.Wh)
    print("Wy:", gru_cell.Wy)
    print("bz:", gru_cell.bz)
    print("br:", gru_cell.br)
    print("bh:", gru_cell.bh)
    print("by:", gru_cell.by)
    gru_cell.bz = np.random.randn(1, 15)
    gru_cell.br = np.random.randn(1, 15)
    gru_cell.bh = np.random.randn(1, 15)
    gru_cell.by = np.random.randn(1, 5)
    h_prev = np.random.randn(8, 15)
    x_t = np.random.randn(8, 10)
    h, y = gru_cell.forward(h_prev, x_t)
    print(h.shape)
    print(h)
    print(y.shape)
    print(y)

# Expected Output
"""
Wz: [[-4.16757847e-01 -5.62668272e-02 -2.13619610e+00  1.64027081e+00
  -1.79343559e+00 -8.41747366e-01  5.02881417e-01 -1.24528809e+00
  -1.05795222e+00 -9.09007615e-01  5.51454045e-01  2.29220801e+00
   4.15393930e-02 -1.11792545e+00  5.39058321e-01]
 [-5.96159700e-01 -1.91304965e-02  1.17500122e+00 -7.47870949e-01
   9.02525097e-03 -8.78107893e-01 -1.56434170e-01  2.56570452e-01
  -9.88779049e-01 -3.38821966e-01 -2.36184031e-01 -6.37655012e-01
  -1.18761229e+00 -1.42121723e+00 -1.53495196e-01]
 [-2.69056960e-01  2.23136679e+00 -2.43476758e+00  1.12726505e-01
   3.70444537e-01  1.35963386e+00  5.01857207e-01 -8.44213704e-01
   9.76147160e-06  5.42352572e-01 -3.13508197e-01  7.71011738e-01
  -1.86809065e+00  1.73118467e+00  1.46767801e+00]
 [-3.35677339e-01  6.11340780e-01  4.79705919e-02 -8.29135289e-01
   8.77102184e-02  1.00036589e+00 -3.81092518e-01 -3.75669423e-01
  -7.44707629e-02  4.33496330e-01  1.27837923e+00 -6.34679305e-01
   5.08396243e-01  2.16116006e-01 -1.85861239e+00]
 [-4.19316482e-01 -1.32328898e-01 -3.95702397e-02  3.26003433e-01
  -2.04032305e+00  4.62555231e-02 -6.77675577e-01 -1.43943903e+00
   5.24296430e-01  7.35279576e-01 -6.53250268e-01  8.42456282e-01
  -3.81516482e-01  6.64890091e-02 -1.09873895e+00]
 [ 1.58448706e+00 -2.65944946e+00 -9.14526229e-02  6.95119605e-01
  -2.03346655e+00 -1.89469265e-01 -7.72186654e-02  8.24703005e-01
   1.24821292e+00 -4.03892269e-01 -1.38451867e+00  1.36723542e+00
   1.21788563e+00 -4.62005348e-01  3.50888494e-01]
 [ 3.81866234e-01  5.66275441e-01  2.04207979e-01  1.40669624e+00
  -1.73795950e+00  1.04082395e+00  3.80471970e-01 -2.17135269e-01
   1.17353150e+00 -2.34360319e+00  1.16152149e+00  3.86078048e-01
  -1.13313327e+00  4.33092555e-01 -3.04086439e-01]
 [ 2.58529487e+00  1.83533272e+00  4.40689872e-01 -7.19253841e-01
  -5.83414595e-01 -3.25049628e-01 -5.60234506e-01 -9.02246068e-01
  -5.90972275e-01 -2.76179492e-01 -5.16883894e-01 -6.98589950e-01
  -9.28891925e-01  2.55043824e+00 -1.47317325e+00]
 [-1.02141473e+00  4.32395701e-01 -3.23580070e-01  4.23824708e-01
   7.99179995e-01  1.26261366e+00  7.51964849e-01 -9.93760983e-01
   1.10914328e+00 -1.76491773e+00 -1.14421297e-01 -4.98174194e-01
  -1.06079904e+00  5.91666521e-01 -1.83256574e-01]
 [ 1.01985473e+00 -1.48246548e+00  8.46311892e-01  4.97940148e-01
   1.26504175e-01 -1.41881055e+00 -2.51774118e-01 -1.54667461e+00
  -2.08265194e+00  3.27974540e+00  9.70861320e-01  1.79259285e+00
  -4.29013319e-01  6.96197980e-01  6.97416272e-01]
 [ 6.01515814e-01  3.65949071e-03 -2.28247558e-01 -2.06961226e+00
   6.10144086e-01  4.23496900e-01  1.11788673e+00 -2.74242089e-01
   1.74181219e+00 -4.47500876e-01 -1.25542722e+00  9.38163671e-01
  -4.68346260e-01 -1.25472031e+00  1.24823646e-01]
 [ 7.56502143e-01  2.41439629e-01  4.97425649e-01  4.10869262e+00
   8.21120877e-01  1.53176032e+00 -1.98584577e+00  3.65053516e-01
   7.74082033e-01 -3.64479092e-01 -8.75979478e-01  3.96520159e-01
  -3.14617436e-01 -5.93755583e-01  1.14950057e+00]
 [ 1.33556617e+00  3.02629336e-01 -4.54227855e-01  5.14370717e-01
   8.29458431e-01  6.30621967e-01 -1.45336435e+00 -3.38017777e-01
   3.59133332e-01  6.22220414e-01  9.60781945e-01  7.58370347e-01
  -1.13431848e+00 -7.07420888e-01 -1.22142917e+00]
 [ 1.80447664e+00  1.80409807e-01  5.53164274e-01  1.03302907e+00
  -3.29002435e-01 -1.15100294e+00 -4.26522471e-01 -1.48147191e-01
   1.50143692e+00  8.69598198e-01 -1.08709057e+00  6.64221413e-01
   7.34884668e-01 -1.06136574e+00 -1.08516824e-01]
 [-1.85040397e+00  3.30488064e-01 -3.15693210e-01 -1.35000210e+00
  -6.98170998e-01  2.39951198e-01 -5.52949440e-01  2.99526813e-01
   5.52663696e-01 -8.40443012e-01 -3.12270670e-01  2.14467809e+00
   1.21105582e-01 -8.46828752e-01  6.04624490e-02]
 [-1.33858888e+00  1.13274608e+00  3.70304843e-01  1.08580640e+00
   9.02179395e-01  3.90296450e-01  9.75509412e-01  1.91573647e-01
  -6.62209012e-01 -1.02351498e+00 -4.48174823e-01 -2.50545813e+00
   1.82599446e+00 -1.71406741e+00 -7.66395640e-02]
 [-1.31756727e+00 -2.02559359e+00 -8.22453750e-02 -3.04666585e-01
  -1.59724130e-01  5.48946560e-01 -6.18375485e-01  3.78794466e-01
   5.13251444e-01 -3.34844125e-01 -2.83519516e-01  5.38424263e-01
   5.72509465e-02  1.59088487e-01 -2.37440268e+00]
 [ 5.85199353e-02  3.76545911e-01 -1.35479764e-01  3.35908395e-01
   1.90437591e+00  8.53644334e-02  6.65334278e-01 -8.49995503e-01
  -8.52341797e-01 -4.79985112e-01 -1.01964910e+00 -7.60113841e-03
  -9.33830661e-01 -1.74996844e-01 -1.43714343e+00]
 [-1.65220029e+00 -6.75661789e-01 -1.06706712e+00 -6.52931145e-01
  -6.12094750e-01 -3.51262461e-01  1.04547799e+00  1.36901602e+00
   7.25353259e-01 -3.59474459e-01  1.49695179e+00 -1.53111111e+00
  -2.02336394e+00  2.67972576e-01 -2.20644541e-03]
 [-1.39291883e-01  3.25654693e-02 -1.64056022e+00 -1.15669917e+00
   1.23403468e+00  1.02818490e+00 -7.21879726e-01  1.93315697e+00
  -1.07079633e+00 -5.71381608e-01  2.92432067e-01 -1.19499989e+00
  -4.87930544e-01 -1.73071165e-01 -3.95346401e-01]
 [ 8.70840765e-01  5.92806797e-01 -1.09929731e+00 -6.81530644e-01
   1.80066685e-01 -6.69310440e-02 -7.87749540e-01  4.24753672e-01
   8.19885117e-01 -6.31118683e-01  7.89059649e-01 -1.62167380e+00
  -1.61049926e+00  4.99939764e-01 -8.34515207e-01]
 [-9.96959687e-01 -2.63388077e-01 -6.77360492e-01  3.27067038e-01
  -1.45535944e+00 -3.71519124e-01  3.16096597e+00  1.09951013e-01
  -1.91352322e+00  5.99820429e-01  5.49384465e-01  1.38378103e+00
   1.48349243e-01 -6.53541444e-01  1.40883398e+00]
 [ 7.12061227e-01 -1.80071604e+00  7.47598942e-01 -2.32897001e-01
   1.11064528e+00 -3.73338813e-01  7.86146070e-01  1.94168696e-01
   5.86204098e-01 -2.03872918e-02 -4.14408598e-01  6.73134124e-02
   6.31798924e-01  4.17592731e-01  1.61517627e+00]
 [ 4.25606211e-01  6.35363758e-01  2.10222927e+00  6.61264168e-02
   5.35558351e-01 -6.03140792e-01  4.19576292e-02  1.64191464e+00
   3.11697707e-01  1.45116990e+00 -1.06492788e+00 -1.40084545e+00
   3.07525527e-01 -1.36963867e+00  2.67033724e+00]
 [ 1.24845030e+00 -1.24572655e+00 -1.67168774e-01 -5.76610930e-01
   4.16021749e-01 -5.78472626e-02  9.31887358e-01  1.46833213e+00
  -2.21320943e-01 -1.17315562e+00  5.62669078e-01 -1.64515057e-01
   1.14485538e+00 -1.52117687e-01  8.29789046e-01]]
Wr: [[ 3.36065952e-01 -1.89044051e-01 -4.49328601e-01  7.13524448e-01
   2.52973487e+00  8.37615794e-01 -1.31682403e-01  7.07592866e-01
   1.14053878e-01 -1.28089518e+00  3.09846277e-01  1.54829069e+00
  -3.15828043e-01 -1.12590378e+00  4.88496666e-01]
 [ 1.83094666e+00  9.40175993e-01  1.01871705e+00  2.30237829e+00
   1.62109298e+00  7.12683273e-01 -2.08703629e-01  1.37617991e-01
  -1.03352168e-01  8.48350567e-01 -8.83125561e-01  1.54538683e+00
   1.45840073e-01 -4.00106056e-01  8.15206041e-01]
 [-2.07492237e+00 -8.34437391e-01 -6.57718447e-01  8.20564332e-01
  -4.89157001e-01  1.42496703e+00 -4.46857897e-01  5.21109431e-01
  -7.08194380e-01  1.15553059e+00 -2.54530459e-01  5.18924924e-01
  -4.92994911e-01 -1.08654815e+00 -2.30917497e-01]
 [ 1.09801004e+00 -1.01787805e+00 -1.52939136e+00 -3.07987737e-01
   7.80754356e-01 -1.05583964e+00 -5.43883381e-01  1.84301739e-01
  -3.30675843e-01  2.87208202e-01  1.18952814e+00  2.12015479e-02
  -6.54096803e-02  7.66115904e-01 -6.16350846e-02]
 [-9.52897152e-01 -1.01446306e+00 -1.11526396e+00  1.91260068e+00
  -4.52632031e-02  5.76909718e-01  7.17805695e-01 -9.38998998e-01
   6.28775807e-01 -5.64493432e-01 -2.08780746e+00 -2.15050132e-01
  -1.07502856e+00 -3.37972149e-01  3.43212732e-01]
 [ 2.28253964e+00 -4.95778848e-01 -1.63962832e-01  3.71622161e-01
   1.86521520e-01 -1.58429224e-01 -1.08292956e+00 -9.56625520e-01
  -1.83376735e-01 -1.15980690e+00 -6.57768362e-01 -1.25144841e+00
   1.12448286e+00 -1.49783981e+00  1.90201722e+00]
 [-5.80383038e-01 -1.05491567e+00 -1.18275720e+00  7.79480054e-01
   1.02659795e+00 -8.48666001e-01  3.31539648e-01 -1.49591353e-01
  -2.42440600e-01  1.51197175e-01  7.65069481e-01 -1.91663052e+00
  -2.22734129e+00  2.06689897e-01 -7.08763560e-02]
 [ 6.84759969e-01 -1.70753905e+00 -9.86569665e-01  1.54353634e+00
  -1.31027053e+00  3.63433972e-01 -7.94872445e-01 -4.05286267e-01
  -1.37775793e+00  1.18604868e+00 -1.90382114e+00 -1.19814038e+00
  -9.10065643e-01  1.17645419e+00  2.99210670e-01]
 [ 6.79267178e-01 -1.76606800e-02  2.36040923e-01  4.94035871e-01
   1.54627765e+00  2.46857508e-01 -1.46877580e+00  1.14709994e+00
   9.55569845e-02 -1.10743873e+00 -1.76286141e-01 -9.82755667e-01
   2.08668273e+00 -3.44623671e-01 -2.00207923e+00]
 [ 3.03234433e-01 -8.29874845e-01  1.28876941e+00  1.34925462e-01
  -1.77860064e+00 -5.00791490e-01 -1.08816157e+00 -7.57855553e-01
  -6.43744900e-01 -2.00878453e+00  1.96262894e-01 -8.75896370e-01
  -8.93609209e-01  7.51902355e-01  1.89693224e+00]
 [-6.29079151e-01  1.81208553e+00 -2.05626574e+00  5.62704887e-01
  -5.82070757e-01 -7.40029749e-02 -9.86496364e-01 -5.94722499e-01
  -3.14811843e-01 -3.46940532e-01  4.11443516e-01  2.32639090e+00
  -6.34053128e-01 -1.54409962e-01 -1.74928880e+00]
 [-2.51957930e+00  1.39116243e+00 -1.32934644e+00 -7.45596414e-01
   2.12608498e-02  9.10917515e-01  3.15276082e-01  1.86620821e+00
  -1.82497623e-01 -1.82826634e+00  1.38955717e-01  1.19450165e-01
  -8.18899200e-01 -3.32639265e-01 -5.86387955e-01]
 [ 1.73451634e+00 -6.12751558e-01 -1.39344202e+00  2.79433757e-01
  -1.82223127e+00  4.27017458e-01  4.06987749e-01 -8.44308241e-01
  -5.59820113e-01 -6.00520405e-01  1.61487324e+00  3.94953220e-01
  -1.20381347e+00 -1.24747243e+00 -7.75462496e-02]
 [-1.33397514e-02 -7.68323250e-01  2.91234010e-01 -1.97330948e-01
   1.07682965e+00  4.37410232e-01 -9.31978663e-02  1.35631416e-01
  -8.82708822e-01  8.84744194e-01  3.83204463e-01 -4.16994149e-01
   1.17796550e-01 -5.36685309e-01  2.48718458e+00]
 [-4.51361054e-01  5.18836127e-01  3.64448005e-01 -7.98348729e-01
   5.65779713e-03 -3.20934708e-01  2.49513550e-01  2.56308392e-01
   7.67625083e-01  7.83020087e-01 -4.07063047e-01 -5.24891667e-01
  -5.89808683e-01 -8.62531086e-01 -1.74287290e+00]
 [ 6.03671461e-01 -7.96134520e-02 -2.11272691e-01 -1.65773474e+00
  -1.50104009e+00 -2.51543946e+00 -1.02961031e-01  6.69229029e-01
   5.94309157e-01 -7.81073374e-02 -1.07873949e+00 -8.98162946e-03
   2.35933432e-03  7.05752538e-01  7.65867459e-01]
 [-2.66236738e-01 -3.46853660e-02  6.96193752e-01  4.57188521e-01
  -1.70701551e-01 -2.16861850e+00 -6.65180166e-01  8.38712986e-01
   1.49827950e-01  9.53177400e-01 -3.45241965e-01  8.02706183e-02
   7.93524596e-01  6.87824159e-01  3.91682864e-01]
 [ 1.08885847e+00  1.33531175e+00  1.39034601e+00 -1.65167960e+00
  -4.86318581e-01 -3.28568470e-01 -3.64615003e-01 -1.63761438e+00
   1.30112042e+00 -1.00130515e+00  9.94992653e-02 -2.40422605e+00
  -5.07073802e-01 -2.58049426e-01 -9.35868914e-01]
 [ 7.35410461e-01  2.38048446e+00 -8.75581330e-01 -8.65209964e-01
   1.75181816e+00  5.62041138e-01 -3.16094028e-01 -1.27955688e+00
   7.32650013e-01  2.13158678e-01  1.55251343e+00 -8.70952113e-01
  -1.73561386e-01 -3.07935389e-01 -2.16831265e-01]
 [ 1.05763457e+00  8.42369345e-01 -6.40418910e-01 -9.23232894e-02
  -2.30813008e-01  8.89122318e-01 -1.76246067e-01 -1.11796185e+00
  -3.45308255e-01 -4.77771387e-02  9.17220478e-01  1.27582690e+00
   1.29076796e+00  3.64108618e-01 -5.17934324e-01]
 [ 5.81286240e-01 -1.90924565e-01 -6.25253518e-01  2.89252536e-01
   4.00297487e-01  8.63532101e-01 -9.04881880e-01 -1.67363599e+00
   4.99184358e-01 -9.71332206e-01  9.90152682e-01 -1.10835167e+00
  -5.90090600e-01 -1.81825246e+00  2.03664994e+00]
 [-4.70806767e-01 -9.59694707e-02 -5.40146013e-01 -2.54511211e-01
   8.13676395e-01  8.81310573e-02 -2.89358456e-02  1.17268256e+00
  -1.37042398e+00  1.11352979e+00  1.57689018e+00 -1.40669958e+00
   2.52945926e-01 -1.30543343e+00 -2.12986920e+00]
 [-8.67125505e-01  5.05364896e-01  7.38651836e-01 -3.86625781e-01
  -8.84577703e-01 -4.57308828e-01 -7.35640523e-01 -6.49205160e-01
  -2.42825346e+00 -2.57124969e-01 -1.36978296e-01  2.16246241e+00
   6.57551247e-01 -1.60262559e-01  5.30264828e-02]
 [ 3.08356262e-01 -7.22288055e-01 -2.10355834e+00 -7.51374842e-01
  -2.48143335e-01  9.35717871e-02 -7.39607076e-01 -9.45751712e-01
  -2.87703710e-01  3.00600559e-02  5.47261804e-01 -2.66317868e-01
   4.14103748e-01 -1.02298822e+00  7.89522560e-01]
 [-8.07479574e-02 -1.38716941e+00 -2.76666363e-01  8.28224803e-02
  -1.08739480e+00  7.02013525e-01 -3.56135931e-01  4.31988981e-01
  -1.01786273e+00  2.87747172e-01  7.04450885e-01 -4.62865876e-01
  -2.14452750e-01 -5.92966711e-01  3.11603984e-01]]
Wh: [[ 1.00343703e-02  4.78804609e-01 -8.03055920e-02 -1.29222381e+00
  -1.33340399e+00 -4.69840677e-01  4.40206796e-01  2.24266347e+00
   8.48821449e-01 -6.33261191e-01 -2.04586668e+00  4.94493866e-01
  -1.95291246e-03 -1.23166449e+00  8.75688930e-01]
 [-1.07756418e-02 -4.30335554e-01 -1.95027706e+00  9.49121728e-01
   5.09069885e-02 -2.66021064e-01 -9.78930651e-01 -3.83809846e-01
   1.22185026e+00  5.07226604e-01  1.98983529e+00  1.04838866e+00
   3.32762523e-01  8.84358999e-01  1.48886189e-01]
 [-1.46267835e+00 -6.16844470e-01  3.21335796e-01 -9.46446864e-01
  -5.30139408e-01 -1.25920702e+00  1.67754406e+00 -1.33116173e+00
  -1.05287411e+00 -8.98985491e-01  9.61104313e-01  1.11651599e+00
  -5.65119384e-01  5.65121735e-01 -9.03360910e-01]
 [-7.64231104e-03  2.60369967e+00  9.35916150e-01 -5.08666726e-02
  -1.33441228e+00 -3.08002732e-01 -1.32891514e+00 -2.19296670e+00
   5.99465615e-01  5.76275114e-01  1.93928425e-01  9.93505594e-01
  -1.67756538e+00  1.39213012e+00 -1.08875168e+00]
 [ 3.74289725e-01  4.51433955e-01  1.07436141e+00  1.99611078e+00
   3.45449370e-01 -3.82803100e-01 -1.11330131e+00  2.58003025e-01
  -8.48414457e-01 -1.35845405e+00 -2.02840738e-01  6.71146763e-01
  -3.09983175e-01 -1.05333201e+00  1.41641453e-01]
 [-1.24410394e+00 -1.51837263e+00  1.45897097e+00  2.42874291e-01
   1.98021995e+00 -1.47462796e+00  1.03691782e+00 -1.76855889e-01
   2.67964423e+00 -2.15424151e-01 -4.44454771e-01  4.23820961e-01
   1.88960995e-01 -4.59134928e-01  9.11747865e-01]
 [ 6.90180924e-01  8.85691503e-01  4.00418848e-01 -7.09654189e-01
  -7.00278087e-01  5.92992793e-01 -9.39057367e-01  1.69804451e+00
   3.24947182e-02 -7.94177964e-01  1.03756491e+00 -2.01933386e-02
   1.19717984e+00  2.11787178e-01  1.76829743e+00]
 [-3.83485183e-01 -2.18417756e+00 -1.51620476e+00 -1.63388363e+00
   5.89894304e-01  1.80914499e+00 -1.95037909e-01 -1.33435858e+00
   6.82921371e-01  4.53701773e-01 -3.81164620e-01  4.07948363e-01
   6.41020641e-03 -1.15021767e+00  6.85617746e-01]
 [-5.04768374e-01 -9.49688881e-01 -2.36323391e-01  1.56800500e+00
   1.96236965e+00  1.40013683e+00 -4.95002423e-01 -1.02716908e+00
   3.43942724e-01 -1.62003355e-01  1.39032527e-01 -1.13040409e+00
  -8.86219125e-01 -1.07589227e+00  7.72703740e-01]
 [ 1.06231931e+00 -6.82623601e-01  5.82613831e-01  6.41540019e-01
  -7.39931870e-01  9.87606898e-03  8.13433674e-01 -1.01466268e+00
   1.24628173e+00 -2.06170252e-01  5.93675946e-02 -2.44349110e-01
  -1.48177155e+00  3.39037480e-01 -6.82749416e-03]
 [-4.10136742e-01 -2.19942167e-01  4.17309223e-01 -1.47417084e-01
  -5.30242753e-01  8.04303988e-02  7.54160973e-01  3.59252825e-02
  -7.96181395e-01  8.30878534e-01 -2.96408571e-01  5.85360099e-01
  -1.45964411e-01 -9.44298276e-01 -1.27511255e+00]
 [-9.00500314e-01 -2.34140999e-01 -2.25268528e+00  3.83008580e-01
   1.09960863e+00 -2.42162016e-01 -1.10950800e+00 -1.66697713e+00
   2.25317802e-01  4.11975689e-01  5.75856506e-02  6.96361151e-01
  -6.72420421e-01 -2.52545882e-01  2.75751090e-01]
 [-2.26031563e-01  4.87200240e-01  4.95588395e-01 -2.71821126e-01
  -9.63965213e-01 -7.24377409e-01  1.09554226e+00 -1.20416797e+00
   5.97309533e-02 -9.96325155e-01  2.30711528e+00 -6.34541150e-01
   6.33710809e-01 -9.68499759e-01  3.19190125e+00]
 [-1.33622687e+00  3.56435819e-01 -1.25306470e+00  8.19206834e-01
  -1.25581222e+00 -4.43511462e-01 -1.59513440e+00 -3.97705756e-01
   6.28684111e-04  1.74122456e+00 -2.30303282e+00  5.44911801e-01
   4.19309510e-02 -6.08914196e-01 -2.12194138e-01]
 [ 3.90698517e-01 -3.75202983e-02 -4.40514277e-02 -7.80616391e-01
  -4.01026894e-01  4.83982464e-01 -9.22443629e-01 -5.18974685e-01
   7.34282816e-02  3.25968553e-01  3.85998076e-01 -2.01988744e-01
  -2.03445123e+00  7.61485079e-01  1.00147133e+00]
 [ 1.19451016e+00  3.39459772e-01  8.43393007e-01 -2.97174784e-01
  -1.11431147e+00 -1.75330779e-01 -2.49692591e-01  9.91660289e-01
   7.92990718e-01 -5.22655090e-01 -4.29012263e-01 -5.28647394e-02
   6.29926754e-02  1.40452975e+00 -5.01512485e-01]
 [ 1.27224463e+00 -1.40185313e+00 -6.93225598e-01  1.64787517e+00
   3.73226981e-01  8.19317930e-02  5.68725594e-01 -2.34482668e-01
   3.51102376e-02  1.96785270e-01  1.97749914e-01  3.36836136e-01
  -5.97657259e-01  3.37936610e-01 -7.30028118e-01]
 [ 5.60022058e-01 -1.88145390e-01  2.25961077e-01  2.55541968e-01
  -7.58511523e-01 -5.53796527e-01 -1.64129023e-01  4.24801043e-01
   9.13505484e-01 -7.42410515e-02 -6.98822452e-01  2.18195773e-01
  -4.19304280e-02  7.29059047e-01  1.17859548e+00]
 [ 1.91567888e+00 -1.66040484e+00 -4.92985257e-01 -9.60824565e-02
   7.53657929e-01  6.49636178e-01  3.59341800e-02  7.41614047e-01
  -5.68695137e-01 -3.84533335e-01  2.77721817e-01 -1.08067527e+00
   1.53873599e+00 -8.07964987e-01 -1.14380083e+00]
 [ 2.96695136e-01 -1.92074773e+00 -4.47283718e-01 -1.85306211e-01
   1.25356725e+00  3.00943119e+00  1.51647092e-01 -1.29823835e+00
   2.41037207e-01  6.42954244e-01 -9.31713747e-01  3.26330750e-01
   1.55233462e+00  4.71299893e-01 -7.94150057e-01]
 [-5.68612003e-01 -1.64354281e+00 -4.46904271e-01 -5.90224602e-01
   1.36382529e+00 -1.55275783e+00 -1.58006952e+00  1.74283681e-01
   5.71033519e-01 -5.60998601e-01  1.75140722e-01  6.46350324e-01
   7.16881429e-01  3.48280608e-01  5.20956268e-01]
 [-1.55146025e+00  7.78365878e-01  1.22683306e-01 -8.36932455e-01
  -4.07456423e-01 -3.06069120e-01 -5.59133187e-01 -1.79736596e-01
  -4.03748423e-01 -1.46015397e+00  2.12078282e+00  3.61506517e-01
   2.18173119e+00 -2.92709378e-01  1.58493598e+00]
 [-1.46943188e-01  1.53941339e+00  8.99889094e-01  7.40251684e-01
  -1.93203970e-01  2.01997788e-01  1.31130608e+00 -2.00007670e+00
  -6.98164583e-01 -1.25657282e+00 -9.26607996e-01  6.00310394e-01
   8.17850592e-01 -2.09371844e-01  1.11341623e+00]
 [-7.43297333e-01 -6.04458342e-01  1.15817143e-01  3.92723163e-01
  -1.37538530e-01 -1.07133422e+00  5.58712720e-01  1.68988128e+00
  -3.78987788e-01  2.05051189e-02 -1.11049256e+00 -8.72058999e-03
  -9.15559063e-01  1.67048688e-01  1.54128788e+00]
 [ 5.17836157e-01 -7.25315353e-01  7.98810309e-01 -1.72152952e+00
   1.20023885e+00  2.96490384e-01 -1.06440306e+00 -3.28244493e-01
  -9.10869775e-01  1.98216333e+00  5.61164198e-01 -1.01107475e+00
  -6.77100670e-01  1.48227436e-01 -5.78089149e-01]]
Wy: [[ 0.22369028  0.3665932  -1.45445982  0.59984846  1.65686924]
 [ 0.3063363   0.60795344 -0.52274185 -0.51791238  0.2916135 ]
 [-0.88719727 -1.6165354   0.81215385 -0.65629884  0.20371847]
 [ 0.10059741  0.39416105  0.58305368  0.51152733 -0.30284741]
 [ 0.79997067 -0.37036938  0.34152201 -0.63096327  0.06960731]
 [-0.86009609  1.37132047  0.31171596 -0.74105137 -1.79463257]
 [-0.73480587  1.28456605 -0.65457587  0.96032221 -0.23224853]
 [-0.34682333 -1.06581629  0.26457867  1.00494415  0.75227017]
 [ 0.49679698 -1.05750513  0.07043388 -1.1645268  -0.87609924]
 [ 0.3345957  -1.09416655  0.44512688 -0.3522659   1.38699011]
 [-0.20590439  0.43647166  0.94353757  0.51910556  0.57192416]
 [-1.78770604  0.82037104 -1.67702141 -0.74902616 -2.51437871]
 [-0.41514197 -0.75213326 -0.32451789 -1.06451065 -0.25582782]
 [-0.81382581 -0.2822963   0.72823683 -2.2559395  -0.14062891]
 [-0.24608776 -1.63540643 -0.52835299  1.32096631  0.26801178]]
bz: [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
br: [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
bh: [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
by: [[0. 0. 0. 0. 0.]]
(8, 15)
[[ 0.23630278  0.98998925  0.70337605 -0.8934883  -0.68675219 -1.43138193
   0.85722051  0.72000897  0.59323403  0.46665668  0.90618092 -0.73216867
   0.62295978 -0.38380603  0.98239992]
 [-0.36096569  0.75208146  0.40671235 -0.69447894 -0.06094302 -0.63246575
  -0.12514052  0.73686668 -0.99334842  0.74862347 -0.98633672  0.32144001
  -0.51660863 -0.72301784 -1.07425913]
 [ 0.46185917  1.82082976 -0.42685613  0.6044154   0.91428034 -0.45204306
   0.24488866  0.93170272 -0.69403405  1.07151406 -0.73900235  0.36881956
   1.93902232 -1.70519257  0.88414043]
 [-0.99999785  0.9098005   0.98721406  0.13833382 -0.97663467 -0.94226707
   0.61027366 -0.1835817  -0.80972535 -0.49062626 -0.29317507  0.98507366
  -0.97375079  0.64587113  0.67788493]
 [ 0.38648148  0.97832306  3.30037975 -0.99368615  0.66508082 -0.99413476
   1.00153007 -0.95722948 -1.1500249   0.27401448  0.84287816 -0.09483668
  -0.53284654 -0.0337837  -0.97349466]
 [-0.99160361 -0.51118561  1.46783228 -0.85864799  0.90923747 -0.4957721
  -0.20190644  0.89237884 -0.6901318  -0.64645711 -0.83111312 -0.87001685
   1.39500763  0.59063258  0.99948902]
 [ 0.28169264 -0.99681357  1.31190699  0.36305927  1.1242142  -0.0941534
   0.87243115  0.94347705 -0.99225282 -0.85576172 -1.07148764 -0.33022001
   1.81048671  1.14907385  0.99983487]
 [-0.99233756 -0.99814877 -0.90699449  0.31418277  0.98476424  0.90427922
   0.87500801  0.99469182 -0.99259575 -0.87496971 -0.59677366  1.34286615
   0.32986642 -0.87766234  0.55909932]]
(8, 5)
[[1.08997431e-03 3.40721642e-06 7.24155658e-03 7.30623299e-02
  9.18602732e-01]
 [3.51684049e-02 3.73628253e-02 2.27943724e-01 2.39343214e-01
  4.60181832e-01]
 [1.92578289e-02 6.71333215e-04 1.03669219e-03 7.07952946e-01
  2.71081200e-01]
 [1.05743094e-03 9.27219922e-02 4.18867572e-01 4.74250692e-01
  1.31023124e-02]
 [4.24709522e-04 1.29722371e-03 3.12761321e-01 2.44426682e-03
  6.83072479e-01]
 [9.88731656e-04 1.28871410e-06 9.61304657e-01 2.82772245e-03
  3.48776001e-02]
 [9.66236383e-04 2.97140679e-04 8.22956739e-01 5.19160761e-02
  1.23863808e-01]
 [1.36626219e-04 2.08883657e-01 7.10466415e-03 7.83867071e-01
  7.98200522e-06]]
"""
