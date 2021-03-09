import React from 'react'
import { Navbar, Nav, Container } from 'react-bootstrap'
import {LinkContainer} from 'react-router-bootstrap'

function Header() {
    return (
        <div>
            <header>
            <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
                
                <Container>
                    <LinkContainer to="/">
                        <Navbar.Brand>DoggerApp</Navbar.Brand>
                    </LinkContainer>
                    
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="mr-auto">
                            <LinkContainer to="/home">
                                <Nav.Link>
                                    Home
                                </Nav.Link>

                            </LinkContainer>

                            <LinkContainer to="/login">
                                <Nav.Link>
                                    Login
                                </Nav.Link>
                            </LinkContainer>
                            
                        </Nav>
                        
                    </Navbar.Collapse>
                </Container>
                
            </Navbar>
            </header>
        </div>
    )
}

export default Header
