from mongoengine import connect, disconnect
import pytest
from user_manager.mongoengine import MongoUserManager, Permission

@pytest.fixture(autouse=True)
def run_around_tests():
    connect('mongoenginetest', host='mongomock://localhost')
    yield
    disconnect()


def test_grant():
    um = MongoUserManager()
    assert Permission.objects.count() == 0
    um.grant(role="pepe", resource="item", permission="buy")
    assert Permission.objects.count() == 1
    um.grant(role="pepe", resource="item", permission="sell", namespace="sellers")
    assert Permission.objects.count() == 2
    um.grant(role="other_role", resource="item", permission="sell", namespace="sellers")
    um.grant(role="seller", resource="item", permission="sell")
    um.grant(role="seller", resource="item", permission="sell", resource_id="theid")
    um.grant(role="seller", resource="item", permission="sell", resource_id="theid", namespace="sellers")
    um.grant(role="seller", resource="item", permission="sell_seller", resource_id="theid", namespace="sellers")

    assert um.is_granted(role="pepe", resource="item", permission="buy")
    assert not um.is_granted(role="pepe", resource="item2", permission="buy")
    assert not um.is_granted(role="joseluis", resource="item", permission="buy")

    assert not um.is_granted(role="pepe", resource="item", permission="sell")
    assert um.is_granted(role="pepe", resource="item", permission="sell", namespace="sellers")

    assert not um.is_granted(role="pepe", resource="item", permission="buy", resource_id="theid")
    assert not um.is_granted(role="seller", resource="item", permission="buy", resource_id="theid")
    assert um.is_granted(role="seller", resource="item", permission="sell", resource_id="theid", namespace="sellers")
    assert um.is_granted(role="seller", resource="item", permission="sell_seller", resource_id="theid", namespace="sellers")

    # Multiroles
    assert um.is_granted(role=["pepe"], resource="item", permission="buy")
    assert um.is_granted(role=["pepe", "toto"], resource="item", permission="buy")
    assert not um.is_granted(role=["tutu", "toto"], resource="item", permission="buy")
    assert not um.is_granted(role=[], resource="item", permission="buy")

    # Get elements
    assert um.get_granted(role="pepe", namespace=None).count() == 2
    assert um.get_granted(role="pepe", namespace="sellers").count() == 1
    assert um.get_granted(namespace="sellers").count() == 4


