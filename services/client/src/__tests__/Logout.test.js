import React from 'react'
import { shallow } from 'enzyme'
import renderer from 'react-test-renderer'
import { MemoryRouter as Router } from 'react-router-dom';

import Logout from '../components/Logout'

const logoutUser = jest.fn()


test('should render Logout properly', () => {
    const wrapper = shallow(<Logout logoutUser={logoutUser} />)
    const element = wrapper.find('p')
    expect(element.length).toBe(1)
    expect(element.get(0).props.children[0]).toContain(
        'You are now logged out.'
    )
})

test('should render Logout snapshot properly', () => {
    const tree = renderer.create(
        <Router location="/logout"><Logout logoutUser={logoutUser}/></Router>
    ).toJSON()
    expect(tree).toMatchSnapshot()
})

