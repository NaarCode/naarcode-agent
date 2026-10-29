# Simplified excerpt derived from app/core/state_machine.py.
from enum import StrEnum
class TaskState(StrEnum):
    QUEUED = "QUEUED"
    RESEARCHING = "RESEARCHING"
    GENERATING = "GENERATING"
    VALIDATING = "VALIDATING"
    READY = "READY"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"

TRANSITIONS: dict[TaskState, set[TaskState]] = {
    TaskState.QUEUED: {TaskState.RESEARCHING, TaskState.CANCELLED, TaskState.FAILED},
    TaskState.RESEARCHING: {TaskState.GENERATING, TaskState.FAILED, TaskState.CANCELLED},
    TaskState.GENERATING: {TaskState.VALIDATING, TaskState.FAILED, TaskState.CANCELLED},
    TaskState.VALIDATING: {TaskState.READY, TaskState.FAILED, TaskState.CANCELLED},
    TaskState.READY: {TaskState.COMPLETED, TaskState.CANCELLED, TaskState.FAILED},
    TaskState.COMPLETED: set(),
    TaskState.FAILED: set(),
    TaskState.CANCELLED: set(),
}
def validate_transition(current: TaskState, target: TaskState) -> None:
    if target not in TRANSITIONS[current]:
        raise ValueError(f"Cannot transition {current} -> {target}")
