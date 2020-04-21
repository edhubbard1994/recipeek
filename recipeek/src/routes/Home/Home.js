import React, { Component } from 'react';
import Searchbar from '../../components/Searchbar';
import styles from './Home.module.css';
import SearchResultCard from '../../components/SearchResultCard';
import GradientButton from '../../components/GradientButton';



export default class Home extends Component {
  constructor(props){
    super(props)
    this.state = {
      searchString: "",
      results: []
    }
  }

  btnCallback = async (inputText,stateVar) => {
    let reqData ={
      method: 'post',
      headers:{
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({keywords :inputText})
    }
    let results = await fetch('http://localhost:8000/api/search/',reqData)
        .then(res => res.json())
        .then(recipes => {this.setState({results: recipes}); console.log(recipes);})
  }


    render() {
        return (
          <div>
            <div className={styles.wrapper}>
              <div className={styles.header}>
                <h1>Recipeek</h1>
              </div>
              <div className={styles.search}>
                <Searchbar
                  label = 'Find your feast...'
                  onClick = {() => {this.btnCallback(this.state.searchString,this.setState);this.setState({searchString: ""})}}
                  searchInput = ''
                  onChange = { (e) => this.setState({searchString: e.target.value}) }
                />
              </div>
              <div className={styles.button}>
                <GradientButton
                  label = {'Advanced'}
                  onClick = {() => {alert('Keywords:\nhas: to specify required term\ndiet: vegan, vegetarian, paleo, dairy-free, wheat-free, fat-free, low-sugar, egg-free, peanut-free, tree-nut-free, soy-free, fish-free, shellfish-free')}}
                />
              </div>
            </div>
            <div className={styles.results}>
              <ul> {this.state.results.map(result =>
                <li>
                  <SearchResultCard
                    recipeImageURL={result.imageUrl}
                    recipeURL={result.url}
                    recipeName={result.name}
                    calories={result.calories}
                    diet={result.diets}
                  />
                </li>
              )}</ul>
            </div>
          </div>
        );
    }
}
