# Created by Lenovo.
# @Time : 2026/3/12 10:13
# @Author : feora
# Description here
# 从用户输入接收新任务，并保存到任务列表
# add_task.py
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """从 tasks.json 加载任务列表，如果文件不存在则返回空列表"""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []  # 如果文件损坏，当作空任务列表处理


def save_tasks(tasks):
    """将任务列表保存到 tasks.json"""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(description: str) -> None:
    """
    添加一个新任务到任务列表
    :param description: 任务描述（非空字符串）
    """
    if not description.strip():
        raise ValueError("任务描述不能为空")

    tasks = load_tasks()

    # 生成新的任务 ID：当前最大 ID + 1，若无任务则从 1 开始
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1

    new_task = {
        "id": new_id,
        "description": description.strip(),
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)