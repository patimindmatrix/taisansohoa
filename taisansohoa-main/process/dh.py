from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_dh(dh_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:DH {MADH: $MADH, NgayTao: $NgayTao, TongTien: $TongTien}) RETURN n",
            **dh_data.dict()
        )
        return result.single()[0]


def get_dh(madh):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:DH {MADH: $MADH}) RETURN n",
            MADH=madh
        )
        return result.single()[0]


def update_dh(madh, dh_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:DH {MADH: $MADH}) "
            "SET n += {NgayTao: $NgayTao, TongTien: $TongTien} "
            "RETURN n",
            MADH=madh, **dh_data.dict()
        )
        return result.single()[0]


def delete_dh(madh):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:DH {MADH: $MADH}) DELETE n",
            MADH=madh
        )
        return result.consume().counters.nodes_deleted > 0
