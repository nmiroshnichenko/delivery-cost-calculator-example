# Delivery Cost Calculator Example

## Usage
Use the module [src/calculate_delivery_cost.py](src/calculate_delivery_cost.py) as a library.

An example of usage:
```python
from src.calculate_delivery_cost import (
    CargoDimensions,
    DeliveryCostCalculator,
    DeliveryLoad,
)

distance = 2
dimensions = CargoDimensions.SMALL
delivery_load = DeliveryLoad.INCREASED
is_fragile = True
result = DeliveryCostCalculator.calculate_delivery_cost(
    distance, dimensions, delivery_load, is_fragile
)
print(result) # must be 540
```

## How to run tests
### Install requirements
1. Create a virtual environment in the folder `venv`:
    ```shell
    python3 -m venv venv
    ```
2. Activate the virtual environment
    ```shell
    source venv/bin/activate
    ```
3. Install the dev requirements:
    ```shell
    python -m pip install -r requirements-dev.txt
    ```
### Run tests
Run the command
```shell
pytest
```


## Contributing

### Use linters to check code before commit
We use [isort](https://pycqa.github.io/isort/) and [black](https://pypi.org/project/black/) linters to have a consistent coding style.
We also use [pre-commit](https://pre-commit.com/) to automate checking, so you don't need to run linters yourself.
Just run once:
```shell
pip install -r requirements-dev.txt
pre-commit install
```
to set up the git hook scripts.

Then `pre-commit` will run automatically on every `git commit`

**Note** that `git commit` won't be executed if files have been changed after `pre-commit` checking. Before you run `git commit` again, you need to include changes in the commit running `git add`.
