import React from 'react'
import CustomTable from './CustomTable'

function UserList(props) {
    return (
        <CustomTable users={props.users}/>
    )
}

export default UserList
