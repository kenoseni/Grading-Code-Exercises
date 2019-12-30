import React, {useState, useEffect} from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'


const UserStatus = (props) => {
    const [userDetail, setUserDetail] = useState({
        email: '',
        id: '',
        username: ''
    })
    useEffect(() => {
        const fetchStatus = async() => {
            const options = {
                url: `${process.env.REACT_APP_USERS_SERVICE_URL}/auth/status`,
                method: 'get',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${window.localStorage.authToken}`
                }
            }
            try {
                const res = await axios(options)
                setUserDetail({
                    email: res.data.data.email,
                    id: res.data.data.id,
                    username: res.data.data.username
                })
            }
            catch (error) {
                console.log(error)
            }
        }
        if (props.isAuthenticated) {
            fetchStatus()
        }
    }, [props.isAuthenticated])
    if (!props.isAuthenticated) {
        return (
            <p>
                You must be logged in to view this. 
                Click <Link to="/login">here</Link> to log back in
            </p>
        )
    }
    return (
        <div>
            <ul>
                <li><strong>User ID:</strong>{userDetail.id}</li>
                <li><strong>Email:</strong>{userDetail.email}</li>
                <li><strong>Username:</strong>{userDetail.username}</li>
            </ul>
        </div>
    )
}

export default UserStatus
