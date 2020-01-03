import React from 'react'
import renderer from 'react-test-renderer'
import { shallow } from 'enzyme'

import Users from '../components/Users'



test('should render Users properly', () => {
    const wrapper = shallow(<Users />)
    const element = wrapper.find('h1')
    expect(element.length).toBe(1)
    expect(element.get(0).props.children).toBe('All users')

})

// snapshot testing
test('renders a snapshot properly', () => {
    const tree = renderer.create(<Users />).toJSON()
    expect(tree).toMatchSnapshot()
})