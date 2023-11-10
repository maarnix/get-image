import requests
import time

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully to {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

def periodic_image_download(url, save_path, interval_seconds):
    while True:
        download_image(url, save_path)
        time.sleep(interval_seconds)

if __name__ == "__main__":
    # Replace these values with your specific URL and desired save path
    image_url = "http://193.162.14.47:8081/jpg/1/image.jpg"
    save_path = "downloaded_image.jpg"
    
    # Set the interval in seconds (e.g., 60 seconds for one minute)
    download_interval_seconds = 60
    
    periodic_image_download(image_url, save_path, download_interval_seconds)
