import React, { useContext } from 'react'
import './expenseItem.css'
import { Button } from '@mui/material'
import ItemContext from '../../helpers/ItemContext'

export default function ExpenseItem({ item, handleClickDelete, handleClickAdd }) {

    return (
        <div className='expense-item'>
            <div>{item.name}</div>
            <div className='expense-item__description'>
                <h2>{item.description}</h2>
                <div className='expense-item__price'>{item.age}</div>
            </div>
            <Button sx={{ ml: '1%' }} variant="contained" color='error' onClick={() => handleClickDelete()}>X</Button>
            <Button sx={{ ml: '1%' }} variant="contained" onClick={handleClickAdd}>+</Button>
        </div>
    )
}
