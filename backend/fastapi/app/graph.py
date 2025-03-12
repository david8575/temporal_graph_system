import networkx as nx
from datetime import datetime, timedelta

class Temporalgraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_edge(self, src, des, timestamp):
        self.graph.add_edge(src, des, timestamp=timestamp)

    def get_edges(self):
        return list(self.graph.edges(data=True))
    
    def get_edges_in_time_range(self, start_time: str, end_time: str):
        """
        특정 시간 범위 내의 간선들 반환
        """
        edges_in_range = [
            (u,v,data)
            for u, v, data in self.graph.edges(data=True
                                               )
            if start_time <= data['timestamp'] <= end_time
        ]
        return edges_in_range
    
    def get_edges_with_sliding_window(self, target_time: str, window_size: int):
        """
        특정 시간에서 ±window_size 분 범위의 간선을 반환
        """
        target_time_dt = datetime.strptime(target_time, "%Y-%m-%dT%H:%M:%S")
        start_time = (target_time_dt - timedelta(minutes=window_size)).strftime("%Y-%m-%dT%H:%M:%S")
        end_time = (target_time_dt + timedelta(minutes=window_size)).strftime("%Y-%m-%dT%H:%M:%S")

        return self.get_edges_in_time_range(start_time, end_time)

    def get_exact_timestamp_edges(self, target_time: str):
        """
        정확한 타임스탬프를 가진 간선 반환
        """
        return [
            (u, v, data)
            for u, v, data in self.graph.edges(data=True)
            if data['timestamp'] == target_time
        ]    
# 전역 그래프 객체  
temporal_graph = Temporalgraph()