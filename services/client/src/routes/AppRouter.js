import React from 'react'
import { Route, Switch } from 'react-router-dom'
import About from '../components/About'
import Users from '../components/Users'


const AppRouter = () => {
    return (
        <Switch>
            <Route exact path='/' component={Users} />
            <Route exact path='/about' component={About} />
        </Switch>
    )
}

export default AppRouter
