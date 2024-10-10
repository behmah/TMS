import openai

def get_phi3_response(user_input):
    """
    Interacts with the phi3 model hosted by Ollama to generate a response based on user input.

    Args:
        user_input (str): The input text from the user.

    Returns:
        str: The formatted response from the phi3 model. If there is an error, returns an error message.
    """
    # Set up the connection to the phi3 model hosted by Ollama
    client = openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="nokeyneeded",  # The API key is not required for local access
    )

    # Define the request message
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input},
    ]

    try:
        # Call the model and get the response
        response = client.chat.completions.create(
            model="phi3",
            temperature=0.2,
            n=1,  # We only need one response
            messages=messages,
        )

        # Extract the model's response
        model_response = response.choices[0].message.content.strip()
        
        # Optional: Format the response for better readability
        formatted_response = model_response.replace('\n', '<br>')  # Convert line breaks to HTML
        return formatted_response

    except Exception as e:
        return f"Error communicating with the model: {str(e)}"
