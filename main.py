import functions_framework
import requests

@functions_framework.http
def hello_world(request):
    return "Hello World!", 200

@functions_framework.http
def save_image_local(request):
    """Saves an image from a URL to local temporary storage."""

    image_url = "https://images.pexels.com/photos/27168459/pexels-photo-27168459/free-photo-of-a-clock-tower-is-in-the-foreground-of-a-blurry-photo.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"  

    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        temp_file_path = "/tmp/downloaded_image.jpg"  

        with open(temp_file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192): 
                f.write(chunk)

        return f"Image downloaded and saved to {temp_file_path}", 200

    except requests.exceptions.RequestException as e:
        return f"Error downloading image: {e}", 500
    except Exception as e:
        return f"An unexpected error occurred: {e}", 500
    
