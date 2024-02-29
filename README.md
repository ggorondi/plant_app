# Plant App

This project is a simple web application made with Django // React // Tensorflow. 

It provides a simple interface for users to upload images of plants and receive classification results using a Pre trained Convolutional Neural Network.

https://github.com/ggorondi/plant_app/assets/113739099/85d2d9e8-f853-423d-86dc-aeb143250890

## How It Works

1. **Upload Image**: Users can upload an image of a plant using the drag-and-drop dropzone interface.
2. **Image Processing**: The uploaded image is sent to the Django backend, where it is processed by a pre-trained TensorFlow model, which is a fine-tuned MobileNetV2 trained on a custom dataset of plant images.
3. **Classification**: The model classifies the image into one of the 129 plant species with associated certainty percentages and presents the top prediction to the user.

## Dataset and Model

The MobileNetV2 model used in the project has been trained by applying transfer learning on the last few layers and adding a fully connected dense classification layer. 
I used and modified a dataset of plant images obtained from a public project: ['plantnet-300k'](https://openreview.net/forum?id=eLYinD0TtIt). This dataset is not ideal for my use-case because it was designed for research, and because of this has the following issues:
- Strong class imbalance, long tailed distribution.
- Many species are visually similar and 'difficult (to classify) even for the expert eye'
- Has low quality user uploaded images.
  
To face these issues, I only kept classes with over 400 images and trimmed classes with +1000 images. This approach improved validation accuracy by a wide margin. For 129 classes of plants the model achieves about 59% test accuracy, which is far from ideal but sufficient for my MVP. Further improvements include expanding the dataset with more images, cleaning and filtering the current images, and trying out different model architectures like ResNet. 

## Usage

To run the Plant App locally:

1. Clone the repository.
2. Navigate to the backend directory and install the required dependencies using `pip install -r requirements.txt`.
3. Run the Django backend server using `python manage.py runserver`.
4. Navigate to the frontend directory and install the required dependencies using `npm install`.
5. Start the React frontend server using `npm start`.
6. Access the Plant App in your web browser at `http://localhost:3000`.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it according to your needs.
