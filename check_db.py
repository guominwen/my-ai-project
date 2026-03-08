from sqlalchemy import create_engine, text

# 数据库连接配置 (根据 tech_stack.md)
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "todo_db"

SQLALCHEMY_BASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/"

try:
    engine = create_engine(SQLALCHEMY_BASE_URL)
    with engine.connect() as connection:
        print("--- MySQL 服务连接成功 ---")
        
        # 1. 检查所有数据库
        result = connection.execute(text("SHOW DATABASES"))
        databases = [row[0] for row in result]
        print(f"当前所有数据库: {databases}")
        
        if MYSQL_DB in databases:
            print(f"--- 找到项目库: {MYSQL_DB} ---")
            connection.execute(text(f"USE {MYSQL_DB}"))
            
            # 2. 列出所有表
            result = connection.execute(text("SHOW TABLES"))
            tables = [row[0] for row in result]
            print(f"包含的表: {tables}")
            
            # 3. 统计表数据
            for table in tables:
                count_res = connection.execute(text(f"SELECT COUNT(*) FROM {table}"))
                count = count_res.scalar()
                print(f"表 [{table}] 中的数据量: {count}")
        else:
            print(f"!!! 未找到数据库: {MYSQL_DB} !!!")
            print(f"请手动执行: CREATE DATABASE {MYSQL_DB};")
            
except Exception as e:
    print(f"--- 连接失败 ---")
    print(f"错误信息: {str(e)}")
