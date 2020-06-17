import { data } from './data.mjs'; 
import { mockData } from './mockGameData.mjs';
import { obj } from './gameData.mjs';

function getGameSpecificDetails(obj){
    let gameDuration = obj.gameDuration;
    let gameId = obj.gameId;
    let id = obj.id;
    console.log(gameDuration, gameId, id)
}

function getParticiants(obj){
    let participantsArray = obj.participants;
    for(let object in participantsArray){
        for(let key in object){
            console.log(participantsArray[object[key]])
        }
    }
}
function getTeams(obj){
    let teamsArray = obj.teams;
    for(let object in teamsArray){
        for(let key in object){
            console.log(teamsArray[object[key]])
        }
    }
}
getGameSpecificDetails(obj);
//getParticiants(obj);
//getTeams(obj);
