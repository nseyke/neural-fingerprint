# This experiment is designed to show that convnets can learn to predict molecular weight, while
# Morgan fingerprints can't.
#
# David Duvenaud
# Dougal Maclaurin
# Ryan P. Adams
#
# Sept 2014

import sys

from deepmolecule import get_data_file, run_nn_with_params, output_dir

def main():
    # Parameters for convolutional net.
    train_params = {'num_epochs'  : 50,
                         'batch_size'  : 10,
                         'learn_rate'  : 1e-3,
                         'momentum'    : 0.98,
                         'param_scale' : 0.1,
                         'gamma': 0.9}

    arch_params = {'num_hidden_features' : [1, 1],
                        'bond_vec_dim' : 1,
                        'permutations' : False,
                        'l2_penalty': 0.001}

    task_params = {'N_train'     : 2000,
                   'N_valid'     : 1000,
                   'N_test'      : 3000,
                   'target_name' : 'Number of Rings',
                   'data_file'   : get_data_file('2014-11-03-all-tddft/processed.csv')}

    #run_nn_with_params(train_params=train_params,
    #                   arch_params=arch_params,task_params=task_params,
    #                   output_dir=output_dir())

    morgan_arch_params = {'h1_size': 100,
                          'h1_dropout': 0.01,
                          'fp_length': 512,
                          'fp_radius': 4}

    run_nn_with_params(net_type='morgan', train_params=train_params,
                       arch_params=morgan_arch_params,task_params=task_params,
                       output_dir=output_dir())

if __name__ == '__main__':
    sys.exit(main())