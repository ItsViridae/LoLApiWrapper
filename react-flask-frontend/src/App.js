import React, { useState, useEffect }from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [ GameData, setGameData ] = useState()

  useEffect(() => {
    fetch('/api/game').then(response => response.json()).then(data => {
      console.log(data.game);
      setGameData(data.game);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          This is your Api Call: {GameData}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
