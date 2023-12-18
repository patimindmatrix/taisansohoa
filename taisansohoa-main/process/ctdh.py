from neo4j import GraphDatabase
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))

def get_all_cdth():
    with driver.session() as session:
        result = session.run("MATCH (n:CDTH) RETURN n")
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

def create_ctdh(ctdh_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:CTDH {MACTDH: $MACTDH, SL: $SL}) RETURN n",
            **ctdh_data.dict()
        )
        return result.single()[0]


def get_ctdh(mactdh):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:CTDH {MACTDH: $MACTDH}) RETURN n",
            MACTDH=mactdh
        )
        return result.single()[0]


def update_ctdh(mactdh, ctdh_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:CTDH {MACTDH: $MACTDH}) "
            "SET n += {SL: $SL} "
            "RETURN n",
            MACTDH=mactdh, **ctdh_data.dict()
        )
        return result.single()[0]


def delete_ctdh(mactdh):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:CTDH {MACTDH: $MACTDH}) DELETE n",
            MACTDH=mactdh
        )
        return result.consume().counters.nodes_deleted > 0
