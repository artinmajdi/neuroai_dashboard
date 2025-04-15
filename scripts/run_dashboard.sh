#!/bin/bash

# Define colors for better user experience
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get the root directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$( cd "$SCRIPT_DIR/.." && pwd )"

echo -e "${BLUE}=== NeuroAI Dashboard Runner ===${NC}"
echo "This script helps you run the NeuroAI dashboard."
echo ""

# Check if .env file exists
if [ ! -f "$ROOT_DIR/.env" ]; then
    echo -e "${YELLOW}Warning: .env file not found. Some features may not work properly.${NC}"
    echo -e "Consider running './scripts/setup_env.sh' first to set up your environment."
    echo ""
fi

# Prompt user to choose between Docker and directly running the app
echo "Please choose how you would like to run the dashboard:"
echo -e "${BLUE}1)${NC} Run using Docker (recommended for production use)"
echo -e "${BLUE}2)${NC} Run directly with local environment (recommended for development)"
echo ""

read -p "Enter your choice (1/2): " choice

case $choice in
    1)
        echo -e "${GREEN}Starting Docker container...${NC}"
        "$SCRIPT_DIR/run_docker.sh" start
        ;;
    2)
        echo -e "${GREEN}Starting application directly...${NC}"

        # Check if virtual environment exists and activate if found
        if [ -d "$ROOT_DIR/.venv" ]; then
            echo -e "${BLUE}Using virtual environment...${NC}"
            source "$ROOT_DIR/.venv/bin/activate" || source "$ROOT_DIR/.venv/Scripts/activate"
        else
            # Check if we're in a conda environment
            if command -v conda &> /dev/null && [ -n "$CONDA_DEFAULT_ENV" ]; then
                echo -e "${BLUE}Using conda environment: $CONDA_DEFAULT_ENV${NC}"
            else
                echo -e "${YELLOW}Warning: No virtual environment detected, using system Python.${NC}"
                echo -e "Consider running './scripts/install.sh' first to set up your environment."
            fi
        fi

        # Determine the application entry point
        APP_PATH=""
        if [ -f "$ROOT_DIR/src/visualization/app.py" ]; then
            APP_PATH="src/visualization/app.py"
        elif [ -f "$ROOT_DIR/src/dashboard/app.py" ]; then
            APP_PATH="src/dashboard/app.py"
        elif [ -f "$ROOT_DIR/src/app.py" ]; then
            APP_PATH="src/app.py"
        elif [ -f "$ROOT_DIR/src/main.py" ]; then
            APP_PATH="src/main.py"
        else
            echo -e "${YELLOW}No application entry point found. Please specify the path:${NC}"
            read -p "Enter the relative path to your application file: " custom_path
            APP_PATH="$custom_path"
        fi

        # Start React frontend (in background)
        if [ -d "$ROOT_DIR/react-slides" ]; then
            echo -e "${GREEN}Starting React frontend (slide decks)...${NC}"
            cd "$ROOT_DIR/react-slides"
            if command -v npm &> /dev/null; then
                npm run dev &
                REACT_PID=$!
                echo -e "${BLUE}React frontend running at http://localhost:3000${NC}"
            else
                echo -e "${YELLOW}npm (Node.js) not found. React slide decks will not be available.\nInstall Node.js and run 'npm run dev' in react-slides manually.${NC}"
            fi
            cd "$ROOT_DIR"
        fi

        # Start Streamlit backend
        if command -v streamlit &> /dev/null; then
            echo -e "${GREEN}Starting Streamlit application: $APP_PATH${NC}"
            streamlit run "$APP_PATH" &
            STREAMLIT_PID=$!
        else
            echo -e "${GREEN}Starting Python application: $APP_PATH${NC}"
            python "$APP_PATH" &
            STREAMLIT_PID=$!
        fi

        echo -e "\n${BLUE}To stop the React frontend, run:${NC}"
        echo -e "${YELLOW}    kill $REACT_PID${NC}"
        echo -e "${BLUE}To stop the Streamlit backend, run:${NC}"
        echo -e "${YELLOW}    kill $STREAMLIT_PID${NC}"
        wait $STREAMLIT_PID
        ;;
    *)
        echo -e "${YELLOW}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac
