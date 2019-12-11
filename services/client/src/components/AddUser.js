import React, { useState} from 'react'
import axios from 'axios'

function AddUser() {
    const [formDetails, setFormDetails] = useState({
        username: '',
        email: ''
    })
    const reset = () => setFormDetails(
        {
            username: '',
            email: ''
        }
    )
    const handleSubmit = event => {
        event.preventDefault()
        axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, formDetails)
        .then((res) => {
            reset()
            window.location.reload(false);
            })
        .catch((err) => { console.log(err) })
    }
    return (
        <form onSubmit={handleSubmit}>
            <div className="form-group col-md-6">
                <label htmlFor="InputUsername">Username</label>
                <input
                    value={formDetails.username}
                    onChange={event => setFormDetails({
                        ...formDetails,
                        username: event.target.value
                    })}
                    className="form-control input-lg"
                    type="text"
                    placeholder="Enter a username"
                    required
                />
            </div>
            <div className="form-group col-md-6">
                <label htmlFor="InputEmail1">Email address</label>
                <input
                    value={formDetails.email}
                    onChange={event => setFormDetails({
                        ...formDetails,
                        email: event.target.value
                    })}
                    className="form-control input-lg"
                    type="email"
                    placeholder="Enter an email address"
                    required
                />
                <br />
            <input
                type="submit"
                className="btn btn-primary btn-lg btn-block"
                value="Submit"
            />
            </div>
        </form>
    )
}

export default AddUser
