import React, { Component } from 'react';
import Searchbar from '../../components/Searchbar';
import styles from './SearchResults.module.css';
import logo from '../../assets/recipeek-logo.png';

export default class SearchResults extends Component {
    render() {
        return (
          <div className={styles.wrapper}>
            <img
              src={logo}
              alt={"logo"}
              className={styles.logo}
            />
            <div className={styles.search}>
              <Searchbar
                label = 'Find your feast...'
                onClick = {() => {alert('Button Clicked')}}
                searchInput = ''
                onChange = { () => {alert('onChange')} }
              />
            </div>
          </div>
        );
    }
}
