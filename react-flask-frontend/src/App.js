import React, { useState, useEffect }from 'react';
import logo from './logo.svg';
import mockGameData from './mockGameData.json'
import './App.css';

function App() {
  const [ GameData, setGameData ] = useState([])
  const [ mockObject, setMockObject ] = useState([mockGameData])

  // useEffect(() => {
  //   fetch('/api/game')
  //     .then(response => response.json())
  //     .then(data => {
  //       console.log(data);
  //       setGameData(data);
  //     });
  // }, []);

  function BuildMap_FromObject(valueObject){
      const result = Object.entries(valueObject);
      console.log(result)
      return result
  }
    //may have to return
  
  function CheckIfObjectInsideData(mockObject){
    for(let obj of mockObject){
      if(typeof obj !== Array.isArray()){
       //Do some sort of convertion?
       const gameArray = BuildMap_FromObject(obj)
       // Gets ParticipantAccountInfo Array
       const pai = gameArray[3][1].map(x => x)
       console.log(pai)
       // Gets Summoner Names In Current Game
       const allSummonerNames = gameArray[3][1].map(x => x.player.summonerName)
       console.log(allSummonerNames)
      }
      else{
      }
    }
  }
  function MatchDetails(participantDetails){
    const allChampionid = participantDetails.map(x => x.championId)
    console.log(allChampionid)
    const allParticipantid = participantDetails.map(x => x.participantId)
    console.log(allParticipantid)
    const allspell1id = participantDetails.map(x => x.spell1Id)
    console.log(allspell1id)
    const allspell2id = participantDetails.map(x => x.spell2Id)
    console.log(allspell2id)
    const allstats = participantDetails.map(x => x.stats)
    console.log(allstats)
    const allteamid = participantDetails.map(x => x.teamId)
    console.log(allteamid)
    const alltimeline = participantDetails.map(x => Object.entries(x.timeline))
    console.log(alltimeline)
  }
  function GetParticipants(mockObject){
    for(let obj of mockObject){
      console.log(typeof mockObject)
      if(typeof obj != Array.isArray()){
        const gameArray = BuildMap_FromObject(obj)
        // Gets participantDetails In Current Game
        const participantDetails = gameArray[4][1].map(x => x)
        console.log(participantDetails)
        //get MatchDetails
        MatchDetails(participantDetails)
      }
      else if(Array.isArray(obj)){
        //return Map
      }
    }
  }
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
          {console.log(CheckIfObjectInsideData(mockObject))}
          {console.log(GetParticipants(mockObject))}
          <ul>{mockObject.map(game =>
            <li key={game.id}>
              <p>id:{game.id}</p>
              <p>RiotGameId:{game.gameId}</p>
              <p>Game Duration: {game.gameDuration}</p>
              {/* <p>Participant-Info: {game.participantAccountInfo.map(participantInfo => <li key={participantInfo.participantId}>
              <p>{game.participantAccountInfo.player.map(player => 
              <li key={player.accountId}>
                <p>Name: {Object.values(player.summonerName)}</p>
              </li>)}</p>
              </li>)}</p> */}
              {/* <p>Participants: {game.participants}</p>
              <p>Teams: {game.teams}</p> */}
            </li>)}
          </ul>
        </div>
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
