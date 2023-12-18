from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))

def get_all_kh():
    with driver.session() as session:
        result = session.run("MATCH (n:KH) WHERE n.MAKH <> '' RETURN n")
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
    
def create_kh(kh_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:KH {MAKH: $MAKH, TenKH: $TenKH, SDT: $SDT, EMAIL: $EMAIL, MST: $MST, DC: $DC}) RETURN n",
            **kh_data.dict()
        )
        return result.single()[0]


def get_kh(makh):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:KH {MAKH: $MAKH}) RETURN n",
            MAKH=makh
        )
        return result.single()[0]


def update_kh(makh, kh_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:KH {MAKH: $MAKH}) "
            "SET n += {TenKH: $TenKH, SDT: $SDT, EMAIL: $EMAIL, MST: $MST, DC: $DC} "
            "RETURN n",
            MAKH=makh, **kh_data.dict()
        )
        return result.single()[0]


def delete_kh(makh):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:KH {MAKH: $MAKH}) DELETE n",
            MAKH=makh
        )
        return result.consume().counters.nodes_deleted > 0
