import React, {useState, useCallback} from 'react';
import axios from 'axios';
import './App.css';
import AppRouter from './routes/AppRouter';
import NavBar from './components/NavBar';

function App() {
  const [title] = useState('Coding Exercise')
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
  })
  const [authentication, setAuthentication] = useState({
    isAuthenticated: false
  })

  const handleUserFormSubmit = (event) => {
    event.preventDefault()
    const formType = window.location.href.split('/').reverse()[0]
    let data = {
      email: formData.email,
      password: formData.password
    }
    if (formType === 'register') {
      data.username = formData.username
    }
    const url = `${process.env.REACT_APP_USERS_SERVICE_URL}/auth/${formType}`
    axios.post(url, data)
    .then((res) => {
      window.localStorage.setItem('authToken', res.data.auth_token)
      setFormData({
        username: '',
        email: '',
        password: ''
      })
      setAuthentication({
        isAuthenticated: true
      })
    })
    .catch((err) => { console.log(err) })
  }
  const handleFormchange = (event) => {
    const obj = {...formData}
    obj[event.target.name] = event.target.value
    setFormData(obj)
  }
  const logoutUser = useCallback(() => {
    window.localStorage.clear();
    setAuthentication({isAuthenticated: false})
  }, [])
  return (
    <div className="App">
      <NavBar
				title={title}
			/>
      <AppRouter formData={formData}
        handleUserFormSubmit={handleUserFormSubmit}
        handleFormchange={handleFormchange}
        isAuthenticated={authentication.isAuthenticated}
        logoutUser={logoutUser}
      />
    </div>
  );
}

export default App;
