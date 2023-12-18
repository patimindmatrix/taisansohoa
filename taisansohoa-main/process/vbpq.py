from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))

def get_all_vbpq():
    with driver.session() as session:
        result = session.run("MATCH (n:VBPQ) WHERE n.MAVBPQ <> '' RETURN n")
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

def create_vbpq(vbpq_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:VBPQ {MAVBPQ: $MAVBPQ, TenVBPQ: $TenVBPQ, NgayBH: $NgayBH}) RETURN n",
            **vbpq_data.dict()
        )
        return result.single()[0]


def get_vbpq(mavbpq):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:VBPQ {MAVBPQ: $MAVBPQ}) RETURN n",
            MAVBPQ=mavbpq
        )
        return result.single()[0]


def update_vbpq(mavbpq, vbpq_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:VBPQ {MAVBPQ: $MAVBPQ}) "
            "SET n += {TenVBPQ: $TenVBPQ, NgayBH: $NgayBH "
            "RETURN n",
            MAVBPQ=mavbpq, **vbpq_data.dict()
        )
        return result.single()[0]


def delete_vbpq(mavbpq):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:VBPQ {MAVBPQ: $MAVBPQ}) DELETE n",
            MAVBPQ=mavbpq
        )
        return result.consume().counters.nodes_deleted > 0
