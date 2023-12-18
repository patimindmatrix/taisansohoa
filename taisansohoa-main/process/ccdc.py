from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))

def get_all_ccdc():
    with driver.session() as session:
        result = session.run("MATCH (n:CCDC) WHERE n.MACCDC <> '' RETURN n")
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
