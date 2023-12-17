from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_tl(tl_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:TL {MATL: $MATL, TenTL: $TenTL, NgayTaiLen: $NgayTaiLen, TepDinhKem: $TepDinhKem}) RETURN n",
            **tl_data.dict()
        )
        return result.single()[0]


def get_tl(matl):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:TL {MATL: $MATL}) RETURN n",
            MATL=matl
        )
        return result.single()[0]


def update_tl(matl, tl_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:TL {MATL: $MATL}) "
            "SET n += {TenTL: $TenTL, NgayTaiLen: $NgayTaiLen, TepDinhKem: $TepDinhKem} "
            "RETURN n",
            MATL=matl, **tl_data.dict()
        )
        return result.single()[0]


def delete_tl(matl):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:TL {MATL: $MATL}) DELETE n",
            MATL=matl
        )
        return result.consume().counters.nodes_deleted > 0
