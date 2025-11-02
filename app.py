import gradio as gr
import sys
import os

# Add the dist directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'dist'))

# Import obfuscated module
try:
    from core_logic import (
        remove_background_secure,
        upscale_image_secure,
        blur_background_secure,
        get_company_info,
        get_remb_example_images,
        get_upscale_example_images,
        get_blur_example_images,
        create_footer,
        get_custom_css
    )
except ImportError as e:
    print(f"Error: Obfuscated module not found: {e}")
    print("Current directory:", os.getcwd())
    print("Files in dist:", os.listdir('dist') if os.path.exists('dist') else 'dist not found')
    sys.exit(1)

# Create Gradio interface
with gr.Blocks(title="Miragic AI Background", theme=gr.themes.Ocean(), css=get_custom_css()) as demo:
    gr.Markdown("""
    <div style="display: flex; align-items: center;">
        <img src="https://avatars.githubusercontent.com/u/211682198?s=200&v=4" style="width: 80px; margin-right: 20px;"/>
        <div>
            <h1 style="margin-bottom: 0;">Miragic AI Background</h1>
            <p>Choose from our powerful AI image processing features!</p>
        </div>
    </div>
    """)
    
    gr.Markdown(get_company_info())
    
    with gr.Tabs():
        # Tab 1: Background Remover
        with gr.TabItem("🎨 Background Remover"):
            with gr.Row():
                with gr.Column():
                    bg_remove_input = gr.Image(
                        label="Upload Image",
                        type="pil",
                        sources=["upload", "clipboard"],
                        height=300
                    )
                    
                    with gr.Accordion("Background Replacement Options", open=False):
                        bg_file_input = gr.Image(
                            label="Custom Background Image (Optional)",
                            type="pil",
                            sources=["upload", "clipboard"],
                            height=200
                        )
                        
                        bg_color_input = gr.ColorPicker(
                            label="Custom Background Color (Optional)",
                            value="#FFFFFF"
                        )
                    
                    gr.Examples(
                        examples=get_remb_example_images(),
                        inputs=bg_remove_input,
                        label="Try these examples!",
                        examples_per_page=5
                    )
                    
                    bg_remove_btn = gr.Button("Remove Background 🚀", elem_classes="button-gradient")
                
                with gr.Column():
                    bg_remove_slider = gr.ImageSlider(
                        label="Before & After Comparison (Drag to compare)",
                        type="pil",
                        show_download_button=True,
                        height=500  # Fixed height to match input
                    )

                    gr.HTML("""
                    <div class="interaction-section">
                        <p>If you like our AI Background service, please give us a ⭐ in our space!</p>
                    </div>
                    """)

                    signup_prompt = gr.HTML(
                        visible=True,
                        value="""<div class="signup-container">
                            <h3>🚀 Want unlimited generations?</h3>
                            <p>Please sign up at Miragic.ai for unlimited access to all our AI Features!</p>
                            <a href='https://miragic.ai/products/ai-background' target='_blank' class="signup-button">
                                SignUp for Free 🚀
                            </a>
                        </div>"""
                    )
        
        # Tab 2: Image Upscaler
        with gr.TabItem("🔍 Image Upscaler"):
            with gr.Row():
                with gr.Column():
                    upscale_input = gr.Image(
                        label="Upload Image to Upscale",
                        type="pil",
                        sources=["upload", "clipboard"],
                        height=300
                    )
                    
                    gr.Examples(
                        examples=get_upscale_example_images(),
                        inputs=upscale_input,
                        label="Try these examples!",
                        examples_per_page=5
                    )
                    
                    upscale_btn = gr.Button("Upscale Image 🚀", elem_classes="button-gradient")
                
                with gr.Column():
                    upscale_slider = gr.ImageSlider(
                        label="Before & After Comparison (Drag to compare)",
                        type="pil",
                        show_download_button=True,
                        height=500  # Fixed height to match input
                    )

                    gr.HTML("""
                    <div class="interaction-section">
                        <p>If you like our AI Background service, please give us a ⭐ in our space!</p>
                    </div>
                    """)

                    signup_prompt = gr.HTML(
                        visible=True,
                        value="""<div class="signup-container">
                            <h3>🚀 Want unlimited generations?</h3>
                            <p>Please sign up at Miragic.ai for unlimited access to all our AI Features!</p>
                            <a href='https://miragic.ai/products/ai-background' target='_blank' class="signup-button">
                                SignUp for Free 🚀
                            </a>
                        </div>"""
                    )
        
        # Tab 3: Background Blur
        with gr.TabItem("🌄 Background Blur"):
            with gr.Row():
                with gr.Column():
                    blur_input = gr.Image(
                        label="Upload Image",
                        type="pil",
                        sources=["upload", "clipboard"],
                        height=300
                    )
                    
                    blur_radius_slider = gr.Slider(
                        minimum=0.1,
                        maximum=1.0,
                        value=0.5,
                        step=0.1,
                        label="Blur Radius Intensity"
                    )
                    
                    gr.Examples(
                        examples=get_blur_example_images(),
                        inputs=blur_input,
                        label="Try these examples!",
                        examples_per_page=5
                    )
                    
                    blur_btn = gr.Button("Blur Background 🚀", elem_classes="button-gradient")
                
                with gr.Column():
                    blur_slider = gr.ImageSlider(
                        label="Before & After Comparison (Drag to compare)",
                        type="pil",
                        show_download_button=True,
                        height=500  # Fixed height to match input
                    )

                    gr.HTML("""
                    <div class="interaction-section">
                        <p>If you like our AI Background service, please give us a ⭐ in our space!</p>
                    </div>
                    """)

                    signup_prompt = gr.HTML(
                        visible=True,
                        value="""<div class="signup-container">
                            <h3>🚀 Want unlimited generations?</h3>
                            <p>Please sign up at Miragic.ai for unlimited access to all our AI Features!</p>
                            <a href='https://miragic.ai/products/ai-background' target='_blank' class="signup-button">
                                SignUp for Free 🚀
                            </a>
                        </div>"""
                    )
    
    # Handle generation for each feature with ImageSlider
    def handle_bg_remove(image, bg_file, bg_color, request: gr.Request):
        if not image:
            raise gr.Error("Please upload an image first!")
        result = remove_background_secure(image, bg_file, bg_color, request)
        return (image, result)
    
    def handle_upscale(image, request: gr.Request):
        if not image:
            raise gr.Error("Please upload an image first!")
        result = upscale_image_secure(image, request)
        return (image, result)
    
    def handle_blur(image, blur_radius, request: gr.Request):
        if not image:
            raise gr.Error("Please upload an image first!")
        result = blur_background_secure(image, blur_radius, request)
        return (image, result)
    
    # Connect the functions
    bg_remove_btn.click(
        fn=handle_bg_remove,
        inputs=[bg_remove_input, bg_file_input, bg_color_input],
        outputs=bg_remove_slider
    )
    
    upscale_btn.click(
        fn=handle_upscale,
        inputs=[upscale_input],
        outputs=upscale_slider
    )
    
    blur_btn.click(
        fn=handle_blur,
        inputs=[blur_input, blur_radius_slider],
        outputs=blur_slider
    )

    gr.HTML('<a href="https://visitorbadge.io/status?path=https%3A%2F%2Fhuggingface.co%2Fspaces%2FMiragic-AI%2FMiragic-AI-Background"><img src="https://api.visitorbadge.io/api/combined?path=https%3A%2F%2Fhuggingface.co%2Fspaces%2FMiragic-AI%2FMiragic-AI-Background&labelColor=%2337d67a&countColor=%23ff8a65&style=plastic&labelStyle=upper" /></a>')

    # Footer
    gr.HTML(create_footer())
    
if __name__ == "__main__":
    demo.launch()