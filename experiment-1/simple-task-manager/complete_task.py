import json
import os

def complete_task(task_id):
    """
    根据任务ID完成任务
    
    Args:
        task_id (int): 要完成的任务ID
        
    Returns:
        bool: 完成任务成功返回True，失败返回False
    """
    # 检查任务文件是否存在
    if not os.path.exists('tasks.json'):
        return False
    
    try:
        # 读取现有任务
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        
        # 查找并更新任务状态
        task_found = False
        for task in tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['completed_time'] = __import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                task_found = True
                break
        
        # 如果找到任务，保存更新后的任务列表
        if task_found:
            with open('tasks.json', 'w', encoding='utf-8') as f:
                json.dump(tasks, f, ensure_ascii=False, indent=2)
            return True
        else:
            return False
            
    except (json.JSONDecodeError, FileNotFoundError):
        # 文件损坏或不存在
        return False
    except Exception as e:
        print(f"完成任务时发生错误: {e}")
        return False