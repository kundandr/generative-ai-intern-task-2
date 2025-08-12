This project demonstrates the process of using a pre-trained generative AI model to create an image from a text prompt. The entire workflow was completed locally on a personal computer using VS Code, with the final project stored on a GitHub repository.
Process
1.Environment Setup: The local environment was prepared by installing Python, VS Code, and Git. The necessary AI libraries, including `diffusers`, `transformers`, and `torch`, were installed using the `pip` package manager.
2.Model and Code: The "Stable Diffusion v1.5" model was loaded locally from the Hugging Face Hub using a Python script. The script was executed directly from the VS Code terminal.
3.Image Generation: A custom text prompt was used to generate an image, which was then saved as a file in the project folder.
4.Version Control: Git was used to manage the project files. The final code and generated image were committed and pushed to a GitHub repository, which serves as a public portfolio of the work.

References

"Rombach, R., et al. (2022). High-Resolution Image Synthesis with Latent Diffusion Models".This is the foundational paper for the Stable Diffusion model used in this project.
"von Platen, P., et al. (2023). Diffusers."This is the GitHub repository for the `diffusers` library, a key tool for running the model.
"Wolf, T., et al. (2020). Transformers: State-of-the-Art Natural Language Processing." This is the paper for the `transformers` library, which is essential for loading and using many AI models, including parts of this one.