from sqlalchemy import create_engine, text
from src.backend.core.database import Base, engine
from src.backend.models.user import User
from src.backend.models.task import Task

# 1. 连接到 MySQL (不指定数据库) 以创建数据库
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "todo_db"

# 使用无数据库连接
base_url = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/"
temp_engine = create_engine(base_url)

try:
    with temp_engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"))
        conn.commit()
        print(f"--- 数据库 {MYSQL_DB} 已准备就绪 ---")

    # 2. 使用 SQLAlchemy 自动创建所有表
    print("正在创建数据表...")
    Base.metadata.create_all(bind=engine)
    print("--- 数据表 (users, tasks) 已成功创建 ---")

    # 3. 验证
    with engine.connect() as conn:
        result = conn.execute(text("SHOW TABLES"))
        tables = [row[0] for row in result]
        print(f"最终数据库中的表: {tables}")

except Exception as e:
    print(f"!!! 初始化失败: {str(e)}")
