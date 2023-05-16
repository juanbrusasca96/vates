import React from 'react'
import './expenseItem.css'
import { Button } from '@mui/material'

export default function ExpenseItem({ user, handleClickDelete, handleClickAdd }) {
    return (
        <div className='expense-item'>
            <div>{user.name}</div>
            <div className='expense-item__description'>
                <h2>{user.description}</h2>
                <div className='expense-item__price'>{user.age}</div>
            </div>
            <Button sx={{ ml: '1%' }} variant="contained" color='error' onClick={()=>handleClickDelete()}>X</Button>
            <Button sx={{ ml: '1%' }} variant="contained" onClick={handleClickAdd}>+</Button>
        </div>
    )
}
