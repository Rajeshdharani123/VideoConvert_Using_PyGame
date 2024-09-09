Cartoonize Video using OpenCV and Pygame
This project allows you to cartoonize a video using OpenCV and display it in real-time using Pygame. Each frame of the video is processed with edge detection and color filtering to create a cartoon effect.

Features
Cartoonizes video frames in real-time.
Displays video using Pygame.
Customizable edge detection and color filtering.
Prerequisites
Before running the code, ensure you have the following Python libraries installed:

OpenCV: For image and video processing
Pygame: For displaying the video in a window
Numpy: For efficient array manipulation
You can install the required libraries using the following command:


  pip install opencv-python pygame numpy
##How it Works
Edge Detection: The video frame is converted to grayscale and then a median blur is applied to reduce noise. Adaptive thresholding is used to detect edges in the frame.
Color Filtering: A bilateral filter is applied to reduce the number of colors in the image, which helps give a cartoon-like appearance.
Combining the Effects: The edge mask is combined with the color-filtered frame to create the final cartoonized frame.
Display: The cartoonized frames are displayed in real-time using Pygame.
##How to Use
Clone or download the project files.
Make sure you have a video file to cartoonize.
Update the video_path variable in the Python code with the path to your video file.
Run the script:

  python your_script_name.py
Example Usage:

  video_path = r"C:\path_to_your_video\video.mp4"
  display_video(video_path)
Code Structure
cartoonize_image(image): This function applies cartoon effects to a single frame of the video. It converts the frame to grayscale, applies edge detection, and reduces the number of colors using bilateral filtering.

  display_video(video_path) 
  This function loads the video file, applies cartoonization to each frame, and displays it in real-time using Pygame.

##Key Functions
  OpenCV (cv2)
  cv2.cvtColor(): Converts the image between color spaces.
  cv2.medianBlur(): Reduces image noise.
  cv2.adaptiveThreshold(): Performs adaptive thresholding to detect edges.
  cv2.bilateralFilter(): Reduces the number of colors while preserving edges.
  Pygame
  pygame.display.set_mode(): Initializes the screen to display the video.
  pygame.surfarray.make_surface(): Converts a Numpy array to a Pygame surface for display.
##Troubleshooting
If the video doesn't open, make sure the video path is correct and that the video file is supported by OpenCV.
If you encounter performance issues, consider resizing the video to a lower resolution before running the code.
License
This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.

