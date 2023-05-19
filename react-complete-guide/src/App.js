import { useState } from 'react';
import './App.css';
import ExpenseItem from './components/expenseItem/ExpenseItem';
import ItemProvider from './helpers/ItemContext';
import ItemList from './components/itemsList/ItemList';



function App() {

  return (
    <ItemProvider>
      <div className="App">
        <ItemList />
      </div>
    </ItemProvider>

  );
}

export default App;
