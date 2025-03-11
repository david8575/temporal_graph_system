from data_loader import load_data
from temporal_graph import TemporalGraph

def main():
    file_path = '../temporal_graph/data/edges.csv'
    print("[1] 데이터 로딩 중...")
    df = load_data(file_path)
    print(f"데이터 로딩 완료: {len(df)}개의 간선 로드")
    
    print("[2] 템포럴 그래프 생성 중...")
    temp_graph = TemporalGraph()
    temp_graph.add_edges_from_dataframe(df)
    temp_graph.display_graph_info()
    
    print("[3] 특정 시간 범위의 간선 출력")
    start_time = '2024-03-10 10:00:00'
    end_time = '2024-03-11 10:00:00'
    edges = temp_graph.get_edges_in_time_range(start_time, end_time)
    print(f"선택된 간선 수: {len(edges)}")
    for edge in edges[:10]:
        print(edge)

    print("[4] 시간 필터링 기능 테스트")
    print("슬라이딩 윈도우 테스트 (±10분)")
    edges = temp_graph.get_edges_with_sliding_window('2024-03-10 10:30:00', 10)
    print(f"선택된 간선 수: {len(edges)}")

    print("[5] 정확한 타임스탬프 검색")
    exact_edges = temp_graph.get_exact_timestamp_edges('2024-03-10 10:30:00')
    print(f"정확한 시간 일치 간선 수: {len(exact_edges)}")

if __name__ == '__main__':
    main()
    