from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_vbpq(vbpq_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:VBPQ {MAVBPQ: $MAVBPQ, TenVBPQ: $TenVBPQ, NgayBH: $NgayBH}) RETURN n",
            **vbpq_data.dict()
        )
        return result.single()[0]


def get_vbpq(mavbpq):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:VBPQ {MAVBPQ: $MAVBPQ}) RETURN n",
            MAVBPQ=mavbpq
        )
        return result.single()[0]


def update_vbpq(mavbpq, vbpq_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:VBPQ {MAVBPQ: $MAVBPQ}) "
            "SET n += {TenVBPQ: $TenVBPQ, NgayBH: $NgayBH "
            "RETURN n",
            MAVBPQ=mavbpq, **vbpq_data.dict()
        )
        return result.single()[0]


def delete_vbpq(mavbpq):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:VBPQ {MAVBPQ: $MAVBPQ}) DELETE n",
            MAVBPQ=mavbpq
        )
        return result.consume().counters.nodes_deleted > 0
