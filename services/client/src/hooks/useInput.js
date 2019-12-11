import {useState} from 'react'

function useInput(intialValue) {
    const [value, setValue] = useState(intialValue)
    const reset = () => setValue(intialValue)
    const bind = {
        onChange: event => {
            setValue(value => (
                {
                    ...value,
                    [event.target.name]: event.target.value
                }
            ))
        }
    }
    return [value, bind, reset]
}

export default useInput
