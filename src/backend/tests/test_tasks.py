import pytest
from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)

def test_task_lifecycle():
    # 1. 创建一个测试用户 (用于关联任务)
    user_resp = client.post(
        "/api/v1/auth/register",
        json={"username": "taskuser", "email": "task@example.com", "password": "password123"}
    )
    user_id = user_resp.json()["data"]["id"]

    # 2. 创建任务
    create_resp = client.post(
        f"/api/v1/tasks/?owner_id={user_id}",
        json={"title": "Test Task", "description": "This is a test task"}
    )
    assert create_resp.status_code == 200
    task_id = create_resp.json()["data"]["id"]
    assert create_resp.json()["data"]["title"] == "Test Task"

    # 3. 读取任务列表
    list_resp = client.get(f"/api/v1/tasks/?owner_id={user_id}")
    assert list_resp.status_code == 200
    assert len(list_resp.json()["data"]) >= 1

    # 4. 更新任务
    update_resp = client.put(
        f"/api/v1/tasks/{task_id}",
        json={"completed": True, "title": "Updated Task"}
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["data"]["completed"] is True
    assert update_resp.json()["data"]["title"] == "Updated Task"

    # 5. 删除任务
    delete_resp = client.delete(f"/api/v1/tasks/{task_id}")
    assert delete_resp.status_code == 200
    assert delete_resp.json()["data"] is True

    # 6. 验证任务已删除
    check_resp = client.get(f"/api/v1/tasks/?owner_id={user_id}")
    # 查找刚才删除的 ID 是否还在列表中
    task_ids = [t["id"] for t in check_resp.json()["data"]]
    assert task_id not in task_ids
