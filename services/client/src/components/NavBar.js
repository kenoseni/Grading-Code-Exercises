import React from 'react'
import { Navbar, Nav} from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'


const NavBar = (props) => (
    <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
        <Navbar.Brand>
            <span>{props.title}</span>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse>
            <Nav className="mr-auto">
                <LinkContainer to="/">
                    <Nav.Item>
                        Home
                    </Nav.Item>
                </LinkContainer>
                <LinkContainer to="/about">
                    <Nav.Item>
                        About
                    </Nav.Item>
                </LinkContainer>
                {
                    props.isAuthenticated &&
                    <LinkContainer to="/status">
                        <Nav.Item>
                            User Status
                        </Nav.Item>
                    </LinkContainer>
                }
            </Nav>
            <Nav>
                {
                    !props.isAuthenticated &&
                    <LinkContainer to="/register">
                        <Nav.Item>
                            Register
                        </Nav.Item>
                    </LinkContainer>
                }
                {
                    !props.isAuthenticated &&
                    <LinkContainer to="/login">
                        <Nav.Item>
                            Log In
                        </Nav.Item>
                    </LinkContainer>
                }
                {
                    props.isAuthenticated &&
                    <LinkContainer to="/logout">
                        <Nav.Item>
                            Log Out
                        </Nav.Item>
                    </LinkContainer>
                }
            </Nav>
        </Navbar.Collapse>
    </Navbar>
)

export default NavBar
