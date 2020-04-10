import React, { Component } from 'react';
import Searchbar from '../../components/Searchbar';
import styles from './Home.module.css';

export default class Home extends Component {
  constructor(props){
    super(props)
    this.state = {
      searchString: ""
    }
  }

    render() {
        return (
            <div className={styles.wrapper}>
              <div className={styles.header}>
                <h1>Recipeek</h1>
              </div>
              <div className={styles.search}>
                <Searchbar
                  label = 'Find your feast...'
                  onClick = {()=>{btnCallback(this.state.searchString);this.setState({searchString: ""})}}
                  searchInput = ''
                  onChange = { (e) => this.setState({searchString: e.target.value}) }
                />
              </div>
            </div>
        );
    }
}

let btnCallback = async (inputText) => {
  let reqData ={
    method: 'post',
    headers:{
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({keywords :inputText})
  }
  let results = await fetch('http://localhost:8000/api/search/',reqData)
      .then(res => res.json())
      .then(recipes => console.log(recipes))
}


