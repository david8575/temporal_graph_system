import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    주어진 파일 경로에서 데이터를 로드하고 DataFrame으로 변환
    지원 파일 형식: CSV, JSON
    """
    if file_path.lower().endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.lower().endswith('.json'):
        data = pd.read_json(file_path)
    else:
        raise ValueError("[지원 하지 않는 파일 형식 -> CSV나 JSON 파일 형식을 이용]")
    
    required_columns = {"source", "destination", "timestamp"}
    if not required_columns.issubset(data.columns):
        raise ValueError("[필수 열 없음]")
    
    return data

if __name__ == "__main__":
    file_path = '../temporal_graph/data/edges.csv'
    df = load_data(file_path)
    print(df.head())