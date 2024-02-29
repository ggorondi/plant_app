import numpy as np
from tensorflow.keras.models import load_model
import json

def process_uploaded_image(img_array):
    """
    Uses pre-trained model to predict the plant species of the uploaded image.
    Returns top picks and their probabilities.
    Eg. [({'class_id': '1418146', 'scientific_name': 'Fittonia albivenis (Lindl. ex Veitch) Brummitt'}, '98.8%'), ({'class_id': '1394489', 'scientific_name': 'Anemone pulsatilla L.'}, '0.2%'), ({'class_id': '1409238', 'scientific_name': 'Anthurium andraeanum Linden ex André'}, '0.1%')]
    """
    
    ml_model = load_model('images/tf_models/second_model.h5')
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32')  # Convert to float32
    img_array = img_array/255
    prediction = ml_model.predict(img_array)
    # I Want to return the plant name. 
    # predicted_idx = prediction.argmax(axis=-1)[0]
    top_3_indices = np.argsort(prediction[0])[-3:][::-1]  # Indices of top 3 classes
    top_3_probabilities = prediction[0][top_3_indices]  # Probabilities of top 3 classes
    top_3_probs_percent = [prob for prob in top_3_probabilities]
    
    # Load the JSON file containing the mapping of class IDs to species names
    with open('images/tf_models/tiny_index_2_name.json', 'r') as f:
        index_2_name = json.load(f)
    
    top_3_names = [index_2_name.get(str(idx), 'Unknown') for idx in top_3_indices]
    return [(name, prob) for name, prob in zip(top_3_names, top_3_probs_percent)]
    
