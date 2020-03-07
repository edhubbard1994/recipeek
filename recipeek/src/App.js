import React from 'react';
import './styles/App.css';
import Home from './routes/Home';
import { Route } from 'react-router-dom'

class App extends React.Component {

  constructor(){
    super()
    this.state = {
      recipes: {"hello":"world"}
    }
    console.log('HELLO')
    this.getData();
  }

  getData = ()=>{

    //TODO: MAKE THIS WORK WITH DNS RESOLUTION
    fetch('http://localhost:8000/api/recipe')
      .then(response => response.json())
      .then(data => this.setState({recipes: data}))

  }

  render(){

    return (
      <div className="App">
        <Route exact path="/" component={Home} />
      </div>
    );
  }
}

export default App;
