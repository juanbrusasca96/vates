import React from 'react';

const TaskContext = React.createContext({
  todos: [],
  quantity: 0,
  addTask: (task) => {},
  removeTask: (id) => {}
});

export default TaskContext;