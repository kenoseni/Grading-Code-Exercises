import React from 'react'
import renderer from 'react-test-renderer'
import { shallow } from 'enzyme'
import About from '../components/About'


test('should render About page properly', () => {
    const wrapper = shallow(<About/>)
    const element = wrapper.find('p')
    expect(element.length).toBe(1)
    expect(element.text()).toBe('Add something relevant here.')
})

// snapshot testing
test('renders a snapshot of About page properly', () => {
    const tree = renderer.create(<About />).toJSON()
    expect(tree).toMatchSnapshot()
})
