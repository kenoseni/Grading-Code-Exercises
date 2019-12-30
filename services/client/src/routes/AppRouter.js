import React from 'react'
import { Route, Switch } from 'react-router-dom'
import About from '../components/About'
import Users from '../components/Users'
import Form from '../components/Form'
import Logout from '../components/Logout'


const AppRouter = (props) => {
    return (
        <Switch>
            <Route exact path='/' component={Users} />
            <Route exact path='/about' component={About} />
            <Route exact path='/register' render={() => (
                <Form
                    formType={'Register'}
                    formData={props.formData}
                    handleUserFormSubmit={props.handleUserFormSubmit}
                    handleFormchange={props.handleFormchange}
                    isAuthenticated={props.isAuthenticated}
                />
            )} />
            <Route exact path='/login' render={() => (
                <Form
                    formType={'Login'}
                    formData={props.formData}
                    handleUserFormSubmit={props.handleUserFormSubmit}
                    handleFormchange={props.handleFormchange}
                    isAuthenticated={props.isAuthenticated}
                />
            )} />
            <Route exact path='/logout' render={() => (
                <Logout
                    logoutUser={props.logoutUser}
                />
            )} />
        </Switch>
    )
}

export default AppRouter
