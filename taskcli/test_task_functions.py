import pytest
from functions import (add_task, delete_task, mark_task_done, mark_task_in_progress, update_task)

database : dict[str, dict] = {}

def test_add_task() -> None:
    add_task(database, "Hello world")
    assert len(database) == 1 and database["1"]["description"] == "Hello world"

def test_update_task() -> None:
    update_task(database, "1", "Goodbye world")
    assert database["1"]["description"] == "Goodbye world"

def test_mark_in_progress() -> None:
    mark_task_in_progress(database, "1")
    assert database["1"]["status"] == "in_progress"

def test_mark_done() -> None:
    mark_task_done(database, "1")
    assert database["1"]["status"] == "done"

def test_delete_task() -> None:
    delete_task(database, "1")
    assert "1" not in database
