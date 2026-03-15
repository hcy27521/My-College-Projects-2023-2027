# Created by Lenovo.
# @Time : 2026/3/12
# @Author : feora
# Description here
# 查看任务列表，区分完成/未完成状态
# view_tasks.py
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """从 tasks.json 加载任务列表，文件不存在/损坏则返回空列表"""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def view_tasks() -> None:
    """格式化展示所有任务，标注完成/未完成状态"""
    tasks = load_tasks()
    if not tasks:
        print("暂无任务，快来添加第一个任务吧！")
        return
    
    print("\n======= 我的任务列表 =======")
    for task in tasks:
        # 纯文字状态标识，移除图形符号
        status = "已完成" if task["completed"] else "未完成"
        print(f"ID: {task['id']} | {status} | 描述: {task['description']}")
    print("===========================\n")

if __name__ == "__main__":
    view_tasks()