from django.shortcuts import render
from .ollama_phi import get_phi3_response

def chatphi(request):
    """
    Handles user input for the phi3 model and displays the response.

    If the request method is POST, it extracts user input from the request, calls the `get_phi3_response`
    function to communicate with the phi3 model, and renders the `ollama_phi.htm` template with the model's response.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the `ollama_phi.htm` template with the model's response and user input.
    """
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        # Call the function that interacts with the phi3 model
        response = get_phi3_response(user_input)
        return render(request, 'ollama_phi.htm', {'response': response, 'user_input': user_input})
    
    return render(request, 'ollama_phi.htm')
