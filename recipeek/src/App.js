import React from 'react';
import logo from './logo.svg';
import './App.css';

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
        <p>{JSON.stringify(this.state.recipes)}</p>
      </div>
    );
  }
}

export default App;
