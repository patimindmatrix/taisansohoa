from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))

def get_all_bb():
    with driver.session() as session:
        result = session.run("MATCH (n:BB) WHERE n.NhaBao <> '' RETURN n")
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
