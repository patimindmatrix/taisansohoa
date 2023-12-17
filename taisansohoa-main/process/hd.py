from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_hd(hd_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:HD {MAHD: $MAHD, TenHD: $TenHD, NgayTao: $NgayTao, NgayTaiLen: $NgayTaiLen, TepDinhKem: $TepDinhKem}) RETURN n",
            **hd_data.dict()
        )
        return result.single()[0]


def get_hd(mahd):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:HD {MAHD: $MAHD}) RETURN n",
            MAHD=mahd
        )
        return result.single()[0]


def update_hd(mahd, hd_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:HD {MAHD: $MAHD}) "
            "SET n += {TenHD: $TenHD, NgayTao: $NgayTao, NgayTaiLen: $NgayTaiLen, TepDinhKem: $TepDinhKem} "
            "RETURN n",
            MAHD=mahd, **hd_data.dict()
        )
        return result.single()[0]


def delete_hd(mahd):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:HD {MAHD: $MAHD}) DELETE n",
            MAHD=mahd
        )
        return result.consume().counters.nodes_deleted > 0
