from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_nvl(nvl_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:NVL {MANVL: $MANVL, TenNVL: $TenNVL, DVT: $DVT, DG: $DG}) RETURN n",
            **nvl_data.dict()
        )
        return result.single()[0]


def get_nvl(manvl):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:NVL {MANVL: $MANVL}) RETURN n",
            MANVL=manvl
        )
        return result.single()[0]


def update_nvl(manvl, nvl_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:NVL {MANVL: $MANVL}) "
            "SET n += {TenNVL: $TenNVL, DVT: $DVT, DG: $DG} "
            "RETURN n",
            MATSCD=manvl, **nvl_data.dict()
        )
        return result.single()[0]


def delete_nvl(manvl):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:NVL {MANVL: $MANVL}) DELETE n",
            MANVL=manvl
        )
        return result.consume().counters.nodes_deleted > 0
