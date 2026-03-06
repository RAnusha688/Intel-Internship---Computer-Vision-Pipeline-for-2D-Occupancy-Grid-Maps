# Intel Internship - Computer Vision Pipeline for 2D Occupancy Grid Maps

## Overview

Developed a **computer vision pipeline** to generate 2D occupancy grid maps of indoor environments. The system converts raw visual input into structured representations of free and occupied space, supporting robotics navigation and spatial understanding.

## Key Contributions

* **Image Preprocessing:** Performed filtering, normalization, and noise reduction to prepare input images for feature detection.
* **Feature Detection:** Implemented algorithms to detect key points and edges for spatial mapping.
* **Spatial Mapping:** Converted detected features into 2D occupancy grids representing free and occupied space.
* **Perception Pipeline:** Integrated core components of a perception pipeline suitable for robotics navigation.

## Technologies Used

* Python
* OpenCV
* NumPy
* Matplotlib (for visualization)
* ROS ( for robotics integration)

## Project Structure

```
intel_cv_pipeline/
├── data/               # Sample images or datasets
├── scripts/            # Image processing and mapping scripts
│   ├── preprocess.py
│   ├── feature_detect.py
│   └── occupancy_grid.py
├── results/            # Output occupancy grid maps
├── README.md           # Project documentation
└── requirements.txt    # Dependencies
```

## Installation

```bash
git clone <your-repo>
cd intel_cv_pipeline
pip install -r requirements.txt
```

## Usage

```bash
python scripts/preprocess.py --input data/image1.png --output results/preprocessed.png
python scripts/feature_detect.py --input results/preprocessed.png --output results/features.png
python scripts/occupancy_grid.py --input results/features.png --output results/occupancy_grid.png
```

## Results

* Generated **2D occupancy grids** from raw indoor images.
* Visualizations include **free vs occupied space** and mapped features.
* Pipeline supports integration into **robotics navigation systems**.


## Limitations

* Assumes indoor environments with good lighting and clear features.
* May require tuning for different camera perspectives or sensor noise.
* Currently 2D mapping only; no 3D reconstruction.

## Author

**Anusha Raj**

## License

MIT License
