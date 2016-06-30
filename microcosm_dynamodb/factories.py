"""
Factory that configures flywheel DynamoDB ORM-like framework.

"""
from os import environ

from flywheel import Engine

from microcosm.api import defaults


@defaults(
    namespace=None,
    region=environ.get("AWS_DEFAULT_REGION"),
)
def configure_flywheel_engine(graph):
    """
    Create the flywheel engine.

    """
    namespace = graph.config.dynamodb.namespace or ()
    if graph.metadata.testing:
        namespace = "test"

    engine = Engine(namespace=namespace)
    engine.connect_to_region(graph.config.dynamodb.region)

    return engine
