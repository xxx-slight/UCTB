import os

import warnings
warnings.filterwarnings("ignore")

shared_params_amulti_gclstm = ('python -m Experiment.AMulti_GCLSTM_Bike --Train True --T 12'
                               ' --Epoch 10000 --BatchSize 64 --lr 1e-3 --patience 50'
                               ' --K 1 --L 1 --GLL 1 --LSTMUnits 64 --GALUnits 64 --GALHeads 2 --DenseUnits 32'
                               ' --TC 0 --TD 1000 --TI 500'
                               ' --TrainDays All'
                               ' --Device 0 ')

if __name__ == "__main__":

    os.system(shared_params_amulti_gclstm + '--City NYC --Graph Distance --K 1 --L 1 --CodeVersion V0')
    os.system(shared_params_amulti_gclstm + '--City NYC --Graph Interaction --K 1 --L 1 --CodeVersion V0')
    os.system(shared_params_amulti_gclstm + '--City NYC --Graph Correlation --K 1 --L 1 --CodeVersion V0')

    os.system(shared_params_amulti_gclstm + '--City DC --Graph Distance --K 1 --L 1 --CodeVersion V0')
    os.system(shared_params_amulti_gclstm + '--City DC --Graph Interaction --K 1 --L 1 --CodeVersion V0')
    os.system(shared_params_amulti_gclstm + '--City DC --Graph Correlation --K 1 --L 1 --CodeVersion V0')

    os.system(shared_params_amulti_gclstm + '--City Chicago --Graph Distance --K 1 --L 1 --CodeVersion V0')
    os.system(shared_params_amulti_gclstm + '--City Chicago --Graph Interaction --K 1 --L 1 --CodeVersion V0')
    os.system(shared_params_amulti_gclstm + '--City Chicago --Graph Correlation --K 1 --L 1 --CodeVersion V0')