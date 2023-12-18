from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))

def get_all_pb():
    with driver.session() as session:
        result = session.run("MATCH (n:PB) WHERE n.MAPB <> '' RETURN n")
        data = result.data()

        # Xử lý dữ liệu trả về từ Neo4j
        processed_data = []
        for record in data:
            nv_node = record['n']

            # Thay thế giá trị None bằng chuỗi rỗng
            processed_nv = {key: value if value is not None else '' for key, value in nv_node.items()}

            processed_data.append(processed_nv)
        
        print(processed_data)

        return processed_data

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
