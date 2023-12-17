from neo4j import GraphDatabase
from datetime import datetime
import config  # Assuming your config.py contains Neo4j connection details

driver = GraphDatabase.driver(config.NEO4J_URI, auth=(
    config.NEO4J_USERNAME, config.NEO4J_PASSWORD))


def create_tscd(tscd_data):
    with driver.session() as session:
        result = session.run(
            "CREATE (n:TSCD {MATSCD: $MATSCD, TenTSCD: $TenTSCD, TT: $TT, GiaTri: $GiaTri, THSD: $THSD, NgayMua: $NgayMua, KhauHao: $KhauHao }) RETURN n",
            "match(a:TSCD{MATSCD: $MATSCD}), ("
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