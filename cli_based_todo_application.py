import json
from typing import List

import typer

app = typer.Typer()

TODO_FILE = "todo_list.json"


def load_todo_list() -> List[str]:
    """할 일 목록을 파일에서 로드합니다."""
    try:
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_todo_list(todo_list: List[str]):
    """할 일 목록을 파일에 저장합니다."""
    with open(TODO_FILE, "w") as f:
        json.dump(todo_list, f, ensure_ascii=False, indent=4)


def add_task(task: str):
    """할 일을 ToDo 목록에 추가합니다."""
    todo_list = load_todo_list()
    todo_list.append(task)  # 새로운 할 일 추가
    save_todo_list(todo_list)
    typer.echo(f"할 일이 추가되었습니다: {task}")  # 사용자에게 메시지 출력


def remove_task(index: int):
    """ToDo 목록에서 특정 할 일을 제거합니다."""
    todo_list = load_todo_list()
    try:
        removed_task = todo_list.pop(index)  # 지정된 인덱스의 할 일 제거
        save_todo_list(todo_list)
        typer.echo(f"할 일이 제거되었습니다: {removed_task}")
    except IndexError:
        typer.echo("유효하지 않은 할 일 인덱스입니다")


def list_tasks():
    """ToDo 목록에 있는 모든 할 일을 나열합니다."""
    todo_list = load_todo_list()
    if todo_list:
        typer.echo("ToDo 목록:")
        for i, task in enumerate(todo_list):
            typer.echo(f"{i + 1}. {task}")
    else:
        typer.echo("ToDo 목록에 할 일이 없습니다")


@app.command()
def add(할일: str):
    """새로운 할 일을 ToDo 목록에 추가합니다."""
    add_task(할일)


@app.command()
def remove(인덱스: int):
    """ToDo 목록에서 특정 할 일을 제거합니다."""
    remove_task(인덱스 - 1)


@app.command()
def list():
    """ToDo 목록에 있는 모든 할 일을 나열합니다."""
    list_tasks()


if __name__ == "__main__":
    app()
