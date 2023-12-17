from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_sp(sp_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:SP {MASP: $MASP, TenSP: $TenSP, DVT: $DVT, DG: $DG}) RETURN n",
            **sp_data.dict()
        )
        return result.single()[0]


def get_s(masp):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:SP {MASP: $MASP}) RETURN n",
            MASP=masp
        )
        return result.single()[0]


def update_sp(masp, sp_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:SP {MASP: $MASP}) "
            "SET n += {TenSP: $TenSP, DVT: $DVT, DG: $DG} "
            "RETURN n",
            MASP=masp, **sp_data.dict()
        )
        return result.single()[0]


def delete_sp(masp):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:SP {MASP: $MASP}) DELETE n",
            MASP=masp
        )
        return result.consume().counters.nodes_deleted > 0
