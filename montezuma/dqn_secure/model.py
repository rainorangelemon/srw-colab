from keras.layers import Input
from keras.layers.core import Dense, Flatten, Permute
from keras.layers.convolutional import Convolution2D
from keras.models import Model
from keras import backend as K

floatX = 'float32'


def build_large_cnn(state_shape, num_channels, nb_actions):
    #  Network used in: Playing Atari with Deep Reinforcement Learning, Nips 2013

    input_dim = tuple([num_channels] + state_shape)
    states = Input(shape=input_dim, dtype=floatX, name='states')
    print(K.image_data_format())
    conv1 = Convolution2D(nb_filter=16,
                      nb_row=8,
                      nb_col=8,
                      border_mode='same',
                      subsample=(4, 4),
                      activation='relu',
                      init='he_uniform',
                      data_format=K.image_data_format())(states)
    conv2 = Convolution2D(nb_filter=32,
                      nb_row=4,
                      nb_col=4,
                      border_mode='same',
                      subsample=(2, 2),
                      activation='relu',
                      init='he_uniform',
                      data_format=K.image_data_format())(conv1)
    flatten = Flatten()(conv2)
    dense1 = Dense(output_dim=256,
               init='he_uniform',
               activation='relu')(flatten)
    out = Dense(input_dim=256,
            output_dim=nb_actions,
            init='he_uniform',
            activation='linear')(dense1)
    return Model(input=states, output=out)
