from fastapi import APIRouter
from app.graph import temporal_graph

graph_router = APIRouter()

@graph_router.get("/getgraph")
def get_graph():
    return {"edges": temporal_graph.get_edges()}

@graph_router.post("/addedge")
def add_edge(src: str, des: str, timestamp: str):
    temporal_graph.add_edge(src, des, timestamp)
    return {"message": "edge added successfully"}

@graph_router.get("/filteredges")
def filter_edges(start_time: str, end_time: str):
    edges = temporal_graph.get_edges_in_time_range(start_time, end_time)
    return {"filtered_edges": edges}

@graph_router.get("/slidingwindow")
def sliding_window(target_time: str, window_size: int):
    edges = temporal_graph.get_edges_with_sliding_window(target_time, window_size)
    return {"sliding_window_edges": edges}

@graph_router.get("/exacttimestamp")
def exact_timestamp(target_time: str):
    edges = temporal_graph.get_exact_timestamp_edges(target_time)
    return {"exact_edges": edges}
