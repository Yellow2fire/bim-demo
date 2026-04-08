from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os
import random
from datetime import datetime

# 初始化Flask应用
app = Flask(__name__)
load_dotenv()

# 模拟数据库数据（实际项目替换为MySQL/PostgreSQL连接）
# 养殖车间基础信息
workshop_info = {
    "name": "6#海水养殖车间",
    "address": "浙江省海宁市",
    "area": 2000,  # 建筑面积 (㎡)
    "water_volume": 1200,  # 养殖水体 (㎡)
    "system_count": 4,  # 系统套数
    "status": "停止运营"  # 运营状态
}

# 设备数据
device_data = {
    "total": 6,  # 设备总数
    "running": 0,  # 运行数量
    "strategy_running": 0,  # 控制策略开启数
    "high_risk": [
        {"name": "制氧机 H_P1_OG1", "risk_level": 9},
        {"name": "液位探头 H_P1_LV1", "risk_level": 1}
    ]
}

# 养殖区数据
breeding_area = {
    "1#养殖区": {
        "status": "运营中",
        "fish_type": "武昌鱼",
        "stocking_amount": 50000,  # 投放量 (尾)
        "water_change_start": "2026-02-03",  # 吊水起始时间
        "expected_shipment": "2026-02-28",  # 预计出货时间
        "expected_profit": 10  # 预期收益 (万元)
    },
    "2#养殖区": {"status": "停止运营"},
    "3#养殖区": {"status": "停止运营"},
    "4#养殖区": {"status": "停止运营"}
}

# 首页路由（BIM可视化主界面）
@app.route('/')
def index():
    return render_template('index.html', 
                           workshop=workshop_info,
                           device=device_data,
                           breeding=breeding_area)

# 实时数据接口（模拟数据推送）
@app.route('/api/realtime-data')
def realtime_data():
    # 模拟实时变化的设备数据（实际项目从传感器/PLC获取）
    return jsonify({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "oxygen_machine": random.uniform(85, 95),  # 制氧机运行参数
        "level_sensor": random.uniform(0, 1),      # 液位探头数值
        "running_devices": random.randint(0, 6)    # 实时运行设备数
    })

# 风险预警接口
@app.route('/api/risk-warning')
def risk_warning():
    return jsonify(device_data["high_risk"])

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
