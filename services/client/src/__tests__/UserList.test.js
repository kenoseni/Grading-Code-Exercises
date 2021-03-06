import React from 'react'
import renderer from 'react-test-renderer'
import { shallow } from 'enzyme'

import UserList from '../components/UserList'

const users = [
    {   
        'admin': false,
        'active': true,
        'email': 'barry@gmail.com',
        'id': 1,
        'username': 'barry'
    },
    {   'admin': false,
        'active': true,
        'email': 'barry@gmail.com',
        'id': 2,
        'username': 'barry'
    }

]
    

test('should render UserList properly', () => {
    const wrapper = shallow(<UserList users={users}/>)

})

// snapshot testing
test('renders a snapshot properly', () => {
    const tree = renderer.create(<UserList users={users}/>).toJSON()
    expect(tree).toMatchSnapshot()
})
