from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_ccdc(ccdc_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:CCDC {MACCDC: $MACCDC, TenCCDC: $TenCCDC, TT: $TT, GiaTri: $GiaTri}) RETURN n",
            **ccdc_data.dict()
        )
        return result.single()[0]


def get_ccdc(maccdc):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:CCDC {MACCDC: $MACCDC}) RETURN n",
            MACCDC=maccdc
        )
        return result.single()[0]


def update_ccdc(maccdc, ccdc_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:CCDC {MACCDC: $MACCDC}) "
            "SET n += {TenCCDC: $TenCCDC, TT: $TT, GiaTri: $GiaTri} "
            "RETURN n",
            MACCDC=maccdc, **ccdc_data.dict()
        )
        return result.single()[0]


def delete_ccdc(maccdc):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:CCDC {MACCDC: $MACCDC}) DELETE n",
            MACCDC=maccdc
        )
        return result.consume().counters.nodes_deleted > 0
