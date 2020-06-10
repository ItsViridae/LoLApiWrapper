import React from 'react'
import APIClient from '../apiClient'


class Home extends React.Component {
    state = {
        value: 0,
        gameDtoObject: []
    };

 async componentDidMount() {
    const accessToken = await this.props.auth.getAccessToken()
    this.apiClient = new APIClient(accessToken);
    this.apiClient.getGameDto().then((data) =>
      this.setState({...this.state, gameDtoObject: data})
    );
  }
onClick = (event) => {

}
updateGameDto = (newGameObject) => {
    this.setState({
        ...this.state, gameDtoObject: []
    })
}
renderAllGames = (gameDtoObject) => {
    if(!gameDtoObject) {return [] }
    return gameDtoObject.map((newGameObject) => {
        return (
            <Grid item xs={12} md={3} key={newGameObject[0]}>
                
            </Grid>
        )
    })
}
 


 //#TODO: Return and Render Method...
 render() {
    return (
      <div className={styles.root}>
          <button>Get GameDto</button>
      </div>
    );
  }
};

export default Home;