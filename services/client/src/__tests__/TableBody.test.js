import React from 'react'
import renderer from 'react-test-renderer'
import { shallow } from 'enzyme'

import TableBody from '../components/TableBody'

const users = [
    {   
        'admin': false,
        'active': true,
        'email': 'maggie@gmail.com',
        'id': 1,
        'username': 'maggie'
    },
    {   'admin': false,
        'active': true,
        'email': 'barry@gmail.com',
        'id': 2,
        'username': 'barry'
    }

]


test('should render TableBody properly', () => {
    const wrapper = shallow(<TableBody users={users}/>)
    const row = wrapper.find('tr')
    const td = wrapper.find('td')
    expect(row.length).toBe(2)
    expect(td.length).toBe(10)
    expect(td.get(0).props.children).toBe(1)
    expect(td.get(1).props.children).toBe('maggie@gmail.com')
    expect(td.get(5).props.children).toBe(2)
    expect(td.get(6).props.children).toBe('barry@gmail.com')

})

// snapshot testing
test('renders a snapshot properly', () => {
    const tree = renderer.create(<TableBody users={users}/>).toJSON()
    expect(tree).toMatchSnapshot()
})