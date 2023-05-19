import React, { useContext } from 'react'
import ItemsContext from '../../helpers/items-context';
import ExpenseItem from '../expenseItem/ExpenseItem';

export default function ItemList() {
    const itemCtx = useContext(ItemsContext);

    const itemRemoveHandler = (id) => {
        itemCtx.removeItem(id);
    };

    const itemAddHandler = (item) => {
        itemCtx.addItem({ ...item, id: itemCtx.items.length + 1 });
    };

    return (
        <div>
            <h3>Cantidad de items: {itemCtx.totalAmount}</h3>
            {
                itemCtx.items.map((user, i) => <ExpenseItem key={i} item={user} handleClickDelete={() => itemRemoveHandler(user.id)} handleClickAdd={() => itemAddHandler(user)} />)
            }
        </div>
    )
}
