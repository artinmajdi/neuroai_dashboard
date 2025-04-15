import streamlit as st
import streamlit.components.v1 as components
import os
import json

def render_tsx_component(tsx_file_path):
    """
    Renders a TSX React component in Streamlit using streamlit.components.v1

    This function takes a path to a TSX file and renders it in the Streamlit app.
    It uses a simple HTML wrapper with React and ReactDOM loaded from CDN.

    Args:
        tsx_file_path (str): Path to the TSX file to render

    Returns:
        None: The component is rendered directly in the Streamlit app
    """
    # Check if file exists
    if not os.path.exists(tsx_file_path):
        st.error(f"TSX file not found: {tsx_file_path}")
        return

    # Get the component name from the file path
    file_name = os.path.basename(tsx_file_path)
    component_name = os.path.splitext(file_name)[0].replace('-', '')

    # For K99R00, extract just the component name part
    if component_name.lower() == 'k99r00slidedeck':
        component_name = 'K99R00Slides'
    elif component_name.lower() == 'nsfcareerslidedeck':
        component_name = 'NSFCareerSlides'
    elif component_name.lower() == 'mcknightscholarslidedeck':
        component_name = 'McKnightScholarsSlides'

    # Read the TSX file content
    with open(tsx_file_path, 'r') as f:
        tsx_content = f.read()

    # Create HTML with React and Tailwind CSS
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://unpkg.com/react@17/umd/react.development.js"></script>
        <script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"></script>
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ margin: 0; padding: 0; }}
        </style>
    </head>
    <body>
        <div id="root"></div>

        <script type="text/babel">
        {tsx_content}

        ReactDOM.render(
            <{component_name} />,
            document.getElementById('root')
        );
        </script>
    </body>
    </html>
    """

    # Render the HTML using streamlit.components.v1
    components.html(html_content, height=800, scrolling=True)
