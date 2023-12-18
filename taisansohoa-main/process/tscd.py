from neo4j import GraphDatabase
from datetime import datetime
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))

def get_all_tscd():
    with driver.session() as session:
        result = session.run("MATCH (n:TSCD) WHERE n.MATSCD <> '' RETURN n")
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

def create_tscd(tscd_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:TSCD {MATSCD: $MATSCD, TenTSCD: $TenTSCD, TT: $TT, GiaTri: $GiaTri, THSD: $THSD, NgayMua: $NgayMua, KhauHao: $KhauHao }) RETURN n",
            **tscd_data.dict()
        )
        return result.single()[0]

def get_tscd(matscd):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:TSCD {MATSCD: $MATSCD}) RETURN n",
            MATSCD=matscd
        )
        return result.single()[0]


def update_tscd(matscd, tscd_data):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:TSCD {MATSCD: $MATSCD}) "
            "SET n += {TenTSCD: $TenTSCD, TT: $TT, GiaTri: $GiaTri, THSD: $THSD, NgayMua: $NgayMua, KhauHao: $KhauHao} "
            "RETURN n",
            MATSCD=matscd, **tscd_data.dict()
        )
        return result.single()[0]


def delete_tscd(matscd):
    with driver.session() as session:
        result = session.run(
            "MATCH (n:TSCD {MATSCD: $MATSCD}) DELETE n",
            MATSCD=matscd
        )
        return result.consume().counters.nodes_deleted > 0

# def khau_Hao(ngayHienTai, tscd_data):
#     ngayHienTai = datetime.now().year
#     if ngayHienTai <= NgayMua: $NgayMua