temporal_graph_project/
├── backend/          # FastAPI 백엔드
│   ├── fastapi/      # FastAPI 관련 코드 저장
│   │   ├── main.py   # FastAPI 실행 파일
│   │   ├── routes.py # API 라우트 정의
│   │   ├── graph.py  # 그래프 관리 (기존 기능 포함)
│   │   ├── database.py  # DB 연동 (선택)
│   │   ├── models.py  # 데이터 모델 정의
├── frontend/         # 프론트엔드 (추후 React 적용)
│   ├── public/       
│   ├── src/
│   ├── pages/
│   ├── components/
├── data/             # 데이터 파일 (CSV, JSON 등)
│   ├── edges.csv
├── docs/             # 프로젝트 문서
│   ├── README.md
