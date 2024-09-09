# Cartoonize Video

This project applies a cartoon effect to each frame of a video using OpenCV and displays it using Pygame.

## Requirements

Before running the script, ensure you have the following installed:

    - Python 3.x
    - OpenCV library
    - NumPy library
    - PyGame

You can install the required packages using pip:
   pip install opencv-python pygame numpy
   
## Usage
Clone the repository or download the script.

Edit the video_path variable in the script to point to the path of the video you want to cartoonize.

    video_path = r"C:\Users\4a Freeboard\Videos\AnyDesk\demovedio.mp4"  # Replace with your video path
  
  
### Run the script:

    python cartoonize_video.py

This will open a Pygame window displaying the cartoonized video.

### Functions
  cartoonize_image(image)
Applies a cartoon effect to a single frame of the video. This function:

Converts the image to grayscale.
Applies median blur to reduce noise.
Detects edges using adaptive thresholding.
Reduces the number of colors using bilateral filtering.
Combines the edge mask with the color-filtered image.
  display_video(video_path)
Opens the video file, applies the cartoon effect to each frame, and displays it using Pygame.

### Troubleshooting
If you encounter issues with video playback, ensure the path to the video is correct and that the video file is accessible.
For performance issues, consider reducing the resolution of the video.
License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
OpenCV for image processing.
Pygame for displaying the video.
