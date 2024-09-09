import cv2
import pygame
import numpy as np

def cartoonize_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a median blur to reduce image noise
    gray = cv2.medianBlur(gray, 5)
    
    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )
    
    # Reduce the number of colors using bilateral filtering
    color = cv2.bilateralFilter(image, 9, 300, 300)
    
    # Combine the edge mask with the color-filtered image
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon

def display_video(video_path):
    # Initialize pygame
    pygame.init()

    # Open the video file
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    # Get video properties
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    # Set up pygame display
    screen = pygame.display.set_mode((frame_width, frame_height))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Read the next frame
        ret, frame = video.read()
        if not ret:
            break

        # Cartoonize the frame
        cartoon_frame = cartoonize_image(frame)
        
        # Convert the frame to RGB (pygame uses RGB format)
        cartoon_frame_rgb = cv2.cvtColor(cartoon_frame, cv2.COLOR_BGR2RGB)
        
        # Transpose the frame array to match pygame's format
        cartoon_frame_rgb = np.transpose(cartoon_frame_rgb, (1, 0, 2))

        # Convert the frame to a surface object
        frame_surface = pygame.surfarray.make_surface(cartoon_frame_rgb)
        
        # Display the frame
        screen.blit(frame_surface, (0, 0))
        pygame.display.flip()
        
        # Wait to maintain the correct FPS
        clock.tick(fps)

    # Release video object and quit pygame
    video.release()
    pygame.quit()

# Example usage
video_path = r"C:\Users\4a Freeboard\Videos\AnyDesk\demovedio.mp4"  # Replace with your video path
display_video(video_path)
