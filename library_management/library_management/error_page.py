def context_404(context):
    # Add custom values to the 404 page context
    context.custom_404_message = "Oops! This page does not exist."
    context.show_button = True
    context.button_label = "Go to Home"
    context.button_url = "/"
