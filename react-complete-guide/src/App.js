import { useState } from 'react';
import './App.css';
import ExpenseItem from './components/expenseItem/ExpenseItem';
import ItemProvider from './helpers/ItemContext';
import ItemList from './components/itemsList/ItemList';
import TableBasic from '../frontend-vuexy-full/src/views/table/data-grid/TableBasic'



function App() {

  return (
    // <ItemProvider>
    //   <div className="App">
    //     <ItemList />
    //   </div>
    // </ItemProvider>
    <div className='app'>
      <TableBasic/>
    </div>
  );
}

export default App;
