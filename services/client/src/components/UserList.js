import React from 'react'

function User({user}) {
    return (
        <h4 className="card card-body bg-light">
            {user.username}
        </h4>
    )
}

export default User
