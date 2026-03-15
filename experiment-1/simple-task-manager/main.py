# Created by Lenovo.
# @Time : 2026/3/12 10:11
# @Author : feora
# Description here
# main.py
from add_task import add_task
from view_tasks import view_tasks
from complete_task import complete_task
from delete_task import delete_task

def main():
    while True:
        print("\n=== 简易任务管理器 ===")
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 完成任务")
        print("4. 删除任务")
        print("0. 退出")
        choice = input("请选择操作: ").strip()

        if choice == '1':
            desc = input("请输入任务描述: ")
            add_task(desc)
            print("✅ 任务已添加！")
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                tid = int(input("请输入要完成的任务ID: "))
                if complete_task(tid):
                    print("✅ 任务已完成！")
                else:
                    print("❌ 任务ID不存在！")
            except ValueError:
                print("⚠️ 请输入有效数字！")
        elif choice == '4':
            try:
                tid = int(input("请输入要删除的任务ID: "))
                if delete_task(tid):
                    print("🗑️ 任务已删除！")
                else:
                    print("❌ 任务ID不存在！")
            except ValueError:
                print("⚠️ 请输入有效数字！")
        elif choice == '0':
            print("👋 再见！")
            break
        else:
            print("⚠️ 无效选项，请重试。")

if __name__ == "__main__":
    main()