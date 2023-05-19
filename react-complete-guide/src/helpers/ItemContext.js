import { useReducer } from 'react';

import ItemsContext from './items-context';

const defaultItemsState = {
    items: [{ id: 1, name: 'pepito', description: 'fullstack developer', age: 26 }, { id: 2, name: 'rafa', description: 'backend developer', age: 27 }, { id: 3, name: 'gero', description: 'frontend developer', age: 24 }],
    totalAmount: 3,
};

const itemReducer = (state, action) => {
    if (action.type === 'ADD') {
        let updatedItems = [...state.items, action.item];
        const updatedTotalAmount = updatedItems.length;
        return {
            items: updatedItems,
            totalAmount: updatedTotalAmount,
        };
    }
    if (action.type === 'REMOVE') {
        let updatedItems = state.items.filter(item => item.id !== action.id);
        const updatedTotalAmount = updatedItems.length;
        return {
            items: updatedItems,
            totalAmount: updatedTotalAmount
        };
    }

    return defaultItemsState;
};

const ItemProvider = (props) => {
    const [itemsState, dispatchItemsAction] = useReducer(
        itemReducer,
        defaultItemsState
    );

    const addItemHandler = (item) => {
        dispatchItemsAction({ type: 'ADD', item: item });
    };

    const removeItemHandler = (id) => {
        dispatchItemsAction({ type: 'REMOVE', id: id });
    };

    const itemsContext = {
        items: itemsState.items,
        totalAmount: itemsState.totalAmount,
        addItem: addItemHandler,
        removeItem: removeItemHandler,
    };

    return (
        <ItemsContext.Provider value={itemsContext}>
            {props.children}
        </ItemsContext.Provider>
    );
};

export default ItemProvider;