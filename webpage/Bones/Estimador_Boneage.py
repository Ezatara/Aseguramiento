import numpy as np

from PIL import Image

from lib.tools import features_shape, instantiate_base_model

from keras.layers import GlobalAveragePooling2D, Dense, Dropout
from keras.losses import mean_absolute_error
from keras.models import Model, Sequential
from keras.optimizers import Adam, RMSprop
from keras import backend as k


def load_image(file):
    # Receive a file path in string
    # Open and converts the image
    # Returns the raw array image
    image = Image.open(file)
    image.convert('L')
    image.resize((255, 255))
    raw_image = np.array(list(image.getdata()))
    image.close()

    return raw_image


def load_model(weights):
    # Creates a Keras model
    # Parameter weights is the path to the Keras .h5 file

    # Top model
    top_model = Sequential()
    top_model.add(GlobalAveragePooling2D(
        input_shape=features_shape(instantiate_base_model(model_name='VGG16', input_dim=(255, 255)))))

    top_model.add(Dense(1024, activation='linear'))
    top_model.add(Dropout(0.5))
    top_model.add(Dense(1024, activation='linear'))
    top_model.add(Dropout(0.5))
    top_model.add(Dense(128, activation='linear'))
    top_model.add(Dense(1, activation='linear'))

    top_model.compile(optimizer=Adam(lr=0.001), loss=mean_absolute_error, metrics=['mse', 'mae'])

    # Base model
    base_model = instantiate_base_model(model_name='VGG16', input_dim=(255, 255))

    # Full model
    full_model = Model(inputs=base_model.input, outputs=top_model(base_model.output))

    # Load weights and compile the model
    full_model.load_weights(weights)
    full_model.compile(loss=mean_absolute_error, optimizer=RMSprop(lr=0.0001), metrics=['mse', 'mae'])

    return full_model


def evaluate(model, data):
    # Estimate the bone age
    # Receive a Keras model and a raw image
    # Returns the estimation
    data = format_x(data, (255, 255))
    return model.predict(data, verbose=True)


def format_x(x, image_shape):
    # Reshapes somehow the image in order to make it processable by the model
    unscaled = x.reshape(1, image_shape[0], image_shape[1]).astype('float16')
    stacked = np.stack([unscaled, unscaled, unscaled], axis=3)
    stacked /= 255
    return stacked


def main(imagen):

    # Esta bomba puede cargar dos modelos, osea, uno con el de hombre y otro con el de mujeres.
    image = load_image(imagen)
    model = load_model("./weights/best_female_model.h5")  # Modelo de viejas
    result = evaluate(model, image)
    print(result)
    k.clear_session()  # Esta linea la usé porque yo no entiendo que porongas pasa que a veces el bichillo no funciona

    image = load_image(imagen)
    model = load_model("./weights/best_female_model.h5")  # Modelo de viejos
    result = evaluate(model, image)
    print(result)
    k.clear_session()


main()
