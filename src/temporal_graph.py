import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

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
    
    def get_edges_with_sliding_window(self, target_time: str, window_size: int):
        """
        target_time을 중심으로 ±window_size 분의 간선을 반환.
        시간 형식: 'YYYY-MM-DD HH:MM:SS'
        """
        target_time_dt = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
        start_time = (target_time_dt - timedelta(minutes=window_size)).strftime("%Y-%m-%d %H:%M:%S")
        end_time = (target_time_dt + timedelta(minutes=window_size)).strftime("%Y-%m-%d %H:%M:%S")

        return self.get_edges_in_time_range(start_time, end_time)

    def get_exact_timestamp_edges(self, target_time: str):
        """
        정확한 타임스탬프를 가진 간선 반환.
        """
        return [
            (u, v, data)
            for u, v, data in self.graph.edges(data=True)
            if data['timestamp'] == target_time
        ]
    
    def display_graph_info(self):
        """
        그래프의 기본 정보 출력
        """
        print(f"노드 수: {self.graph.number_of_nodes()}")
        print(f"간선 수: {self.graph.number_of_edges()}")

    def visualize_graph(self, show_labels=True):
        """
        그래프를 시각화하는 함수
        """
        plt.figure(figsize=(12,8))
        pos = nx.spring_layout(self.graph,k=1.0)
        nx.draw(self.graph, pos, with_labels=False, node_color='lightblue', edge_color='gray', node_size=100)
        nx.draw_networkx_labels(self.graph, pos, font_size=8)
        
        if show_labels:
            edge_labels = {(u, v): data['timestamp'] for u, v, data in self.graph.edges(data=True)}
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_size=2)

        plt.title("Temporal Graph Visualization")
        plt.show()
    
    def add_edge_from_user(self):
        """
        사용자가 직접 데이터를 추가하는 함수
        """
        print("[새로운 간선을 추가하려면 source, target, timestamp을 입력]")
        print("[입력을 끝내려면 '끝'을 입력]")
    
        while True:
            user_input = input("입력: ")
            if user_input.lower() == "끝":
                break

            try:
                source, target, timestamp = user_input.split()
                self.graph.add_edge(source, target, timestamp=timestamp)
                print(f"[추가됨: {source} -> {target} ({timestamp})]")
            except ValueError:
                print("[형식이 잘못됨]")

        print("[모든 사용자 입력이 완료]")

if __name__ == '__main__':
    from data_loader import load_data

    file_path = '../temporal_graph/data/edges.csv'
    df = load_data(file_path)
    temp_graph = TemporalGraph()
    temp_graph.add_edges_from_dataframe(df)
    temp_graph.display_graph_info()
    
    edges = temp_graph.get_edges_in_time_range('2024-03-10 10:00:00', '2024-03-11 10:00:00')
    print(f"선택된 간선 수: {len(edges)}")
