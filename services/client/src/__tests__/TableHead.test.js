import React from 'react'
import renderer from 'react-test-renderer'
import { shallow } from 'enzyme'

import TableHead from '../components/TableHead'



test('should render TableHead properly', () => {
    const wrapper = shallow(<TableHead />)
    const head = wrapper.find('thead')
    const row = wrapper.find('tr')
    const column = wrapper.find('th')
    expect(head.length).toBe(1)
    expect(row.length).toBe(1)
    expect(column.length).toBe(5)
    expect(column.get(0).props.children).toBe('User ID')
    expect(column.get(1).props.children).toBe('Email')
    expect(column.get(2).props.children).toBe('Username')
    expect(column.get(3).props.children).toBe('Active')
    expect(column.get(4).props.children).toBe('Admin')

})

// snapshot testing
test('renders a snapshot properly', () => {
    const tree = renderer.create(<TableHead />).toJSON()
    expect(tree).toMatchSnapshot()
})