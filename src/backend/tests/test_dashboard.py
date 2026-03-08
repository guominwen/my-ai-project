from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)

def test_dashboard_stats():
    # 1. 注册测试用户
    user_resp = client.post(
        "/api/v1/auth/register",
        json={"username": "dashuser", "email": "dash@example.com", "password": "password123"}
    )
    user_id = user_resp.json()["data"]["id"]

    # 2. 创建两个任务，一个完成，一个未完成
    client.post(
        f"/api/v1/tasks/?owner_id={user_id}",
        json={"title": "Task 1", "completed": True}
    )
    client.post(
        f"/api/v1/tasks/?owner_id={user_id}",
        json={"title": "Task 2", "completed": False}
    )

    # 3. 获取统计数据
    resp = client.get(f"/api/v1/dashboard/stats?owner_id={user_id}")
    assert resp.status_code == 200
    data = resp.json()["data"]
    
    assert data["total_tasks"] == 2
    assert data["completed_tasks"] == 1
    assert data["pending_tasks"] == 1
    assert data["completion_rate"] == 50.0
