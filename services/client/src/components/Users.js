import React, { useState, useEffect } from 'react'
import axios from 'axios'
import UserList from './UserList'


function Users() {
	const [users, setUsers] = useState([])
	useEffect(() => {
		axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
		.then((res) => {
			setUsers(res.data.data.users) }
		)
		.catch((err) => { console.log(err) })
	}, [])
	// const userList = users.map((user) => <UserList user={user} key={user.id}/>)
	return (
		<React.Fragment>
			<div className="container">
				<div className="row">
					<div className="col-md-6">
						<br />
							<h1>All users</h1>
						<hr /><br />
						<br />
							<UserList users={users}/>
						<br />
					</div>
				</div>		
			</div>
		</React.Fragment>
	)
}
export default Users
