from diffusers import StableDiffusionPipeline
import torch

if torch.cuda.is_available():
    print("Using GPU...")
else:
    print("Using CPU...")

model_id = "runwayml/stable-diffusion-v1-5"
pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
if torch.cuda.is_available():
    pipeline = pipeline.to("cuda")

prompt = "a professional photograph of a futuristic city at sunset, neon lights, high detail, cinematic lighting"
image = pipeline(prompt).images[0]
image.save("generated_image.png")
print("Image saved as generated_image.png")