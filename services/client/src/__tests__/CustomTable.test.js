import React from 'react'
import renderer from 'react-test-renderer'
import { shallow } from 'enzyme'

import CustomTable from '../components/CustomTable'

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
    

test('should render CustomTable properly', () => {
    const wrapper = shallow(<CustomTable users={users}/>)
    const table = wrapper.find('tbody')
    expect(table.length).toBe(1)

})

// snapshot testing
test('renders a snapshot properly', () => {
    const tree = renderer.create(<CustomTable users={users}/>).toJSON()
    expect(tree).toMatchSnapshot()
})