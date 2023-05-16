import { useState } from 'react';
import './App.css';
import ExpenseItem from './components/ExpenseItem';



function App() {
  const [deleted, setDeleted] = useState([])
  const [listOfUsers, setListOfUsers] = useState([{ id: 1, name: 'pepito', description: 'fullstack developer', age: 26 }, { id: 2, name: 'rafa', description: 'backend developer', age: 27 }, { id: 3, name: 'gero', description: 'frontend developer', age: 24 }])

  const handleClickDelete = (i) => {
    setDeleted([...deleted, i])
  }

  const handleClickAdd = (user) => {
    setListOfUsers([...listOfUsers, { ...user, id: listOfUsers.length + 1 }])
  }

  return (
    <div className="App">
      {
        listOfUsers.filter((user, i) => !deleted.includes(i + 1)).map((user, i) => <ExpenseItem key={i} user={user} handleClickDelete={() => handleClickDelete(user.id)} handleClickAdd={() => handleClickAdd(user)} />)
      }
      todos[todoIndex]={...todoDoneUpdate, done:true}
      setTodos([...todos])
    </div>
  );
}

export default App;
