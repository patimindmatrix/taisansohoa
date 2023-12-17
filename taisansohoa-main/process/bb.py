from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_bb(bb_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:BB {MABB: $MABB, TenBB: $TenBB, NgayViet: $NgayViet, NhaBao: $NhaBao, LinkBB: $LinkBB}) RETURN n",
            **bb_data.dict()
        )
        return result.single()[0]


def get_bb(mabb):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:BB {MABB: $MABB}) RETURN n",
            MABB=mabb
        )
        return result.single()[0]


def update_bb(mabb, bb_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:BB {MABB: $MABB}) "
            "SET n += {TenBB: $TenBB, NgayViet: $NgayViet, NhaBao: $NhaBao, LinkBB: $LinkBB} "
            "RETURN n",
            MABB=mabb, **bb_data.dict()
        )
        return result.single()[0]


def delete_bb(mabb):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:BB {MABB: $MABB}) DELETE n",
            MABB=mabb
        )
        return result.consume().counters.nodes_deleted > 0
