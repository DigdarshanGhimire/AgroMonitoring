import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image


class Models:
    
    def __init__(self):
        self.mapperDisease = {
            0:'Healthy',
            1:'Powdery',
            2:'Rusty'
        }
        #self.pest()
        self.disease()
        self.imgpath = 'images/plants.jpg'
        
        
    # Load the pest model
    def pest(self):
        self.pestModel = tf.keras.models.load_model('models/model.h5')

    def disease(self):
        self.diseaseModel = tf.keras.models.load_model('models/disease.h5')
    
    # Function to preprocess the image
    def predictDisease(self):
        img = image.load_img(self.imgpath)  # Resize to match model's expected input
        img_array = image.img_to_array(img)                      # Convert to array
        img_array = tf.expand_dims(img_array,0)            # Add batch dimension
                            # Normalize to [0, 1]

        predictions = self.diseaseModel.predict(img_array)
        print(predictions)

        predicted_class = np.argmax(predictions, axis=1)

        return (self.mapperDisease.get(predicted_class[0]))
    
    def predictPest(self):
            img = image.load_img(self.img_path, target_size=(256, 256))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
            img_array = img_array / 255.0  # Normalize to [0,1] range

            # Make prediction
            predictions = model.predict(img_array)
            predicted_class = np.argmax(predictions, axis=1)
            return predicted_class


if __name__ == "__main__":
    model = Models()
    print(model.predictDisease())