import sys

import pytest

from src.calculate_delivery_cost import (
    CargoDimensions,
    DeliveryCostCalculator,
    DeliveryLoad,
    Distance,
)

DISTANCE_OVERLIMIT_MESSAGE = (
    "Fragile cargo cannot be transported over a distance of more than"
    f" {Distance.LONG.value} km"
)


@pytest.mark.parametrize(
    "distance, dimensions, delivery_load, is_fragile, expected_cost",
    [
        # Pairwise cases
        (
            2,
            CargoDimensions.LARGE,
            DeliveryLoad.NORMAL,
            False,
            DeliveryCostCalculator.MIN_COST,
        ),
        (
            2,
            CargoDimensions.SMALL,
            DeliveryLoad.INCREASED,
            True,
            540,
        ),
        (
            2,
            CargoDimensions.LARGE,
            DeliveryLoad.HIGH,
            False,
            DeliveryCostCalculator.MIN_COST,
        ),
        (
            2,
            CargoDimensions.SMALL,
            DeliveryLoad.VERY_HIGH,
            True,
            720,
        ),
        (
            10,
            CargoDimensions.SMALL,
            DeliveryLoad.HIGH,
            True,
            700,
        ),
        (
            10,
            CargoDimensions.LARGE,
            DeliveryLoad.VERY_HIGH,
            False,
            480,
        ),
        (
            10,
            CargoDimensions.SMALL,
            DeliveryLoad.NORMAL,
            True,
            500,
        ),
        (
            10,
            CargoDimensions.LARGE,
            DeliveryLoad.INCREASED,
            False,
            DeliveryCostCalculator.MIN_COST,
        ),
        (
            30,
            CargoDimensions.LARGE,
            DeliveryLoad.NORMAL,
            False,
            DeliveryCostCalculator.MIN_COST,
        ),
        (
            30,
            CargoDimensions.SMALL,
            DeliveryLoad.INCREASED,
            True,
            DISTANCE_OVERLIMIT_MESSAGE,
        ),
        (
            30,
            CargoDimensions.LARGE,
            DeliveryLoad.HIGH,
            False,
            560,
        ),
        (
            30,
            CargoDimensions.SMALL,
            DeliveryLoad.VERY_HIGH,
            True,
            DISTANCE_OVERLIMIT_MESSAGE,
        ),
        (
            100,
            CargoDimensions.SMALL,
            DeliveryLoad.HIGH,
            True,
            980,
        ),
        (
            100,
            CargoDimensions.LARGE,
            DeliveryLoad.VERY_HIGH,
            False,
            800,
        ),
        (
            100,
            CargoDimensions.SMALL,
            DeliveryLoad.NORMAL,
            True,
            700,
        ),
        (
            100,
            CargoDimensions.LARGE,
            DeliveryLoad.INCREASED,
            False,
            600,
        ),
        # Positive boundaries cases
        (
            0,
            CargoDimensions.SMALL,
            DeliveryLoad.NORMAL,
            False,
            DeliveryCostCalculator.MIN_COST,
        ),
        (
            2.00000001,
            CargoDimensions.LARGE,
            DeliveryLoad.VERY_HIGH,
            False,
            480,
        ),
        (
            sys.float_info.max,
            CargoDimensions.LARGE,
            DeliveryLoad.VERY_HIGH,
            True,
            1280,
        ),
        # Negative boundaries cases
        (
            -1,
            CargoDimensions.SMALL,
            DeliveryLoad.NORMAL,
            False,
            "Distance should be positive",
        ),
    ],
)
def test_calculate_delivery_cost(
    distance, dimensions, delivery_load, is_fragile, expected_cost
):
    if type(expected_cost) is str:
        with pytest.raises(
            ValueError,
            match=expected_cost,
        ):
            DeliveryCostCalculator.calculate_delivery_cost(
                distance, dimensions, delivery_load, is_fragile
            )
    else:
        actual = DeliveryCostCalculator.calculate_delivery_cost(
            distance, dimensions, delivery_load, is_fragile
        )
        assert actual == expected_cost
