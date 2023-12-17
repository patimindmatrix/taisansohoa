from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_pb(pb_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:PB {MAPB: $MAPB, TenPB: $TePB}) RETURN n",
            **pb_data.dict()
        )
        return result.single()[0]


def get_pb(mapb):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:PB {MAPB: $MAPB}) RETURN n",
            MAPB=mapb
        )
        return result.single()[0]


def update_pb(mapb, pb_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:PB {MAPB: $MAPB}) "
            "SET n += {TenPB: $TePB} "
            "RETURN n",
            MAPB=mapb, **pb_data.dict()
        )
        return result.single()[0]


def delete_pb(mapb):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:PB {MAPB: $MAPB}) DELETE n",
            MAPB=mapb
        )
        return result.consume().counters.nodes_deleted > 0
