from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_nv(nv_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:NV {MANV: $MANV, TenNV: $TenNV, SDT: $SDT, EMAIL: $EMAIL, STKNH: $STKNH, DC: $DC}) RETURN n",
            "match (a:NV{MANV:$MANV}),(b:PB{MAPB:PBSX}) create (a) -[:belong_to]->(b)"
            **nv_data.dict()
        )
        return result.single()[0]


def get_nv(manv):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:NV {MANV: $MANV}) RETURN n",
            MANV=manv
        )
        return result.single()[0]


def update_nv(manv, nv_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:NCC {MANV: $MANV}) "
            "SET n += {TenNV: $TenNV, SDT: $SDT, EMAIL: $EMAIL, STKNH: $STKNH, DC: $DC} "
            "RETURN n",
            MANV=manv, **nv_data.dict()
        )
        return result.single()[0]


def delete_nv(manv):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:NV {MANV: $MANV}) DELETE n",
            MANV=manv
        )
        return result.consume().counters.nodes_deleted > 0
