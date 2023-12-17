from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_ctdh(ctdh_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:CTDH {MACTDH: $MACTDH, SL: $SL}) RETURN n",
            **ctdh_data.dict()
        )
        return result.single()[0]


def get_ctdh(mactdh):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:CTDH {MACTDH: $MACTDH}) RETURN n",
            MACTDH=mactdh
        )
        return result.single()[0]


def update_ctdh(mactdh, ctdh_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:CTDH {MACTDH: $MACTDH}) "
            "SET n += {SL: $SL} "
            "RETURN n",
            MACTDH=mactdh, **ctdh_data.dict()
        )
        return result.single()[0]


def delete_ctdh(mactdh):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:CTDH {MACTDH: $MACTDH}) DELETE n",
            MACTDH=mactdh
        )
        return result.consume().counters.nodes_deleted > 0
