# Plant App

The Plant App is a simple web application that uses Django for backend and React on the frontend. 
It provides a simple interface for users to upload images of plants and receive classification results using a Keras/TensorFlow model.

## Features

- **Image Upload**: Users can upload images of plants using a drag-and-drop interface.
- **Plant Classification**: The uploaded images are processed by a pre-trained TensorFlow model, which has been trained on a custom dataset of plant images. The model applies transfer learning on a MobileNetV2 architecture to classify images into 129 different species of plants.
- **Classification Results**: After processing, the application displays the top prediction for the uploaded image along with the percentage of certainty.

## How It Works

1. **Upload Image**: Users can upload an image of a plant using the provided dropzone interface.
2. **Image Processing**: The uploaded image is sent to the Django backend, where it is processed by the pre-trained TensorFlow model.
3. **Classification**: The TensorFlow model classifies the image into one of the 129 plant species with associated certainty percentages.
4. **Display Results**: The application presents the top prediction and its certainty percentage to the user.

## Dataset and Model

The TensorFlow model used in the Plant App has been trained on a custom dataset of plant images obtained from a public GitHub project. The dataset was cleaned and used for transfer learning on the MobileNetV2 architecture. This approach allows for accurate classification of a wide range of plant species.

## Usage

To run the Plant App locally:

1. Clone the repository.
2. Navigate to the backend directory and install the required dependencies using `pip install -r requirements.txt`.
3. Run the Django backend server using `python manage.py runserver`.
4. Navigate to the frontend directory and install the required dependencies using `npm install`.
5. Start the React frontend server using `npm start`.
6. Access the Plant App in your web browser at `http://localhost:3000`.

## Credits

- The TensorFlow model training and transfer learning techniques were adapted from the TensorFlow documentation and tutorials.
- The plant image dataset used for training was obtained from a public GitHub project.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it according to your needs.
