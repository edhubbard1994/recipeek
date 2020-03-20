import React, { Component } from 'react';
import Searchbar from '../../components/Searchbar';
import styles from './Home.module.css';

export default class Home extends Component {
    render() {
        return (
            <div className={styles.wrapper}>
              <div className={styles.header}>
                <h1>Recipeek</h1>
              </div>
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
