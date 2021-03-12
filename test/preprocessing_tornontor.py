import pandas as pd
import argparse
from helpers import *
pd.options.mode.use_inf_as_na = True

def preprocess_tornontor(TRAIN_DATA, TEST_DATA):
    # df = pd.read_csv("UNSW_NB15_training-set.csv")
    # df_test = pd.read_csv("UNSW_NB15_testing-set.csv")
    df = pd.read_csv(TRAIN_DATA, header=None, skiprows=1, sep=" ")
    df_test = pd.read_csv(TEST_DATA, header=None, skiprows=1, sep=" " )
    df = df[df.columns[1:]]
    df_test = df_test[df_test.columns[1:]]
    return df, df_test

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Normalize UNSW to work with FEMaFS and OPF")
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-ta', '--train', nargs=1, type=str, action='store',
                               help="<Required> UNSW NB15 train data ",
                               required=True)
    requiredNamed.add_argument('-te', '--test', nargs=1,
                               help="<Required> UNSW NB15 test data ",
                               action='store', type=str, required=True)
    args = parser.parse_args()

    if not args:
        print(parser.print_help)

    if args.train and args.test :
        df, df_test = preprocess_tornontor(args.train[0], args.test[0])
        df_test_sampled = df_test.sample(frac=0.1)
        df_sampled = df.sample(frac=0.1)
        generate_file(df_test_sampled, 'opf', 'test-tornontor', log1p=True)
        generate_file(df_sampled, 'opf', 'train-tornontor', log1p=True)
        generate_file(df_test_sampled, 'fem', 'test-tornontor', log1p=True)
        generate_file(df_sampled, 'fem', 'train-tornontor', log1p=True)

    else:
        print(parser.print_help)


