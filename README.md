# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Setup

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```
## Pass environment variable 
if you'd like to change your player name in the game, set an environemnt variable before running:

```player_name="Jon Snow" python game.py

if you'd don't do this, the game will default you as "player one" 

## Usage

Run the rock paper scissors game:

```sh
python game.py
```

## Testing

Run tests:

```sh
pytest
```
