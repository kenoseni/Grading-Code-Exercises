import React from 'react'
import { shallow } from 'enzyme'
import App from '../App'

test('should render App without crashing', () => {
    const wrapper = shallow(<App />)
})
