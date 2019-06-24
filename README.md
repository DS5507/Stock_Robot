# Stock_Robot

# Creating a local copy of the app
Navigate to https://github.com/DS5507/Stock_Robot
Fork and clone the repository.


# Setting up a virtual environment
From the command line navigate to the repository.
```sh
cd ~/Desktop/Stock_Robot
```

Create a virtual environment from the command line.
```sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```

From within the virtual environment, install the required packages specified in the "requirements.txt".
```sh
pip install -r requirements.txt
```

# App Credentials
Create a file named ".env".  Insert the code below into the file and replace "demo" with your own API key.

```sh
ALPHAVANTAGE_API_KEY="demo"
```

# Run the app
Run the app.
```sh
python app/robo_advisor.py
```
