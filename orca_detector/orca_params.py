"""
Global parameters for the OrcaVGGish model.

W251 (Summer 2019) - Spyros Garyfallos, Ram Iyer, Mike Winton
"""

from enum import IntEnum


class DatasetType(IntEnum):
    """ Enumeration with the possible dataset types. """
    TRAIN = 0
    VALIDATE = 1
    TEST = 2


# Paths to key volumes mapped into the Docker container
DATA_PATH = '/data/'
OUTPUT_PATH = '/results/'
WEIGHTS_PATH = '/vggish_weights/vggish_audioset_weights_without_fc2.h5'
WEIGHTS_PATH_TOP = '/vggish_weights/vggish_audioset_weights.h5'

# Classification params
OTHER_CLASS = 'Other'
REMOVE_CLASSES = ['BowheadWhale', 'Narwhal', 'SpermWhale',
                  'TucuxiDolphin', 'White_sidedDolphin', 'DallsPorpoise',
                 'HarpSeal', 'LeopardSeal', 'RibbonSeal',
                 'RingedSeal', 'SpottedSeal']
OTHER_CLASSES = []

# Weighting to account for imbalance when calculating loss
# TODO: update weights based on observed balance
# CLASS_WEIGHTS = {0: 1., 1: 1., 2: 1.}
OPTIMIZER = 'sgd'
LOSS = 'categorical_crossentropy'

# Model training
EPOCHS = 5
BATCH_SIZE = 128

# Model hyperparameters
FILE_MAX_SIZE_SECONDS = 10.00
FILE_SAMPLING_SIZE_SECONDS = 0.98