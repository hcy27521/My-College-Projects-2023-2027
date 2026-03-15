# @Time : 2026/3/15
# @Author : yalin
# Description: 根据任务 ID 从任务列表中删除指定任务
# delete_task.py
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """从 tasks.json 加载任务列表"""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    """将更新后的任务列表保存到 tasks.json"""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def delete_task(task_id: int) -> bool:
    """
    根据 ID 删除任务
    :param task_id: 要删除的任务 ID
    :return: 删除成功返回 True，ID 不存在返回 False
    """
    tasks = load_tasks()
    
    # 记录原始长度，用于判断是否真的删除了任务
    original_length = len(tasks)
    
    # 使用列表推导式过滤掉 ID 匹配的任务
    # 只保留 ID 不等于传入 ID 的任务
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    
    # 如果新列表长度小于原列表，说明删除了东西
    if len(updated_tasks) < original_length:
        save_tasks(updated_tasks)
        return True
    else:
        return False

