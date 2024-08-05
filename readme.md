# Anime Explainer

This project uses AI to research and explain anime based on user input. It uses CrewAI with Groq's language model to generate explanations.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [License](#license)

## Introduction

Anime Explainer is a Streamlit web application that allows users to enter the name of an anime and select focus areas to get AI-generated explanations. The app leverages CrewAI, various tools like Wikipedia and DuckDuckGo search, and Groq's language model to provide accurate and concise information.

## Installation

To get started with Anime Explainer, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/animecrewai.git
    cd  animecrewai
    ```

2. Install the required packages:
    ```bash
    pip install streamlit crewai langchain langchain_groq wikipedia duckduckgo-search
    ```

3. Create a `.env` file in the root directory and add your API key:
    ```plaintext
    GROQ_API_KEY=your_groq_api_key_here
    ```

## Usage

To run the Streamlit app:

1. Make sure you have all the necessary packages installed and the `.env` file created.
2. Save all four files (`crew.py`, `agents.py`, `tasks.py`, and `streamlit_app.py`) in the same directory.
3. Run the Streamlit app with:
    ```bash
    streamlit run streamlit_app.py
    ```

This will launch a web interface where you can enter an anime name, select focus areas, and get an AI-generated explanation.

## Features

- AI-based research and explanation of anime.
- User input for anime name and focus areas.
- Uses Wikipedia and DuckDuckGo for gathering information.
- Generates concise explanations using Groq's language model.

## Dependencies

- streamlit
- crewai
- langchain
- langchain_groq
- wikipedia
- duckduckgo-search

## Configuration

Ensure you have a `.env` file in your project root with the following content:

```plaintext
GROQ_API_KEY=your_groq_api_key_here