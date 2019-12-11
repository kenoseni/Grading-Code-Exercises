import React from 'react';
import './App.css';
import Users from './components/Users'
import AddUser from './components/AddUser';

function App() {
  return (
    <div className="App">
      <AddUser />
      <Users />
    </div>
  );
}

export default App;
