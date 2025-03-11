import networkx as nx
import pandas as pd

class TemporalGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_edges_from_dataframe(self, df: pd.DataFrame):
        """
        DataFrame의 데이터를 바탕으로 간선을 추가
        """
        for _, row in df.iterrows():
            source = row["source"]
            destination = row["destination"]
            timestamp = row["timestamp"]
            self.graph.add_edge(source, destination, timestamp=timestamp)

    def get_edges_in_time_range(self, start_time: str, end_time: str):
        """
        특정 시간 범위 내의 간선들을 반환
        """
        edges_in_range = [
            (u,v,data) for u, v, data in self.graph.edges(data=True) if start_time <= data['timestamp'] <= end_time
        ]

        return edges_in_range
    
    def display_graph_info(self):
        """
        그래프의 기본 정보 출력
        """
        print(f"노드 수: {self.graph.number_of_nodes()}")
        print(f"간선 수: {self.graph.number_of_edges()}")

if __name__ == '__main__':
    from data_loader import load_data

    file_path = '../temporal_graph/data/edges.csv'
    df = load_data(file_path)
    temp_graph = TemporalGraph()
    temp_graph.add_edges_from_dataframe(df)
    temp_graph.display_graph_info()
    
    edges = temp_graph.get_edges_in_time_range('2024-03-10 10:00:00', '2024-03-11 10:00:00')
    print(f"선택된 간선 수: {len(edges)}")