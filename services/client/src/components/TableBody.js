import React from 'react'

const TableBody = ({users}) => {
    const userDetails = users.map((user) => (
        <tr key={user.id}>
            <td>{user.id}</td>
            <td>{user.email}</td>
            <td>{user.username}</td>
            <td>{String(user.active)}</td>
            <td>{String(user.admin)}</td>
        </tr>)
    )
    return (
        <React.Fragment>
            {userDetails}
        </React.Fragment>  
    )
}

export default TableBody
