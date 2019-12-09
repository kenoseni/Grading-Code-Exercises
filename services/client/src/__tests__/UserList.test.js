import React from 'react'
import renderer from 'react-test-renderer'
import { shallow } from 'enzyme'

import User from '../components/UserList'

const user =
    {
        'active': true,
        'email': 'barry@gmail.com',
        'id': 1,
        'username': 'barry'
    }

test('should render UserList properly', () => {
    const wrapper = shallow(<User user={user}/>)
    const element = wrapper.find('h4')
    expect(element.length).toBe(1)

})

// snapshot testing
test('renders a snapshot properly', () => {
    const tree = renderer.create(<User user={user}/>).toJSON()
    expect(tree).toMatchSnapshot()
})
