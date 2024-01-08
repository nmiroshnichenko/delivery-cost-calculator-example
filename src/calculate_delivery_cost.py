from enum import Enum, IntEnum


class Distance(IntEnum):
    SHORT = 2
    MEDIUM = 10
    LONG = 30


class DistanceCoefficient(IntEnum):
    SHORT = 50
    MEDIUM = 100
    LONG = 200
    LONGER = 300


class CargoDimensions(IntEnum):
    LARGE = 200
    SMALL = 100


class DeliveryLoad(Enum):
    NORMAL = 1
    INCREASED = 1.2
    HIGH = 1.4
    VERY_HIGH = 1.6


class DeliveryCostCalculator:
    BASE_COST = 0
    MIN_COST = 400
    FRAGILE_COST = 300

    @staticmethod
    def get_distance_coefficient(distance: int) -> DistanceCoefficient:
        if distance <= Distance.SHORT.value:
            return DistanceCoefficient.SHORT
        elif distance <= Distance.MEDIUM.value:
            return DistanceCoefficient.MEDIUM
        elif distance <= Distance.LONG.value:
            return DistanceCoefficient.LONG
        else:
            return DistanceCoefficient.LONGER

    @staticmethod
    def calculate_delivery_cost(
        distance: int,
        dimensions: CargoDimensions,
        delivery_load: DeliveryLoad,
        is_fragile: bool,
    ):
        if distance < 0:
            raise ValueError("Distance should be positive")
        if is_fragile and distance == Distance.LONG:
            raise ValueError(
                "Fragile cargo cannot be transported over a distance of more than"
                f" {Distance.LONG.value} km"
            )

        distance_cost = DeliveryCostCalculator.get_distance_coefficient(distance).value
        dimensions_cost = dimensions.value if dimensions in CargoDimensions else 0
        fragile_cost = DeliveryCostCalculator.FRAGILE_COST if is_fragile else 0
        load_coefficient = delivery_load.value if delivery_load in DeliveryLoad else 1

        delivery_cost = (
            DeliveryCostCalculator.BASE_COST
            + distance_cost
            + dimensions_cost
            + fragile_cost
        )

        delivery_cost *= load_coefficient

        delivery_cost_rounded = round(delivery_cost, 2)
        # Cast to int if there is a .0 decimal part
        delivery_cost_rounded = (
            int(delivery_cost_rounded)
            if delivery_cost_rounded % 1 == 0
            else delivery_cost_rounded
        )

        return max(delivery_cost_rounded, DeliveryCostCalculator.MIN_COST)
