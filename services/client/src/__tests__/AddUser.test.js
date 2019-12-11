import React from 'react'
import renderer from 'react-test-renderer'
import { shallow } from 'enzyme'

import AddUser from '../components/AddUser'

test('should render AddUser properly', () => {
    const wrapper = shallow(<AddUser />)
    const element = wrapper.find('form');
    expect(element.find('input').length).toBe(3)
})

// snapshot testing
test('renders a snapshot of AddUser properly', () => {
    const tree = renderer.create(<AddUser />).toJSON()
    expect(tree).toMatchSnapshot()
})
