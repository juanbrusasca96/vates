import { useReducer } from "react";
import TaskContext from "./task-context";

const defaulTaskState = {
    todos: [{ id: 1, title: 'hacer aplicacion de todos', complete: false }]
}


const taskReducer = (state, action) => {
    if (action.type === 'ADD') {
        let updateTask = [...state.todos, action.task];
        const updateTaskAmount = updateTask.length
        return {
            todos: updateTask,
            quantity: updateTaskAmount
        }
    }
    return defaulTaskState
}

const TaskProvider = (props) => {
    const [taskState, dispatchTaskAction] = useReducer(
        taskReducer,
        defaulTaskState
    );

    const addTaskHandler = (task) => {
        dispatchTaskAction({ type: 'ADD', task: task })
    }

    const removeTaskHandler = (id) => {
        dispatchTaskAction({ type: 'REMOVE', id: id })
    }

    const taskContext = {
        todos: taskState.todos,
        quantity: taskState.quantity,
        addTask: addTaskHandler,
        removeTask: removeTaskHandler
    }

    return (
        <TaskContext.Provider value={taskContext}>
            {props.children}
        </TaskContext.Provider>
    )
}

export default TaskProvider;
