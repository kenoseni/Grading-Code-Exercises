import React, { useState, useEffect } from 'react'
import axios from 'axios'
import UserList from './UserList'
import AddUser from './AddUser';

function Users() {
	const [users, setUsers] = useState([])
	useEffect(() => {
		axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
		.then((res) => {
			setUsers(res.data.data.users) }
		)
		.catch((err) => { console.log(err) })
	}, [])
	const userList = users.map((user) => <UserList user={user} key={user.id}/>)
	return (
			<div className="container">
				<div className="row">
					<div className="col-md-4">
						<br />
           				 <h1>All users</h1>
            			<hr /><br />
						<AddUser />
						<br />
							{userList}
						<br />
					</div>
				</div>		
			</div>
	)
}
export default Users
