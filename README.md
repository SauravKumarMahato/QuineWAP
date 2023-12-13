# <p align="center">QuineWAP: Generate Your Code</p>

<p align="center">
    <img src="./images/QuineWAP.jpg" width=300 height=300 />
</p>


[QuineWAP](https://github.com/SauravKumarMahato/QuineWAP)  project is a Streamlit web application that leverages the GPT API for code generation. Its intuitive interface features a left section for inputting code explanations and selecting programming languages, while the right section dynamically displays the generated code in a programming-friendly font. QuineWAP combines the power of GPT with the simplicity of Streamlit, offering an interactive platform for code generation and exploration.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Runnig Application](#running-application)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

**Code Generator**: You explain all the requirements of the code and select the language/framework you want to generate your code in and then click `Generate Code` button to get the code on right half portion of streamlit app.

## Demo
<!-- demo link -->
https://github.com/SauravKumarMahato/QuineWAP/assets/83631265/1e2e6a14-8f71-4063-bc6c-c1d82dbe8dda



## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from python.org.

Before running QuineWAP, you will need an OpenAI API key if the project utilizes OpenAI's services. You can obtain an API key by registering on the OpenAI platform.

### Setup

1. Clone the repository:

```bash
git clone https://github.com/SauravKumarMahato/QuineWAP.git
```

2. Navigate to the cloned directory:

```bash
cd QuineWAP
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Add your OpenAI API key at the top [gpt_requester.py](./gpt_requester.py) files having section something like below: 

```python
openai.api_key = "YOUR_API_KEY"
```

## Running Application

For running the Projet write below code in your terminal.

```bash
streamlit run app.py
```

It will now open a web interface of streamlit and now you can test the application.

## Dependencies

Main dependencies which are required for this project to run are given below:

- openai 
- streamlit

You can find all dependencies required in  `requirements.txt`

## Contributing

We encourage contributions to enhance and elevate [QuineWAP](https://github.com/SauravKumarMahato/QuineWAP.git). Don't hesistate to submit issues, suggest new features, or initiate pull requests. Kindly follow our Code of Conduct for a respectful and collaborative environment.

## License

This project is licensed under the [MIT License](/LICENSE).
