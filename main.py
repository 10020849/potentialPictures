import cv2 as cv
import streamlit as st
import os
import io
import pandas as pd

# Function to read images from folder
def read_images_from_folder(folder_path):
    image_files = os.listdir(folder_path)
    images = []
    for file in image_files:
        if file.endswith(".jpg"):
            img_path = os.path.join(folder_path, file)
            if os.path.exists(img_path):
                images.append(cv.imread(img_path))
            else:
                st.warning(f"Image file not found: {img_path}")
    return images

# Function to display images with checkboxes
def display_images_with_checkboxes(images):
    for i, img in enumerate(images):
        st.image(img, caption=f"Image {i+1}")
        st.checkbox(f"Vote for Image {i+1}", key=f"vote_{i+1}")

def main():
    st.title("Potential Pictures Gallery")
    st.subheader("Browse through a collection of potential pictures")

    # Path to your folder containing images
    folder_path = "C:\\Users\\jshri\\Potential Pictures"

    # Read images from the folder
    images = read_images_from_folder(folder_path)

    # Add pp0.jpg to the image list
    pp0_path = os.path.join(folder_path, "pp0.jpg")
    if os.path.exists(pp0_path):
        images.insert(0, cv.imread(pp0_path))
    else:
        st.warning("Image file not found: pp0.jpg")

    # Display images with checkboxes for voting
    display_images_with_checkboxes(images)

    # Submit button to cast votes
    if st.button("Submit Votes"):
        selected_images = []
        vote_counts = [0] * len(images)
        for i, img in enumerate(images):
            if st.session_state[f"vote_{i+1}"]:
                selected_images.append(img)
                vote_counts[i] += 1
        st.success(f"You have voted for {len(selected_images)} images.")

        # Display table showing vote counts for each image
        df = pd.DataFrame({
            "Image": [f"Image {i+1}" for i in range(len(images))],
            "Votes": vote_counts
        })
        st.write("Vote Counts:")
        st.table(df)

if __name__ == "__main__":
    main()
